# Read CSV File and store data in the dictionary.Each key in the dictionary should be a string, as read from the CSV file. The value of that key will be a Python list. 
# import necessary modules
import csv
# opening the CSV file 
with open('Emissions.csv', mode ='r')as file: 
    
  # reading the CSV file 
  csvFile = csv.reader(file) 
  
  # displaying the contents of the CSV file 
  for lines in csvFile: 
        print(lines) 
