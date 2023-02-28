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
W = 30
H = 40

fig = plt.figure(figsize=(W, H))

#scenario 1, Earth, Venus, Sun in line
#view top-down from ecliptic
#draw Sun
plt.scatter(200, 0, s = 400000, marker = '.', color = sKy_colors['orange'])
plt.text(s = 'Sun', x = 200, y = 0, fontsize = 100, color = sKy_colors['very dark blue'], font = font2, weight = 'bold', horizontalalignment = 'center', verticalalignment = 'center')
plt.text(s = 'Prograde\nVenus', x = 1000, y = 1150, font = font2, weight = 'bold', color = 'white', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 50)



#drawing Venus and its orbit
u = 200
v = 0
a = 400
b = 900
t1 = np.linspace(0, 2*np.pi, 1000)
plt.plot(u+a*np.cos(t1), v+b*np.sin(t1), color = sKy_colors['very dark blue'], linestyle = '--', linewidth =6, zorder = 0)


venus_locs = [(600, 0), (550, 400),(500, 590) ]
earth_locs = [(840, -550), (890, -200), (900, 0)]

for i in range(len(venus_locs)):
    v_loc = venus_locs[i]
    e_loc = earth_locs[i]
    vx = v_loc[0]
    vy = v_loc[1]
    plt.scatter(vx, vy, s = 10000, marker = '.', color = sKy_colors['blue'])
    
    ex = e_loc[0]
    ey = e_loc[1]
    plt.scatter(ex, ey, s = 10000, marker = '.', color = sKy_colors['light blue'])
    
    plt.plot([vx, ex],[vy, ey], zorder = -5, linestyle = '--', color = sKy_colors['orange'], linewidth = 4)
    
    plt.text(s = str(i+1), x = vx, y = vy, fontsize = 30, color = 'black', font = font2, weight = 'bold', horizontalalignment = 'center', verticalalignment = 'center')
    
    plt.text(s = str(i+1), x = ex, y = ey, fontsize = 30, color = 'black', font = font2, weight = 'bold', horizontalalignment = 'center', verticalalignment = 'center')
    
    

    
plt.text(s = 'Venus', x = 550, y = 590, fontsize = 50, color = 'white', font = font2, weight = 'bold', horizontalalignment = 'left', verticalalignment = 'center')
plt.arrow(x = 500, y = 650, dx = -20, dy = 50, color = sKy_colors['red'], zorder = 100, width = 15)

plt.arrow(x = 500, y = 650, dx = -20, dy = 50, color = sKy_colors['red'], zorder = 100, width = 15)


#drawing Earth and its orbit
u = 200
v = 0
a = 700
b = 1400
t1 = np.linspace(0, 2*np.pi, 1000)
plt.plot(u+a*np.cos(t1), v+b*np.sin(t1), color = sKy_colors['light blue'], linestyle = '--', linewidth =6, zorder = 0)

plt.text(s = 'Earth', x = 950, y = 0, fontsize = 50, color = 'white', font = font2, weight = 'bold', horizontalalignment = 'left', verticalalignment = 'center')
plt.arrow(x = 900, y =60, dx = 0, dy = 50, color = sKy_colors['red'], zorder = 100, width = 15)


#drawing line of sight from Venus to Earth


#Earth-sky view

#draw Earth's surface
u = 300
v = -4300
a = 900
b = 600
t1 = np.linspace(np.pi, 0, 100)
plt.plot(u+a*np.cos(t1), v+b*np.sin(t1), color = sKy_colors['dull brown'], alpha = 0.8, linewidth =250, zorder = 0)

#draw sun in Earth's sky
plt.scatter(-200, -2500, s = 200000, marker = '.', color = sKy_colors['orange'])
plt.text(s = 'Sun', x = -200, y = -2500, fontsize = 70, color = sKy_colors['very dark blue'], font = font2, weight = 'bold', horizontalalignment = 'center', verticalalignment = 'center')

#draw venus in Earth's sky
for i in range(len(venus_locs)):
    
    plt.scatter((600/len(venus_locs))*i, -2500, s = 10000, marker = '.', color = sKy_colors['blue'])
    plt.text(s = str(i+1), x = (600/len(venus_locs))*i, y = -2500, fontsize = 30, color = 'black', font = font2, weight = 'bold', horizontalalignment = 'center', verticalalignment = 'center')
plt.arrow(x = 440, y =-2500, dx = 70, dy = 0, color = sKy_colors['red'], zorder = 100, width = 50, head_length = 30)

plt.arrow(x = 240, y =-2500, dx = 70, dy = 0, color = sKy_colors['red'], zorder = 100, width = 50, head_length = 30)

plt.arrow(x = 40, y =-2500, dx = 70, dy = 0, color = sKy_colors['red'], zorder = 100, width = 50, head_length = 30)

plt.text(s = 'Venus', x = 200, y = -2300, fontsize = 50, color = sKy_colors['very dark blue'], font = font2, weight = 'bold', horizontalalignment = 'left', verticalalignment = 'center')

plt.vlines(0, -4000, -1500, color = sKy_colors['blue grey'], linewidth = 10000000000, zorder = -99)
plt.text(s = 'Earth', x = 200, y = -3700, fontsize = 50, color = 'white', font = font2, weight = 'bold', horizontalalignment = 'left', verticalalignment = 'center')



plt.vlines(0, -1500, 1700, color = 'black', linewidth = 1000000000, zorder = -99)

#draw stick figure

person_color = 'black'
plt.scatter(300, -3100, s = 10000, marker = '.', color = person_color)
plt.plot([300, 300], [-3100, -3300], color = person_color, linewidth = 10)
#legs
plt.plot([300, 350], [-3300, -3370], color = person_color, linewidth = 10)
plt.plot([300, 250], [-3300, -3370], color = person_color, linewidth = 10)
#arms
plt.plot([300, 350], [-3250, -3180], color = person_color, linewidth = 10)
plt.plot([300, 250], [-3250, -3180], color = person_color, linewidth = 10)

plt.xlim([-600, 1200])
plt.xticks([])
plt.ylim(-4000, 1500)
plt.yticks([])
plt.savefig('Earth_Venus_Sun_Prog.png', bbox_inches = 'tight')
plt.close()








#retrograde


plt.rcParams["font.family"] = 'Shree Devanagari 714'
plt.rc('axes', unicode_minus=False)
W = 30
H = 40

fig = plt.figure(figsize=(W, H))

#scenario 1, Earth, Venus, Sun in line
#view top-down from ecliptic
#draw Sun
plt.scatter(200, 0, s = 400000, marker = '.', color = sKy_colors['orange'])
plt.text(s = 'Sun', x = 200, y = 0, fontsize = 100, color = sKy_colors['very dark blue'], font = font2, weight = 'bold', horizontalalignment = 'center', verticalalignment = 'center')
plt.text(s = 'Retrograde\nVenus', x = 1000, y = 1150, font = font2, weight = 'bold', color = 'white', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 50)



#drawing Venus and its orbit
u = 200
v = 0
a = 400
b = 900
t1 = np.linspace(0, 2*np.pi, 1000)
plt.plot(u+a*np.cos(t1), v+b*np.sin(t1), color = sKy_colors['very dark blue'], linestyle = '--', linewidth =6, zorder = 0)


venus_locs = [(500, 590),(200, 900), (-100, 600)]
earth_locs = [(900, 0),(880, 350),(830, 600)]

for i in range(len(venus_locs)):
    v_loc = venus_locs[i]
    e_loc = earth_locs[i]
    vx = v_loc[0]
    vy = v_loc[1]
    plt.scatter(vx, vy, s = 10000, marker = '.', color = sKy_colors['blue'])
    
    ex = e_loc[0]
    ey = e_loc[1]
    plt.scatter(ex, ey, s = 10000, marker = '.', color = sKy_colors['light blue'])
    
    plt.plot([vx, ex],[vy, ey], zorder = -5, linestyle = '--', color = sKy_colors['orange'], linewidth = 4)
    plt.text(s = str(i+1), x = vx, y = vy, font = font2, weight = 'bold', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 30, color = 'black')
    
    plt.text(s = str(i+1), x = ex, y = ey, font = font2, weight = 'bold', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 30, color = 'black')

    
plt.text(s = 'Venus', x = 200, y = 1050, fontsize = 50, color = 'white', font = font2, weight = 'bold', horizontalalignment = 'center', verticalalignment = 'center')
plt.arrow(x = 500, y = 650, dx = -20, dy = 50, color = sKy_colors['red'], zorder = 100, width = 15)
plt.arrow(x = 180, y = 900, dx = -50, dy = 0, color = sKy_colors['red'], zorder = 0, width = 50, head_length = 30)
plt.arrow(x = -100, y = 600, dx = -30, dy = -80, color = sKy_colors['red'], zorder = 0, width = 30, head_length = 30)


#drawing Earth and its orbit
u = 200
v = 0
a = 700
b = 1400
t1 = np.linspace(0, 2*np.pi, 1000)
plt.plot(u+a*np.cos(t1), v+b*np.sin(t1), color = sKy_colors['light blue'], linestyle = '--', linewidth =6, zorder = 0)

plt.text(s = 'Earth', x = 950, y = 0, fontsize = 50, color = 'white', font = font2, weight = 'bold', horizontalalignment = 'left', verticalalignment = 'center')



#drawing line of sight from Venus to Earth


#Earth-sky view

#draw Earth's surface
u = 300
v = -4300
a = 900
b = 600
t1 = np.linspace(np.pi, 0, 100)
plt.plot(u+a*np.cos(t1), v+b*np.sin(t1), color = sKy_colors['dull brown'], alpha = 0.8, linewidth =250, zorder = 0)

#draw sun in Earth's sky
plt.scatter(-200, -2500, s = 200000, marker = '.', color = sKy_colors['orange'])
plt.text(s = 'Sun', x = -200, y = -2500, fontsize = 70, color = sKy_colors['very dark blue'], font = font2, weight = 'bold', horizontalalignment = 'center', verticalalignment = 'center')

#draw venus in Earth's sky
    
plt.scatter(0, -2500, s = 10000, marker = '.', color = sKy_colors['blue'])
plt.text(s = str(1), x = 0, y = -2500, font = font2, weight = 'bold', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 30, color = 'black')

plt.scatter(300, -2500, s = 10000, marker = '.', color = sKy_colors['blue'])
plt.text(s = str(3), x = 300, y = -2500, font = font2, weight = 'bold', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 30, color = 'black')

plt.scatter(400, -2500, s = 10000, marker = '.', color = sKy_colors['blue'])
plt.text(s = str(2), x = 400, y = -2500, font = font2, weight = 'bold', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 30, color = 'black')

plt.arrow(x = 40, y =-2500, dx = 70, dy = 0, color = sKy_colors['red'], zorder = 100, width = 50, head_length = 30)

plt.arrow(x = 260, y =-2500, dx = -70, dy = 0, color = sKy_colors['red'], zorder = 100, width = 50, head_length = 30)

plt.text(s = 'Venus', x = 200, y = -2300, fontsize = 50, color = sKy_colors['very dark blue'], font = font2, weight = 'bold', horizontalalignment = 'left', verticalalignment = 'center')

plt.vlines(0, -4000, -1500, color = sKy_colors['blue grey'], linewidth = 10000000000, zorder = -99)
plt.text(s = 'Earth', x = 200, y = -3700, fontsize = 50, color = 'white', font = font2, weight = 'bold', horizontalalignment = 'left', verticalalignment = 'center')


#draw stick figure

person_color = 'black'
plt.scatter(300, -3100, s = 10000, marker = '.', color = person_color)
plt.plot([300, 300], [-3100, -3300], color = person_color, linewidth = 10)
#legs
plt.plot([300, 350], [-3300, -3370], color = person_color, linewidth = 10)
plt.plot([300, 250], [-3300, -3370], color = person_color, linewidth = 10)
#arms
plt.plot([300, 350], [-3250, -3180], color = person_color, linewidth = 10)
plt.plot([300, 250], [-3250, -3180], color = person_color, linewidth = 10)



#scenario 3, CO WD is disrupted is gone, He shell will detonate

#draw one WD
#this one will have He shell



plt.vlines(0, -1500, 1700, color = 'black', linewidth = 1000000000, zorder = -99)

plt.xlim([-600, 1200])
plt.xticks([])
plt.ylim(-4000, 1500)
plt.yticks([])
plt.savefig('Earth_Venus_Sun_Ret.png', bbox_inches = 'tight')
plt.close()

