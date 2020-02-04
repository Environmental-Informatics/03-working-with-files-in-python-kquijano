#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Karoll Quijano - kquijano

ABE 651 - Environmental Informatics
2020/02/03

Think Python - Chapter 8-14
Assignment 03 - Using Files and Simple Data Structures with Python
"""



''' 1. Open data file 
    Read txt file from a simulated Raccoon behavior model'''


file = open('2008Male00006.txt', 'r')

flines = file.readlines()                   # Read all lines from file. List of strings
headers = flines[0].strip().split(',')      # list of headers (only)
note = flines[15].strip()                   # Note: George's status             
     
data = [0]*(len(flines)-2)                  # Empty list 



''' 3. Convert column of numbers into lists of the correct number type '''


for line in range(len(flines[1:15])):       # Stores values in empty list with different data type
    data[line] = flines[1:15][line].strip().split(",")
    
    data[line][3] = int(data[line][3])
    data[line][4:6] = map(float,data[line][4:6])
    data[line][8:15] = map(float,data[line][8:15])

datat = list(map(list,zip(*data)))          # Transpose list   
    


''' 2. Store data from file in a Dictionary
    Key terms = headers 
    values = data '''
    
    
dic = dict()                                # Create Dictionary
                
for i in range(len(headers)):               # Adds values from data to key from header 
    for i in range (len(datat)):
        dic[headers[i]] = datat[i]
    
dic ['Status'] = note                       # Add note for George's status   



''' 4. Writing funtions '''


from math import sqrt


def cmpt_mean(lst):
    ''' Computes average of a list '''
    mean = sum(lst)/len(lst)
    return mean

          

def cmpt_sum(lst):
    ''' Computes cumulative sum of a list '''
    cum_sum = sum(lst)
    return round(cum_sum, 2)



def dist(x1,y1,x2,y2):
    ''' Computes the distance between two points (x1,y1) and (x2,y2) '''
    dist = sqrt((x2-x1)**2+(y2-y1)**2)
    return round(dist, 2)


def cmpt_dist(X, Y, dic):
    ''' Computes the distance between subsequent set of coordinates from two lists, X and Y 
        returns list of distances added to dictionary
        initial distance = 0 
        
        X = List of x coordinates
        Y = List of Y coordinates
        dic = Dictionary to add list of distances '''
            
    lt = []                                 # Creates empty list
    distance = 0                            # Initial distance = 0
    lt.append(distance)
    
    for i in range(len(X)-1):               # Uses dist function to calculate distances
        distance = dist(X[i], Y[i], X[i+1], Y[i+1])
        lt.append(distance)
    
    dic['Distance'] = lt                    # Adds list of distances to Dictionary


    
''' 5. Using functions '''


cmpt_dist(dic[' X'], dic[' Y'], dic)          # Add George's movement to the data dictionary.
avg_energy = cmpt_mean(dic['Energy Level']) # Compute George's average energy level
avg_x = cmpt_mean(dic[' X'])                # Compute George's average location (average X and Y).
avg_y = cmpt_mean(dic[' Y'])
t_dist = cmpt_sum(dic['Distance'])          # Compute the total distance George moved in his life.



''' 6. Creating file '''


file_out = open("Georges_life.txt", 'w')                            # Create a new output file
                                            
file_out.write ('Raccoon name: %s \n' %dic['Status'][:6] )             # Writing header 
file_out.write ('Average location: X %f, Y %f \n' %(avg_x, avg_y))
file_out.write ('Distance traveled: %.2f \n' %t_dist)
file_out.write ('Average energy level: %.2f  \n' % avg_energy)
file_out.write ('Raccoon end state: %s \n\n' % dic['Status'])         # Adding blank line

# Writing select content 
header = ['Date', 'X', 'Y', 'Asleep Flag', 'Behavior Mode', 'Distance Traveled']
file_out.write ('%s \t %s \t %s \t %s \t %s \t %s \n'%(header[0], header[1], header[2], header[3], header[4], header[5]))

for i in range(len(dic['Year'])):
    file_out.write ('%s \t %f \t %f \t %s \t %s \t %.2f \n'%(dic['Day'][i],dic[' X'][i],dic[' Y'][i],dic[' Asleep'][i],dic['Behavior Mode'][i],dic['Distance'][i]))

file_out.close()

