# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 22:41:58 2019

@author: PeerapongE
"""
# 

# United States Environmental Protection Agency (EPA) --> aqi.ALGO_EPA
# China Ministry of Environmental Protection (MEP) --> aqi.ALGO_MEP
import aqi

myaqi = int(aqi.to_iaqi(aqi.POLLUTANT_PM25,'12', aqi.ALGO_EPA))

print(myaqi)