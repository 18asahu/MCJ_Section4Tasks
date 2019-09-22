# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:35:39 2019

@author: ANWESHA
"""


import random
import numpy as np
import matplotlib.pyplot as plt

#LEVEL 1

rho_in = [1, 'p_x', 'p_y', 'p_z'] #E=1
#format = [Energy of particle, x_momentum, y_mometum, z_momentum]

E = float(rho_in[0])
E_a = random.random()
E_b = 1 - E_a

z_a = E_a/E
z_b = E_b/E

theta_a = random.uniform(0,(np.pi)/2)
theta_b = random.uniform(0,(np.pi)/2) #ALERT! -  CHECK RANGE FOR THETA_B IN 2D (2PI IR JUST PI OR PI-THETA_A)

#LEVEL2/3 for E_a

E_c = random.uniform(0,E_a)
E_d = E_a - E_c

theta_c = random.uniform(0,(np.pi)/2)
theta_d = random.uniform(0,(np.pi)/2)

z_ca = E_c/E_a
z_da = E_d/E_a

#LEVEL2/3 for E_b

E_e = random.uniform(0,E_b)
E_f = E_b - E_e

theta_e = random.uniform(0,(np.pi)/2)
theta_f = random.uniform(0,(np.pi)/2)

z_eb = E_e/E_b
z_fb = E_f/E_b



#PLOTTING TREE DIAGRAM


en_1 = [E,E_a]
x_c1 = [1,2]
plt.plot(x_c1,en_1, color = 'red')

en_2 = [E,E_b]
x_c2 = [1,2]
plt.plot(x_c2,en_2, color = 'red', label = '2nd generation particle production')

en_3 = [E_a,E_c]
x_c3 = [2,3]
plt.plot(x_c3,en_3 , color = 'black', label = '3rd generation particle production - ROUTE 1')

en_4 = [E_a,E_d]
x_c4 = [2,3]
plt.plot(x_c4,en_4, color = 'black')

en_5 = [E_b,E_e]
x_c5 = [2,3]
plt.plot(x_c5,en_5, color = 'green', label = '3rd generation particle production - ROUTE 2' )

en_6 = [E_b,E_f]
x_c6 = [2,3]
plt.plot(x_c6,en_6, color = 'green')

plt.xlabel('Generation')
plt.ylabel('Energy of particle')

        #SCATTER GRAPH FOR CLEARER VISUALISATION
Energies = [E, E_a, E_b, E_c, E_d, E_e, E_f]
x_coords = [1, 2, 2, 3, 3, 3, 3]

plt.scatter(x_coords, Energies, linewidth = 0.1)


plt.legend()
plt.show()

#print(E_c+E_d+E_e+E_f)


#OUTPUT 4-MOMENTUM VECTOR CALCULATION:

Gen3_Energies = [E_c,E_d,E_e,E_f]

print('These are the energies for the third generation of partons.')
print('Assume that these are the options available for the observed partons:')
print(E_c,',',E_d,',',E_e,',',E_f)




z_test = []
theta_test = []

i = 0
while i<1:
        
    s = int(input('Enter the last four digits of the parton energy value you wish to study, here (copy paste from list above): '))
    #print(s)
    t = str(s)
    #print(t)
    Ec_str = str(E_c)
    Ed_str = str(E_d)
    Ee_str = str(E_e)
    Ef_str = str(E_f)
    
    str_list = [Ec_str,Ed_str,Ee_str,Ef_str]
    
    if t == Ec_str[-4:]:
        z_test.append(z_ca)
        print('\n This is the energy of the parton:  ', E_c)
        print(' This is the associated z: ', z_ca)
        print('This is the angle associated, theta: ', theta_c )
        theta_test.append(theta_c)
        print('\n Now that you know the value of z and theta, please proceed with an algorithm to calculate the kinematics of the parton')
        i = i+1
            
    if t == Ed_str[-4:]:
        z_test.append(z_da)
        print('\n This is the energy of the parton:  ', E_d)
        print(' This is the associated z: ', z_da)
        print('This is the angle associated, theta: ', theta_d )
        theta_test.append(theta_d)
        print('\n Now that you know the value of z and theta, please proceed with an algorithm to calculate the kinematics of the parton')
        i = i+1
            
    if t == Ee_str[-4:]:
        z_test.append(z_eb)
        print('\n This is the energy of the parton:  ', E_e)
        print(' This is the associated z', z_eb)
        print('This is the angle associated, theta: ', theta_e )
        theta_test.append(theta_e)
        print('\n Now that you know the value of z and theta, please proceed with an algorithm to calculate the kinematics of the parton')
        i = i+1
            
    if t == Ef_str[-4:]:
        z_test.append(z_fb)
        print('\n This is the energy of the parton:  ', E_f)
        print('This is the associated z', z_fb)
        print('This is the angle associated, theta :', theta_f )
        theta_test.append(theta_f)
        print('\n Now that you know the value of z and theta, please proceed to calculate whether or not this is an acceptable parton splitting event')
        i = i+1
            
    else: 
        for m in str_list:
            if t!= m:
                pass
        print('\n Please cross-check and re-enter the value you wish to observe. \n NOTE: If you have already received the calculated values for z and theta above, ignore the message above')
        i = i+0
   

print('\n z value , theta value : ', z_test,' , ',theta_test)         

q = []


for z in z_test:
    if 0.36788<z<1 :
        q.append(z)
        
for h in theta_test:
    if 0.5779<h<((np.pi)/2):
        q.append(h)
        
if len(q) == 2:
    print('Event accepted')
    
    
else:
    print('Event rejected ')
    
    
    

    
    
        

        
        