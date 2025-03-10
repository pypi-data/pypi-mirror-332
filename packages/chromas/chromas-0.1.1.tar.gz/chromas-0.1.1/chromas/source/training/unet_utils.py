import torch
import torch.nn as nn


# Define the U-Net model
class UNet3Layers(nn.Module):
    def __init__(self, num_classes: int=2):
        super(UNet3Layers, self).__init__()
        
        # Encoder
        self.enc_conv0 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
        )
        self.pool0 = nn.MaxPool2d(2)
        
        self.enc_conv1 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
        )
        self.pool1 = nn.MaxPool2d(2)
        
        self.enc_conv2 = nn.Sequential(
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
        )
        
        # Decoder
        self.upconv1 = nn.ConvTranspose2d(256, 128, kernel_size=2, stride=2)
        self.dec_conv1 = nn.Sequential(
            nn.Conv2d(256, 128, kernel_size=3, padding=1),  # Concatenate with encoder conv1 output
            nn.ReLU(inplace=True),
        )
        
        self.upconv0 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.dec_conv0 = nn.Sequential(
            nn.Conv2d(128, 64, kernel_size=3, padding=1),  # Concatenate with encoder conv0 output
            nn.ReLU(inplace=True),
        )
        
        self.final_conv = nn.Conv2d(64, num_classes, kernel_size=1)
        

    def forward(self, x):
        # Encoder path
        enc0 = self.enc_conv0(x)
        pool0 = self.pool0(enc0)
        
        enc1 = self.enc_conv1(pool0)
        pool1 = self.pool1(enc1)
        
        enc2 = self.enc_conv2(pool1)
        
        # Decoder path
        up1 = self.upconv1(enc2)
        up1 = torch.cat([up1, enc1], dim=1)  # Skip connection
        dec1 = self.dec_conv1(up1)
        
        up0 = self.upconv0(dec1)
        up0 = torch.cat([up0, enc0], dim=1)  # Skip connection
        dec0 = self.dec_conv0(up0)
        
        out = self.final_conv(dec0)
        return {'out': out, 'aux': None}
    

class UNet3LayersThin(UNet3Layers):
    def __init__(self, num_classes: int=2):
        super(UNet3LayersThin, self).__init__()
        
        # Encoder
        self.enc_conv0 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
        )
        self.pool0 = nn.MaxPool2d(2)
        
        self.enc_conv1 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
        )
        self.pool1 = nn.MaxPool2d(2)
        
        self.enc_conv2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
        )
        
        # Decoder
        self.upconv1 = nn.ConvTranspose2d(64, 32, kernel_size=2, stride=2)
        self.dec_conv1 = nn.Sequential(
            nn.Conv2d(64, 32, kernel_size=3, padding=1),  # Concatenate with encoder conv1 output
            nn.ReLU(inplace=True),
        )
        
        self.upconv0 = nn.ConvTranspose2d(32, 16, kernel_size=2, stride=2)
        self.dec_conv0 = nn.Sequential(
            nn.Conv2d(32, 16, kernel_size=3, padding=1),  # Concatenate with encoder conv0 output
            nn.ReLU(inplace=True),
        )
        
        self.final_conv = nn.Conv2d(16, num_classes, kernel_size=1)
        
    

class SmallUNet(nn.Module):
    def __init__(self, num_classes=2):
        super(SmallUNet, self).__init__()
        
        # Encoder
        self.enc_conv0 = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
        )
        self.pool0 = nn.MaxPool2d(2)
        
        self.enc_conv1 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
        )
        self.pool1 = nn.MaxPool2d(2)
        
        # Bottleneck
        self.bottleneck = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
        )
        
        # Decoder
        self.upconv1 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.dec_conv1 = nn.Sequential(
            nn.Conv2d(128, 64, kernel_size=3, padding=1),  # Concatenate with encoder conv1 output
            nn.ReLU(inplace=True),
        )
        
        self.upconv0 = nn.ConvTranspose2d(64, 32, kernel_size=2, stride=2)
        self.dec_conv0 = nn.Sequential(
            nn.Conv2d(64, 32, kernel_size=3, padding=1),  # Concatenate with encoder conv0 output
            nn.ReLU(inplace=True),
        )
        
        self.final_conv = nn.Conv2d(32, num_classes, kernel_size=1)
    
    def forward(self, x):
        # Encoder path
        enc0 = self.enc_conv0(x)
        pool0 = self.pool0(enc0)
        
        enc1 = self.enc_conv1(pool0)
        pool1 = self.pool1(enc1)
        
        # Bottleneck
        bottleneck = self.bottleneck(pool1)
        
        # Decoder path
        up1 = self.upconv1(bottleneck)
        up1 = torch.cat([up1, enc1], dim=1)
        dec1 = self.dec_conv1(up1)
        
        up0 = self.upconv0(dec1)
        up0 = torch.cat([up0, enc0], dim=1)
        dec0 = self.dec_conv0(up0)
        
        out = self.final_conv(dec0)
        return {'out': out, 'aux': None}
