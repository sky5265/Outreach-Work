import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '/Users/sky5265/Documents/GitHub/Astro_Code')
from Astro_useful_funcs import *
from Analysis_useful_funcs import *
from PIL import Image
import matplotlib.patches as patches


plt.rcParams["font.family"] = 'Shree Devanagari 714'
plt.rc('axes', unicode_minus=False)
W = 17
H = 10

fig = plt.figure(figsize=(W, H))

#draw a really big 7
plt.axis('off')
plt.text(s = '7', x = 0, y = 0, color = sKy_colors['mute red'], fontsize = 600, font = font1, rotation = 0, horizontalalignment = 'center', verticalalignment = 'center')
plt.xlim([-0.05, 0.05])
plt.ylim([-0.1, 0.1])
plt.savefig("7-red.png", bbox_inches = 'tight')
plt.close()

fig = plt.figure(figsize=(W, H))

#draw a really big 7
plt.axis('off')
plt.text(s = '7', x = 0, y = 0, color = sKy_colors['blue'], fontsize = 600, font = font1, rotation = 0, horizontalalignment = 'center', verticalalignment = 'center')
plt.xlim([-0.05, 0.05])
plt.ylim([-0.1, 0.1])
plt.savefig("7-blue.png", bbox_inches = 'tight')
plt.close()

fig = plt.figure(figsize=(W, H))
plt.axis('off')
plt.text(s = '7', x = 0, y = 0, color = sKy_colors['orange'], fontsize = 600, font = font1, rotation = 0, horizontalalignment = 'center', verticalalignment = 'center')
plt.xlim([-0.05, 0.05])
plt.ylim([-0.1, 0.1])
plt.savefig("7-orange.png", bbox_inches = 'tight')
plt.close()

fig = plt.figure(figsize=(W, H))

#draw a really big 7
plt.axis('off')
plt.text(s = '7', x = 0, y = 0, color = sKy_colors['very dark blue'], fontsize = 600, font = font2, rotation = 0, horizontalalignment = 'center', verticalalignment = 'center')
plt.xlim([-0.05, 0.05])
plt.ylim([-0.1, 0.1])
plt.savefig("7-blue.png", bbox_inches = 'tight')
plt.close()

fig = plt.figure(figsize=(W, H))

#draw a really big 7
plt.axis('off')

plt.text(s = '7', x = 0, y = 0, color = sKy_colors['blue grey'], fontsize = 600, font = font2, rotation = 0, horizontalalignment = 'center', verticalalignment = 'center')
plt.xlim([-0.05, 0.05])
plt.ylim([-0.1, 0.1])
plt.savefig("7-blue grey.png", bbox_inches = 'tight')

plt.close()
