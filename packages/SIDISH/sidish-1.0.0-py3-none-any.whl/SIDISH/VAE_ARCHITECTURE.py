################################## IMPORT LIBRARY ############################
import os
import torch
import torch.nn as nn
import numpy as np
import torch
import torch.nn as nn

import pyro.contrib.examples.util
from pyro.distributions.zero_inflated import ZeroInflatedNegativeBinomial

import torch.nn.functional as F
from torch.distributions import kl_divergence as KL
from torch.distributions import Normal

# assert pyro.__version__.startswith('1.8.4')
pyro.distributions.enable_validation(False)

################################ MODEL ARCHITECTURE #########################################

class Decoder(nn.Module):
    def __init__(self, input_dim, z_dim, layer_dims, dropout=0):
        super(Decoder, self).__init__()
        layers = []
        in_dim = z_dim
        for dim in layer_dims:

            layers.append(nn.Linear(in_dim, dim))
            
            if dropout > 0:
                layers.append(nn.Dropout(dropout))
            else:
                None
                
            layers.append(nn.Softplus())
            #layers.append(nn.BatchNorm1d(dim))

            in_dim = dim

        self.before_last_layer = nn.Sequential(*layers)
        self.last_layer_1 = nn.Linear(in_dim, input_dim)
        self.last_layer_2 = nn.Linear(in_dim, input_dim)

    def forward(self, z):
        bll = self.before_last_layer(z)
        mu = self.last_layer_1(bll)
        dropout_logits = self.last_layer_2(bll)

        return torch.exp(mu), dropout_logits


class Encoder(nn.Module):
    def __init__(self, input_dim, z_dim, layer_dims, dropout=0):
        super(Encoder, self).__init__()
        layers = []
        in_dim = input_dim
        self.var_eps = 1e-4
        for dim in layer_dims:
            layers.append(nn.Linear(in_dim, dim))
            
            if dropout > 0:
                layers.append(nn.Dropout(dropout))
            else:
                None
                
            layers.append(nn.Softplus())
            #layers.append(nn.BatchNorm1d(dim))
         
            in_dim = dim

        self.before_last_layer = nn.Sequential(*layers)
        self.fc_mean = nn.Linear(in_dim, z_dim)
        self.fc_logvar = nn.Linear(in_dim, z_dim)

    def forward(self, x):
        hidden = self.before_last_layer(x)
        mean = self.fc_mean(hidden)
        logvar = self.fc_logvar(hidden) # + self.var_eps
        return mean, logvar


class ARCHITECTURE(nn.Module):

    def __init__(self, input_dim, z_dim, layer_dims, seed, dropout=0.5, use_cuda=False):
        super(ARCHITECTURE, self).__init__()

        self.seed = seed

        torch.manual_seed(self.seed)
        torch.cuda.manual_seed(self.seed)
        torch.backends.cudnn.deterministic = True
        np.random.seed(self.seed)
        os.environ["PYTHONHASHSEED"] = str(self.seed)

        self.input_dim = input_dim
        self.z_dim = z_dim
        self.layer_dims = layer_dims
        self.use_cuda = use_cuda

        self.log_theta = torch.nn.Parameter(torch.randn(self.input_dim))

        # create the encoder and decoder networks
        self.encoder = Encoder(self.input_dim, self.z_dim, self.layer_dims, dropout)
        self.decoder = Decoder(self.input_dim, self.z_dim, self.layer_dims[::-1], dropout)

    def reparameterize(self, mu, logvar):
        # Normal(mu, logvar).rsample()
        '''std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)'''
        return Normal(mu, logvar).rsample() #mu + eps * std

    def forward(self, x):
        x = torch.log(x + 1)
        mu_encoder, logvar = self.encoder(x.view(-1, self.input_dim))
        z = self.reparameterize(mu_encoder, logvar)

        # zinb distribution
        mu_decoder, dropout_logits = self.decoder(z)
        return mu_decoder, dropout_logits, mu_encoder, logvar

    def get_latent_representation(self, x):
        x = torch.log(x + 1)
        mu_encoder, logvar = self.encoder(x.view(-1, self.input_dim))
        return mu_encoder + torch.exp(0.5*logvar)

    def kl_d(self,mu, logvar):
        z_loc = torch.zeros_like(mu)
        z_scale = torch.ones_like(logvar)
        kl = KL(Normal(mu, logvar), Normal(z_loc, z_scale)).sum(dim=1)

        return kl #(-0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp(), dim=-1))

    def reconstruction_loss(self, x, mu, dropout_logits, w):
        '''
        x: input data
        mu: output of decoder
        dropout_logits: dropout logits of zinb distribution
        w: weights for each sample in x (same shape as x)
        '''
        theta = F.softplus(self.log_theta)
        nb_logits = (mu + 1e-5).log() - (theta + 1e-5).log()

        distribution = ZeroInflatedNegativeBinomial(total_count=theta, logits=nb_logits, gate_logits=dropout_logits, validate_args=False)

        log_prob = distribution.log_prob(x)

        log_prob = log_prob * w  # Apply the weights

        return -log_prob.sum(dim=-1)

    def loss_function(self, x,w, mu_decoder, dropout_logits, mu_encoder, logvar):
        reconstruction_loss = self.reconstruction_loss(x, mu_decoder, dropout_logits,w)
        kl_div = self.kl_d(mu_encoder, logvar)
        return torch.mean(reconstruction_loss, dim=0) + torch.mean(kl_div, dim=0)


######################################## END ############################################
