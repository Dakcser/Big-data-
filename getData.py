import urllib.request as urllib  # the lib that handles the url stuff
import os
import glob
import pandas as pd
import time


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
lam_id_list_ppohjanmaa =  [1052, 1101, 1103, 1104, 1105, 1121, 1123, 1124, 1201, 1202, 1203, 1204, 1205, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229,
                    1230, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1243, 1244, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1246,
                    1257, 1301, 1302, 1303, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329]

name_of_the_file="lam_data_ppohjanmaa_1.csv"
f = open(name_of_the_file, "w")  # create a file new file if the file does not exists, deletes old file if it exists
f.close()

f = open(name_of_the_file, "a+")  # open the empty file in append mode
f.write("lam_point_id;year;day;hour;minute;second;100th_second;length;lane;direction;category;speed;faulty;total_time;interval;queue_start\n")
counter = 0

for day in range(1,124): #how many days has elapsed this year

    for number in lam_id_list_ppohjanmaa: # Goes through all LAM points
        target_url = "https://aineistot.vayla.fi/lam/rawdata/2020/12/lamraw_{}_20_{}.csv".format(number, day) #get data
        
        data = urllib.urlopen(target_url)   # it's a file like object and works just like a file
        for line in data:                   # files are iterable
            f.write(line.decode("utf-8"))   # changing value from binary to string
            counter += 1                    # counts how many datapoints are saved
            
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


'''
#Combine all csv files    
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
'''

end = time.time()
print("\nLines added to file: {}".format(counter))
print("Run time: {0:.2f} seconds".format(end - start))
