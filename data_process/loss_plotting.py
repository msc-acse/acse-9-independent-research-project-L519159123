"""
author : Yuxuan Liu
github alias: L519159123
"""

import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def plot_loss(experiment_name, model='pix2pix'):
    """Plot plg loss of the training process
    
    Parameters:
        experiment_name (string)
        model (string) - pix2pix by default
    
    """
    
    # load data file
    data = pd.read_csv(os.path.join('./checkpoints', experiment_name, 'loss_log.txt'), skiprows=1, sep='\s*', engine='python', header=None)
    
    if model == 'pix2pix':
        epoch = data[1].str.replace(',', '').astype('int')
        iters = data[3].str.replace(',', '').astype('int') / 1928
        epoch = epoch + iters - 1
        
        # convert string to float32 data
        G_GAN = data[9].astype('float32')
        G_L1 = data[11].astype('float32')
        D_real = data[13].astype('float32')
        D_fake = data[15].astype('float32')
        
        plt.figure(figsize=(15,8))
        plt.xlabel('epoch', fontsize=18, labelpad=20)
        plt.ylabel('loss', fontsize=18, labelpad=20)
        plt.title(experiment_name + 'loss over time', fontsize=18, pad=30)
        plt.plot(epoch.values, G_GAN.values, 'b', label='G_GAN')
        plt.plot(epoch.values, G_L1.values, 'C1', label='G_L1')
        plt.plot(epoch.values, D_real.values, 'g', label='D_real')
        plt.plot(epoch.values, D_fake.values, 'r', label='D_fake')
        plt.tick_params(labelsize=14)
        plt.legend(loc='best', fontsize=14)
        plt.grid(True)
        # save the png image into the corresponding dir 
        plt.savefig(os.path.join('./results', experiment_name, 'test_latest', experiment_name + '.png'))
        plt.show()
        
    if model == 'cyclegan':
        epoch = data[1].str.replace(',', '').astype('int')
        iters = data[3].str.replace(',', '').astype('int') / 1928
        epoch = epoch + iters - 1

        D_A = data[9].astype('float32')
        G_A = data[11].astype('float32')
        cycle_A = data[13].astype('float32')
        idt_A = data[15].astype('float32')
        
        D_B = data[17].astype('float32')
        G_B = data[19].astype('float32')
        cycle_B = data[21].astype('float32')
        idt_B = data[23].astype('float32')
        
        plt.figure(figsize=(15,8))
        plt.xlabel('epoch', fontsize=18, labelpad=20)
        plt.ylabel('loss', fontsize=18, labelpad=20)
        plt.title(experiment_name + 'loss over time', fontsize=18, pad=30)
        plt.plot(epoch.values, D_A.values, 'C1', label='D_A')
        plt.plot(epoch.values, G_A.values, 'C2', label='G_A')
        plt.plot(epoch.values, cycle_A.values, 'C3', label='cycle_A')
        plt.plot(epoch.values, idt_A.values, 'C4', label='idt_A')
        plt.plot(epoch.values, D_B.values, 'C5', label='D_B')
        plt.plot(epoch.values, G_B.values, 'C6', label='G_B')
        plt.plot(epoch.values, cycle_B.values, 'C7', label='cycle_B')
        plt.plot(epoch.values, idt_B.values, 'C8', label='idt_B')
        plt.tick_params(labelsize=14)
        plt.legend(loc='best', fontsize=14)
        plt.grid(True)
        plt.savefig(os.path.join('./results', experiment_name, 'test_latest', experiment_name + '.png'))
        plt.show()

