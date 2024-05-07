import pandas as pd
import math
import csv
#Possible Electrical Climate Controls
# - Electric Resistance Heating System
# - Heat Pump Heating System
# - Cooling System

#Possible Fossil Fuel Heating
# - Natural Gas Heating System
# - Oil Heating System
# - Propane Heating System

#Values From https://energizect.com/sites/default/files/documents/Final%202022%20PSD%20FILED%20110122.pdf

#Electrical Climate Systems
def calcResistanceHeatingKWH(A):
	return 0.4561*A

def calcHeatPumpHeatingKWH(A):
	return 0.1425*A

def calcHVACCoolingKWH(A):
	return 0.0234*A

#Fossil Fuel Heating Systems
def calcNaturalGasHeatingCCF(A):
	return 0.0178*A

def calcOilHeatingGallons(A):
	return 0.0134*A

def calcPropaneHeatingGallons(A):
	return 0.0201*A
	
def ccfToMMBtu(ccf):
	return (ccf*100*1027)/1000000
	
def calcNumThermostats(A):
	AreaPer = A**2 / 2500**2
	numThermostats = math.ceil(A / AreaPer)
	return numThermostats
	
def CO2TonsNaturalGas(GasMMbtu):
	return GasMMbtu * 0.1 * 14.43 * 44 * 0.001

def calcSavings(CoolingKWH, HeatingUnitsSaved, KWH_Rate, HeatingUnitRate, NumThermostats):
	coolingSavings = CoolingKWH * KWH_Rate
	heatingSavings = HeatingUnitsSaved * HeatingUnitRate
	totalSavings = coolingSavings + heatingSavings
	Cost = NumThermostats * (166.57-85)
	PaybackPeriod = Cost / totalSavings
	return [coolingSavings, heatingSavings, totalSavings, Cost, PaybackPeriod]
	

heatingSystem = int(input("Please Select The Heating System Present:\n1. Resistance Heating Unit\n2. Heat Pump\n3. Natural Gas Heater\n4. Oil Heater\n5. Propane Heater\n6. No Heater\n:"))

A = (float(input("Please enter the Area of the facility in ft^2: ")))


CoolingKWH = calcHVACCoolingKWH(A)

savedKWH = CoolingKWH
SavedUnits = 0

KWHRate = float(input("Please Enter the Rate per KWH in USD: $"))

if heatingSystem == 1:
	heatingUnit = 'KWH'
	SavedUnits = calcResistanceHeatingKWH(A)
	savedKWH += SavedUnits
	heatingRate = KWHRate

if heatingSystem == 2:
	heatingUnit = 'KWH'
	SavedUnits = calcHeatPumpHeatingKWH(A)
	savedKWH += SavedUnits
	heatingRate = KWHRate

if heatingSystem == 3:
	heatingUnit = 'CCF'
	SavedUnits = calcNaturalGasHeatingCCF(A)
	heatingRate = float(input("Please Enter the rate per MMBtu in USD: $"))

if heatingSystem == 4:
	heatingUnit = 'Gallons'
	SavedUnits = calcOilHeatingGallons(A)
	heatingRate = float(input("Please Enter the Rate per Gallon in USD: $"))

if heatingSystem == 5:
	heatingUnit = 'Gallons'
	SavedUnits = calcPropaneHeatingGallons(A)
	heatingRate = float(input("Please Enter the Rate per Gallon in USD: $"))

print(str(CoolingKWH) + " kWH")
print(str(SavedUnits) + " " + heatingUnit)
print(str(savedKWH) + " kWH")

titles = ['Cooling Electricity Savings (kWH)', 'Heating Savings', 'Cooling Expense Savings ($)', 'Heating Expense Savings ($)', 'Total Savings ($)', 'Implementation Cost ($)', 'Payback Period (years)']

output = [CoolingKWH, ccfToMMBtu(SavedUnits)]
for i in calcSavings(CoolingKWH, ccfToMMBtu(SavedUnits), KWHRate, heatingRate, calcNumThermostats(A)):
	output.append(i)

dictionary = {}

for i in range(len(titles)):
	dictionary[titles[i]] = output[i]

print(dictionary)

with open('output.csv', 'w') as f:
    for key in dictionary.keys():
        f.write("%s,%s\n"%(key,dictionary[key]))
