import urllib.request as urllib  # the lib that handles the url stuff
import os
import glob
import pandas as pd
import time
from urllib.error import HTTPError
from LAM_points import *
"""
getData version 2.1 - Final release

Release Notes: 
1.  Changed code structure to format data from all LAM points from one day to same file. 
    Smaller files brought time savings of 30% while downloading and 1000% while prosessing in cluster
2.  Error detection prints errors now and tells what file it was asking for

3.  Added code to save loaded data to a folder.
"""

'''
url = https://aineistot.vayla.fi/lam/rawdata/[year]/[ELY]/lamraw_[lam_id]_[yearshort]_[day_number].csv
year        = 2015 - 2020
ELY         = 01 [Uusimaa], 12 [Pohjois-Pohjanmaa] 
lam-id      = all
yearshort   = XX [15 - 20]
day_number  = 1 - 365 [Mukana hyppyvuosia]
'''

start = time.time()
                        
#-------------------------------------------------------------------------------

#Name folder here
name_of_the_file= "lam_data_uusimaa_20"
areaCode = "01"

#-------------------------------------------------------------------------------

path = os.getcwd()
print ("The current working directory is %s" % path) 
final_directory = os.path.join(path, r'{}'.format(name_of_the_file)) 

#Creates Folder
try:
    os.makedirs(final_directory)
except OSError:
    print ("\nCreation of the directory %s failed" % path)
else:
    print ("\nSuccessfully created the directory %s " % path)  

#Moves to new folder
os.chdir(final_directory)
path = os.getcwd()
print("The current working directory is %s\n" % path) 
counter = 0

for day in range(75,121): #how many days has elapsed this year
    
    
    name_of_the_file= "LAM_data_day{}.csv".format(day)
    f = open(name_of_the_file, "w")  # create a file new file if the file does not exists, deletes old file if it exists
    f.close()

    f = open(name_of_the_file, "a+")  # open the empty file in append mode
    f.write("lam_point_id;year;day;hour;minute;second;100th_second;length;lane;direction;category;speed;faulty;total_time;interval;queue_start\n")
    
    
    for number in lam_id_list_uusimaa2018: # Goes through all LAM points
    
        # used to catch errors, when file is mislabeled
        try:            
            target_url = "https://aineistot.vayla.fi/lam/rawdata/2018/01/lamraw_{}_18_{}.csv".format(number, day) #get data
            data = urllib.urlopen(target_url)   # it's a file like object and works just like a file
            
        except HTTPError as err:
                print("Error: {}, LAM point: {}, Day: {}".format(err, number, day)) # print missing/mislabeled file
                pass
                
        for line in data:                   # files are iterable
            f.write(line.decode("utf-8"))   # changing value from binary to string
            

           
end = time.time()
print("Run time: {0:.2f} seconds".format(end - start))