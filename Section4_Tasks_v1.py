# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:35:39 2019

@author: ANWESHA
"""


import random
import numpy as np
import matplotlib.pyplot as plt

dummy_list = [] #empty list to include count for number of acceptable events

def parton_generator():
    
    #LEVEL 1 - includes processes for generation of two partons from a single parent parton of energy 1 relative to that is offspring partons 
    
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
    names = ['Parent Parton','A','B','C','D','E','F']
    
    
    plt.scatter(x_coords, Energies, linewidth = 0.1)
    
    for w, txt in enumerate(names):
        plt.annotate(txt,(x_coords[w],Energies[w]))
    
    plt.legend()
    plt.show()
    
    #print(E_c+E_d+E_e+E_f)
    
    
    #OUTPUT 4-MOMENTUM VECTOR CALCULATION:
    
    Gen3_Energies = [E_c,E_d,E_e,E_f]
    
    l1 = [] #E and theta values corresponding to particle c if event accepted
    l2 = [] #E and theta values corresponding to particle d if event accepted
    l3 = [] #E and theta values corresponding to particle e if event accepted
    l4 = [] #E and theta values corresponding to particle f if event accepted
    
    
    
    for i in Gen3_Energies:
        
        if i == E_c:
            if 0.36788<z_ca<1:
                l1.append(z_ca)   
            if 0.5779<theta_c<(np.pi/2):
                l1.append(theta_c)
                
        if i == E_d:
            if 0.36788<z_da<1:
                l2.append(z_da)   
            if 0.5779<theta_d<(np.pi/2):
                l2.append(theta_d)
                
        if i == E_e:
            if 0.36788<z_eb<1:
                l3.append(z_eb)   
            if 0.5779<theta_e<(np.pi/2):
                l3.append(theta_e)
                
        if i == E_f:
            if 0.36788<z_fb<1:
                l4.append(z_fb)   
            if 0.5779<theta_f<(np.pi/2):
                l4.append(theta_f)
      
    
      
    if len(l1) == 2:
        print('\nz_ca , theta_c:', z_ca,'  ,  ', theta_c)
        print('2nd generation parent parton - parton A - energy: ',E_a)
        print('Event for parton c accepted')
        dummy_list.append('success')
        
    if len(l2) == 2:
        print('\nz_da , theta_d:', z_da,'  ,  ', theta_d)
        print('2nd generation parent parton - parton A - energy: ',E_a)
        print('Event for parton d accepted')
        dummy_list.append('success')
        
    if len(l3) == 2:
        print('\nz_eb , theta_e:', z_eb,'  ,  ', theta_e)
        print('2nd generation parent parton - parton B - energy: ',E_b)
        print('Event for parton e accepted')
        dummy_list.append('success')
        
    if len(l4) == 2:
        print('\nz_fb , theta_f:', z_fb,'  ,  ', theta_f)
        print('2nd generation parent parton - parton B - energy: ',E_b)
        print('Event for parton f accepted')
        dummy_list.append('success')
        

n = 10 # n = number of event sets(i.e tree diagrams) to be generated. Note that each set has 4 possible final, 3rd generation partons
#Alter n as per the number of events you wish to generate. n must be a whole number
for j in range(n):
    num_partons_generated = n*4
    parton_generator()
    print('\nEVENT_SET ', j+1, 'COMPLETE')
    print('\n')
    
Tot_3rdGenEvents_observed = n*4 
Tot_Accepted_Events = len(dummy_list)
Tot_Rejected = (n*4) - len(dummy_list)
Percent_Accepted = (Tot_Accepted_Events/Tot_3rdGenEvents_observed)*100

print('\n')
print('\n')


print('\n SUMMARY OF ALL EVENTS:')  

print('\nTotal number of events observed and calculated: ', Tot_3rdGenEvents_observed)
print('Number of accepted events: ', len(dummy_list))
print('Number of rejected events: ', Tot_Rejected)

print('\n Percentage Accepted: ', Percent_Accepted,'%')
#GENERATE PIE CHART:

labels = 'Accepted', 'Rejected'
sizes = [Tot_Accepted_Events,Tot_Rejected]
color = ['pink','blue']

plt.pie(sizes,labels=labels,colors=color)

plt.axis('equal')
plt.show()
    
    
    
     
            

            
            

    
    
    
    

    
    
        

        
        