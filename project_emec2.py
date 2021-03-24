# -*- coding: utf-8 -*-
"""project_EMEC2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HHECErcr0T_eH6NKjm0gPYBNH-nYPB1d
"""

import pandas as pd
import numpy as np
import random

#Inputs
s = 25 #size of the grid
N = 100 #size of population
M = round(N * 0.007) #Number of infectious population
Et = 2 #Number of days staying exposed
It = 21 #Number of days staying infectious
Mt = 2 #Number of daily movements
D = 30 #Number of days
death_rate = 100
expose_rate = 3

#Initialization
S = N - M #Susceptible population
E = 0 #Exposed population
I = M #Number of infectious population 
R = 0 #Recovered population
P = S + E + I + R #Total population
Economy = 0 #Daily economic transaction
Cum_Economy = 0 #Total economic transaction

infectious_array[0][0]

dummy_array = np.zeros(shape=(P,8))
df = pd.DataFrame(dummy_array,columns=['x','y','Day','Susceptible','Exposed','Infectious','Recovered','GG'])
df = df.astype({'x':int,'y':int,'Day':int,'Susceptible':bool,'Exposed':int,'Infectious':int,'Recovered':bool,'GG':bool})
df['Susceptible'] = True
infectious_array = np.zeros(shape=(s+1,s+1), dtype=bool)
#Appending infectious population in 
dfupdate=df.sample(M)
dfupdate['Infectious'] = np.random.randint(1,It, size=len(dfupdate))
dfupdate['Susceptible'] = False
df.update(dfupdate)
update_list = dfupdate.index.tolist() 
#Dispersing people randomly among grid
df['x'] = np.random.randint(0,s, size=len(df))
df['y'] = np.random.randint(0,s, size=len(df))
df

KPIs = ['Active Cases','Newly Infected','Cured Cases','Death Cases','Reproduction Rate','Economy','Current Movement Restriction']
KPI_df = pd.DataFrame(columns=KPIs)
KPI_df = KPI_df.fillna(0)
KPI_df.loc[0,'Active Cases'] = I     
KPI_df.loc[0,'Newly Infected'] = df.loc[df['Infectious'] == 1].Infectious.count()
KPI_df.loc[0,'Cured Cases'] = 0
KPI_df.loc[0,'Death Cases'] = 0
KPI_df.loc[0,'Reproduction Rate'] = df.loc[df['Infectious'] == 1].Infectious.count()
KPI_df.loc[0,'Economy'] = Economy
KPI_df.loc[0,'Current Movement Restriction'] = 0

np.sum(infectious_array)

KPI_df

#['x','y','Day','Susceptible','Exposed','Infectious','Recovered','GG']
cured_num = 0
dead_num = 0
active_num = I

for day in range(D):    
    newly_infected = 0
    Economy = 0 #Economy per day
    for mt in range(Mt):
        for p in range(P):
            if df.loc[p,'GG'] == False: #If the person is not dead
                new_move_x = random.choice(range(-1,2))
                new_move_y = random.choice(range(-1,2))
                prev_x = df.loc[p,'x']
                prev_y = df.loc[p,'y']
                df.loc[p,'x'] = max(min(df.loc[p,'x']+new_move_x,s),0) #make valid movements in the grid
                df.loc[p,'y'] = max(min(df.loc[p,'y']+new_move_y,s),0)
                df.loc[p,'Day'] = day + 1 #updating the day counter                
                
                if (df.loc[p,'Infectious'] > 0) and (df.loc[p,'Recovered'] == False): #If a person is in infectious state
                    if df.loc[p,'Infectious'] - random.choice(range(0,7)) >= It: #If the infectious days are completed
                        if random.choice(range(0,death_rate)) > (death_rate-2): #If the person dies(with probability distribution 1:4)                           
                            df.loc[p,'Infectious'] = 0
                            df.loc[p,'GG'] = True #Kill the person
                            infectious_array[prev_x][prev_y] = False
                            print(f"Dead and + {infectious_array[df.loc[p,'x']][df.loc[p,'y']]}")
                            dead_num = dead_num+1   
                            active_num = active_num-1
                        else: #If the person survives
                            df.loc[p,'Infectious'] = 0
                            df.loc[p,'Recovered'] = True #Recover the person
                            infectious_array[prev_x][prev_y] = False
                            cured_num = cured_num+1
                            active_num = active_num-1
                    elif mt+1 == Mt:
                        df.loc[p,'Infectious'] = df.loc[p,'Infectious'] + 1 #Increase the infectious day counter
                        infectious_array[df.loc[p,'x']][df.loc[p,'y']] = True
                        infectious_array[prev_x][prev_y] = False
                elif (df.loc[p,'Exposed'] > 0) and (df.loc[p,'Infectious'] == 0): #If a person is in exposed state 
                    print(f"Exposed {infectious_array[prev_x][prev_y]}")
                    if (df.loc[p,'Exposed'] - random.choice(range(0,2))) >= Et: #If the person has reached the exposed day limit?  7
                        df.loc[p,'Exposed'] = 0
                        df.loc[p,'Infectious'] = 1 #Increase the infectious day counter, now the person is infectious
                        infectious_array[df.loc[p,'x']][df.loc[p,'y']] = True
                        infectious_array[prev_x][prev_y] = False
                        active_num = active_num+1
                        newly_infected = newly_infected+1
                        print(f"Became infected {infectious_array[df.loc[p,'x']][df.loc[p,'y']]}")
                    elif mt+1 == Mt:
                        df.loc[p,'Exposed'] = df.loc[p,'Exposed'] + 1 #Increase the exposed day counter
                        
                elif df.loc[p,'Susceptible'] == True: #If the person is in susceptible state 
                    if ((infectious_array[df.loc[p,'x']][df.loc[p,'y']])|(infectious_array[max(df.loc[p,'x']-1,0)][df.loc[p,'y']])|(infectious_array[max(df.loc[p,'x']-1,0)][max(df.loc[p,'y']-1,0)])|(infectious_array[df.loc[p,'x']][max(df.loc[p,'x']-1,0)])|(infectious_array[min(df.loc[p,'x']+1,s)][df.loc[p,'y']])|(infectious_array[df.loc[p,'x']][min(df.loc[p,'y']+1,s)])|(infectious_array[min(df.loc[p,'x']+1,s)][min(df.loc[p,'y']+1,s)])|(infectious_array[max(df.loc[p,'x']-1,0)][min(df.loc[p,'y']+1,s)])|(infectious_array[min(df.loc[p,'x']+1,s)][max(df.loc[p,'y']-1,0)])):
                    
                    
                        if random.choice(range(0,expose_rate)) > (expose_rate-2):
                            df.loc[p,'Exposed'] = 1
                            df.loc[p,'Susceptible'] = False
                if df.loc[p,'Infectious'] == 0:
                    Cum_Economy = Cum_Economy + round(random.uniform(0.8,1), 2)
                    Economy = Economy + round(random.uniform(0.8,1), 2)
                
    #Gathering the data
    KPI_df.loc[day + 1,'Active Cases'] = active_num
    KPI_df.loc[day + 1,'Newly Infected'] = newly_infected
    KPI_df.loc[day + 1,'Cured Cases'] = cured_num
    KPI_df.loc[day + 1,'Death Cases'] = dead_num
    KPI_df.loc[day + 1,'Reproduction Rate'] = active_num
    KPI_df.loc[day + 1,'Economy'] = Economy
    KPI_df.loc[day + 1,'Current Movement Restriction'] = 0

df

KPI_df

np.sum(infectious_array[15])

infectious_array[10]

df

