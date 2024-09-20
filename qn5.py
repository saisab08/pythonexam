#5 write a program that will write your name , age into a text file (5)

import csv 

data =[
    {"name": "Shaishab", "age": 16,"roll_no":19},
    
]
def my_info():
    with open('txtfile.csv','a') as file:
        Head =["name","age"]
        writer=csv.DictWriter(file,fieldnames=Head)
        writer.writerows(data)
my_info()

def get_function():
    with open('txtfile.csv','r') as file:
        reader=csv.DictReader(file,delimiter=',')
        for row in reader:
            print(row)
get_function()

