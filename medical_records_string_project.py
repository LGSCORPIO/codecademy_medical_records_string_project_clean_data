#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:58:39 2021

@author: lilygoodyersait
"""

medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
##turn # into $
print(medical_data)
updated_medical_data=medical_data.replace("#","$")
print (updated_medical_data)

###count number of patients via number of $
num_records=0
for i in updated_medical_data:
  if i == "$":
    num_records+=1
print("There are {} medical records in the data".format(num_records))

###split list into sublists per patient
medical_data_split=updated_medical_data.split(";")
print(medical_data_split)

##split patient lists into name, bmi and insurance 
medical_records=[]
for i in medical_data_split:
  medical_records.append(i.split(","))
  print(medical_records)
###clean up whitespace
medical_records_clean=[]
for i in medical_records:
  record_clean=[]
  for item in i:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

print(medical_records_clean)

### print names in upper case
for i in medical_records_clean:
  i[0]=i[0].upper()
  print(i[0])
### store name, age, BMI and insurance in separate lists

names=[]
ages=[]
bmis=[]
insurance_costs=[]

for i in medical_records_clean:
  names.append(i[0])
  ages.append(i[1])
  bmis.append(i[2])
  insurance_costs.append(i[3])
print (names)
print(ages)
print(bmis)
print(insurance_costs)

###bmi analysis
total_bmi=0
for i in bmis:
  total_bmi+=float(i)
print(total_bmi)

average_bmi=total_bmi/len(bmis)
print("Average BMI: {}".format(average_bmi))

###insurance cost analysis
insurance_costs_2=[]
for i in insurance_costs:
    insurance_costs_2.append(i[1:])
print(insurance_costs_2)

cost_total=0
for i in insurance_costs_2:
  cost_total+=float(i)
print(cost_total)

average_cost=cost_total/len(insurance_costs_2)

print(average_cost)

### print out sentence with details for each patient

for i in range(len(names)-1):
  print( "{name} is {age} years old with a BMI of {bmi} and an insurance cost of {insurance_cost}".format(name=names[i], age=ages[i], bmi=bmis[i], insurance_cost=insurance_costs[i]))