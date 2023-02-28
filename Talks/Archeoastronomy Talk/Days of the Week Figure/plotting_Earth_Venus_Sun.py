import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '/Users/sky5265/Documents/GitHub/Astro_Code')
from Astro_useful_funcs import *
from Analysis_useful_funcs import *
from PIL import Image
import matplotlib.patches as patches
from matplotlib.patches import Rectangle





def plot_days(day_names, saveloc, fontsize = 110, rect_color = sKy_colors['blue']):


    plt.rcParams["font.family"] = 'Shree Devanagari 714'
    plt.rc('axes', unicode_minus=False)
    W = 30
    H = 40

    fig, ax = plt.subplots(figsize = (W,H))
    x = 2
    dx = 5
    y_init = 10
    dy = -3
    y_spacing = -0.5

    for i in range(len(day_names)):
        name = day_names[i]
        ax.add_patch(Rectangle((x,y_init+i*(dy+y_spacing)), dx, dy, edgecolor = sKy_colors['very dark blue'], facecolor = rect_color))
        ax.text(x = x+dx/2, y = y_init+(i+0.5)*(dy+y_spacing), horizontalalignment = 'center', verticalalignment = 'center', s = name, font = font2, weight = 'bold', fontsize = fontsize, color = sKy_colors['orange'])
        

    ax.set_xlim([x, x+2*dx])
    ax.set_ylim([y_init+8*(dy+y_spacing), y_init-dy])
    plt.axis('off')
    
    plt.savefig(saveloc)
    plt.close()


day_names_eng = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

plot_days(day_names_eng, saveloc = 'Day Names English.png')

day_names_span = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']

plot_days(day_names_span, saveloc = 'Day Names Spanish.png')

day_names_tel = ['Soma Vaaram', 'Mangala Vaaram', 'Budha Vaaram', 'Guru Vaaram', 'Sukra Vaaram', 'Sani Vaaram', 'Aadi Vaaram']

plot_days(day_names_tel, saveloc = 'Day Names Telugu.png', fontsize = 80)


planet_names_eng = ['Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn', 'Sun']
plot_days(planet_names_eng, saveloc = 'Planet Names English.png', rect_color = sKy_colors['blue grey'])
