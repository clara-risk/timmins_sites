#coding: utf-8

"""
Summary
-------
Produce geojson files for cumulative defoliation - Timmins 

References 
----------

"""
#import
import geopandas as gpd
import numpy as np
import pyproj
import matplotlib.pyplot as plt
import warnings
import os,sys,time
import math,statistics
import pandas as pd
warnings.filterwarnings("ignore")
from shapely.ops import unary_union
from shapely.geometry import Polygon
from matplotlib.lines import Line2D
import time
##
##
def separate(shp,year):
    shp2 = shp[shp['EVENT_YEAR'] == year]
    print('Completed getting year %s'%(year)) 

    return shp2

def intersect(year1,year2):
    only_s = gpd.clip(year1,year2)
    print('Completed intersection')
    return only_s

def export_json(df,fp):
    print(fp)
    df.to_file(driver='GeoJSON',filename='M1_'+str(fp)+'.geojson')
##
##shp = gpd.read_file('mod_sev_2009_plus.geojson')
##df_hold = {}  
##for year in list(range(2009,2021+1)):
##    
##    year_sep = separate(shp,year)
##    df_hold[year] = year_sep
##    
##counter1 = list(range(0,len(df_hold.keys())))
##counter2 = list(range(1,len(df_hold.keys())+1))
##counter3 = list(range(2,len(df_hold.keys())+2))
##years = list(range(2009,2021+1))
##
##intersected = {} 
##for count1,count2,count3 in zip(counter1,counter2,counter3):
##    if count3 <= max(counter1) and years[count3] <= 2021: 
##        year1 = years[count1]
##        year2 = years[count2]
##        year3 = years[count3]
##        print('processing %s and %s and %s'%(year1,year2,year3))
##
##        df1 = df_hold[year1]
##        df2 = df_hold[year2]
##        df3 = df_hold[year3]
##
##        if len(df2) > 0: 
##
##            only_s = gpd.clip(df2,df1)
##            only_s2 = gpd.clip(only_s,df3)
##            intersected[year3] = only_s2
##
####not_overlapping = {}
####for key,geo_object in intersected.items():
####    print('making sure no overlap for %s'%(key))
####    for overlapper in intersected.values(): 
####        keep_track = [geo_object]
####        if not overlapper['geometry'].equals(geo_object['geometry']): 
####            df_tracked = keep_track[0]
####            cut_object = df_tracked.symmetric_difference(unary_union(overlapper.dissolve().geometry))
####            cut2 =gpd.GeoDataFrame(geometry=cut_object,crs='EPSG:4326')
####            print(cut2)
####            fig,ax = plt.subplots(figsize=(15, 15))
####            cut2.plot(ax=ax,facecolor='None',edgecolor='k')
####            plt.xlabel('Longitude')
####            plt.ylabel('Latitude')
####            plt.show()
####            
####            cut2['EVENT_YEAR'] = key
####            keep_track[0] = cut2
####
####    not_overlapping[key] = keep_track[0]
##
##
####for name,file in not_overlapping.items():
##for name,file in intersected.items():
##
##    print(file)
##    try: 
##        export_json(file,name)
##    except:
##        pass 
    
    
shp = gpd.read_file('timmins_allsites_upd.geojson')
for year in list(range(2009,2021+1)):
    
    year_sep = separate(shp,year)
    print(year_sep)
    try: 
        export_json(year_sep,year)
    except:
        pass 

    

    
        
