import urllib.request as urllib  # the lib that handles the url stuff
import os
import glob
import pandas as pd
import time
from urllib.error import HTTPError


'''
url = https://aineistot.vayla.fi/lam/rawdata/[year]/[ELY]/lamraw_[lam_id]_[yearshort]_[day_number].csv
year        = 2015 - 2020
ELY         = 01 [Uusimaa], 12 [Pohjois-Pohjanmaa] 
lam-id      = all
yearshort   = XX [15 - 20]
day_number  = 1 - 365 [Mukana hyppyvuosia]
'''

start = time.time()

# LAM ID's in Pohjois Pohjanmaa Area
lam_id_list_ppohjanmaa2020 =  [1052, 1101, 1103, 1104, 1105, 1121, 1123, 1124, 1201, 1202, 1203, 1204, 1205, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229,
                    1230, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1243, 1244, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256,
                    1257, 1301, 1302, 1303, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329]
                    
lam_id_list_ppohjanmaa2019 =  [1052, 1101, 1103, 1104, 1105, 1121, 1123, 1124, 1202, 1203, 1204, 1205, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228,
                    1230, 1232, 1233, 1234, 1235, 1236, 1238, 1239, 1243, 1244, 1246, 1247, 1248, 1249, 1252, 1253, 1254, 1255, 1256,
                    1257, 1301, 1302, 1303, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329]

# LAM ID's in Uusimaa Area                   
lam_id_list_uusimaa2019 = [1, 3, 4, 5, 6, 7, 8, 9, 11, 98, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 114, 115, 117, 119, 121,
                        122, 123, 124, 125, 126, 127, 129, 130, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 150, 151, 
                        152, 153, 154, 155, 156, 158, 159, 160, 162, 163, 164, 165, 167, 168, 169, 172, 175, 176, 177, 178, 179, 182, 183, 184, 185,
                        186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 403, 405, 407, 408, 424, 426, 428, 429, 430, 432, 437, 441, 
                        442, 446, 447, 461, 465, 466, 623, 628, 998]
                        

#change year value, depending what data loading
name_of_the_file= "lam_data_uusimaa_20.csv" 


f = open(name_of_the_file, "w")  # create a file new file if the file does not exists, deletes old file if it exists
f.close()

f = open(name_of_the_file, "a+")  # open the empty file in append mode
f.write("lam_point_id;year;day;hour;minute;second;100th_second;length;lane;direction;category;speed;faulty;total_time;interval;queue_start\n")
counter = 0

for day in range(75,121): #how many days has elapsed this year

    for number in lam_id_list_uusimaa2019: # Goes through all LAM points
        # used to catch errors, when file is mislabeled
        try:            
            target_url = "https://aineistot.vayla.fi/lam/rawdata/2020/01/lamraw_{}_20_{}.csv".format(number, day)
            data = urllib.urlopen(target_url)   # it's a file like object and works just like a file
            
        except HTTPError as err:
            print("Error: {}, LAM point: {}, Day: {}".format(err, number, day)) # print missing/mislabeled file
            pass
            
        for line in data:                   # files are iterable
            f.write(line.decode("utf-8"))   # changing value from binary to string
            counter += 1                    # counts how many datapoints are saved
            
            
            # Used to follow progress
            if counter == 1000:
                print("1K")
            elif counter == 10000:
                print("10K")
            elif counter == 50000:
                print("50K")
            elif counter == 100000:
                print("100K")
            elif counter == 1000000:
                print("1M")
            elif counter == 5000000:
                print("5M")
            elif counter == 10000000:
                print("10M")
            elif counter == 20000000:
                print("20M")
            elif counter == 30000000:
                print("30M")
            elif counter == 40000000:
                print("40M")
            elif counter == 50000000:
                print("50M")  
            elif counter == 60000000:
                print("60M")
            elif counter == 70000000:
                print("70M")
            elif counter == 80000000:
                print("80M")
            elif counter == 90000000:
                print("90M")
            elif counter == 100000000:
                print("100M")
            elif counter == 110000000:
                print("110M")
            elif counter == 120000000:
                print("120M")
            
            
f.close()

end = time.time()
print("\nLines added to file: {}".format(counter))
print("Run time: {0:.2f} seconds".format(end - start))