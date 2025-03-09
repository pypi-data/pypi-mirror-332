import torch.nn.utils.rnn as rnn_utils
from torch import nn
import torch
import torch.nn.functional as F
import torch.optim as optim
import os 

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

class Encoder(nn.Module):
    def __init__(self, input_size, hidden_size, latent_size):
        super(Encoder, self).__init__()
        
        self.hidden_size = hidden_size
        self.latent_size = latent_size
        
        self.gru1 = nn.GRU(input_size, hidden_size, batch_first=True, num_layers=1)
        self.gru2 = nn.GRU(hidden_size, hidden_size, batch_first=True)

        
        self.fc1 = nn.Linear(hidden_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, hidden_size)
        self.fc4 = nn.Linear(hidden_size, hidden_size)
        
        
        self.fc_mu = nn.Linear(hidden_size, latent_size)
        self.fc_logvar = nn.Linear(hidden_size, latent_size)
        
    
    def forward(self, x, lengths):
        
        packed_input = rnn_utils.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
        packed_output, hidden = self.gru1(packed_input)
        
        
        final_gru =  hidden[-1]
        
        concat = hidden[-1]

        x = F.tanh(self.fc1(concat))
        x = F.tanh(self.fc2(x))
        x = F.tanh(self.fc3(x))
        x = F.tanh(self.fc4(x))
        
        mu = (self.fc_mu(x))
        logvar = F.relu(self.fc_logvar(x))
        
        
        # Reparameterization trick
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        z = mu + eps * std
        
        return z, mu, logvar

class Decoder(nn.Module):
    def __init__(self, hidden_size, latent_size, output_size):
        super(Decoder, self).__init__()
        
        self.hidden_size = hidden_size
        self.latent_size = latent_size
        self.output_size = output_size
        
        self.gru_out = nn.GRU(latent_size, hidden_size, batch_first=True)
        
        self.fc0 = nn.Linear(latent_size, hidden_size)
        self.fc1 = nn.Linear(hidden_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.output = nn.Linear(hidden_size, 656)

    def forward(self, z, lengths):

        
        z = z.unsqueeze(1)
        x = F.relu(self.fc0(z))
        x = F.relu(self.fc1(x))
        x = F.sigmoid(self.fc2(x))

        output = self.output(x).transpose(1, 2)
        
        return output
    
class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MLP, self).__init__()
        
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, hidden_size)
        
        self.output = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        
        output = self.output(x)
        
        return output
        

    
class FoundationModel(nn.Module):
    def __init__(self, input_size, hidden_size, latent_size, output_size, num_classes=12):
        super(FoundationModel, self).__init__()
        
        self.encoder = Encoder(input_size, hidden_size, latent_size)
        self.decoder = Decoder(hidden_size, latent_size, output_size)
        self.cls = nn.Linear(latent_size, num_classes)
        
    def forward(self, x, lengths):
        z, mu, logvar = self.encoder(x, lengths)
        clas = self.cls(mu)
        return clas, mu, logvar
    
    
    
    def recon_loss(self, x, recon_x, lengths, mask=None):
        if (mask == None):
            mask = torch.ones_like(x[:, :, 0], dtype=torch.bool)
        
        for i, length in enumerate(lengths):
            mask[i, length:] = 0
        
        mse_loss_fn = nn.MSELoss(reduction='none')
    
        
        loss = mse_loss_fn(x[:, :, 2:3], recon_x)

        masked_loss = loss * mask.unsqueeze(-1)
        masked_loss = masked_loss.sum() / mask.sum()
        return masked_loss
    
    def kl_divergence(self, mu, logvar):
        # KL divergence between the latent distribution and a standard normal distribution
        kl = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
        return kl

    def total_loss(self, x, recon_x, lengths, mu, logvar, mask=None):
        recon_loss = self.recon_loss(x, recon_x, lengths, mask)
        kl_loss = self.kl_divergence(mu, logvar) / x.size(0)  # Normalize by batch size
        return recon_loss + kl_loss

    
    def contrastive_loss(self, latent1, latent2, label, margin=0.5):
        cosine_similarity = F.cosine_similarity(latent1, latent2)
        positive_loss = label * (1 - cosine_similarity)  # for similar pairs
        negative_loss = (1 - label) * (cosine_similarity)  # for dissimilar pairs

        loss = positive_loss
        return loss.mean()

class FM:
    def __init__(self, device, model_type=None):
        '''
        Creates a foundation model of the specified type:
            "classifier", "contrastive", "adversarial"
        '''
        self.input = 3
        self.recurrent = 200
        self.latent=100
        self.decoder=1
        self.num_classes=8
        self.model = FoundationModel(self.input, self.recurrent, self.latent, self.decoder, self.num_classes)
        self.model.to(device)
        if (model_type != None):
            self.model.load_state_dict(torch.load(os.path.join(SCRIPT_DIR, "Models", model_type + '.pth')))
        

