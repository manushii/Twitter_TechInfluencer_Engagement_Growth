#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


names_info_spread = ['Lesley Carhart', 'Chris Pirillo', 'Sam Sheffer', 'Carla Gentry', 'Dino A. Dai Zovi']
snp_values_info_spread = [122.35, 292.79, 325.95, 82.02, 367.92]


names_followed = ['TensorFlow', 'Microsoft Teams', 'PyTorch', 'KDnuggets', 'Romain Lanéry']
snp_values_followed = [19.12, 0.72, 62.34, 2.38, 3.89]


import matplotlib.pyplot as plt


names_info_spread = ['Lesley Carhart', 'Chris Pirillo', 'Sam Sheffer', 'Carla Gentry', 'Dino A. Dai Zovi']
snp_values_info_spread = [122.35, 292.79, 325.95, 82.02, 367.92]


plt.figure(figsize=(15, 8))
plt.bar(names_info_spread, snp_values_info_spread, color='skyblue', width=0.4)
plt.ylabel('SNP Values', fontsize=14)
plt.title('Information Spreadability Influencers', fontsize=25)
plt.xticks(rotation=0, fontsize=16)


for i, value in enumerate(snp_values_info_spread):
    plt.text(i, value, f'{value:.2f}', ha='center', va='bottom', fontsize=14)


plt.tight_layout()
plt.show()




plt.figure(figsize=(15, 8))
plt.bar(names_followed, snp_values_followed, color='lightgreen', width=0.4)
plt.ylabel('SNP Values', fontsize=14)  
plt.title('Top Followed Influencers', fontsize=25)  
plt.xticks(rotation=0, fontsize=16)  
plt.ylim(0, 400)  

for i, value in enumerate(snp_values_followed):
    plt.text(i, value, f'{value:.2f}', ha='center', va='bottom', fontsize=14)  # Increase font size for annotations


plt.tight_layout()
plt.show()

