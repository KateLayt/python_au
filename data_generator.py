import random
import math
import sys

def write_to_file(filename, dictlst):
    file = open(filename,"w")
    for line in dictlst:
        file.write(line)
    file.close()

def generate_data_by_sin(n):
    x_data = [i*(math.pi/n) for i in range(n)]
    return [int(10 + 40*math.sin(x)) for x in x_data]

def generate_data_by_pow(n):
    return [2**x for x in range(n)]

def generate_data_by_line(n):
    k = random.randint(-2,2)
    return [30 + k*x for x in range(n)]

def generate_yeardata():
    working_moths = random.randint(0,12)
    functype = random.randint(1,3)
    if functype == 1:
        yeardata = generate_data_by_line(working_moths)
    if functype == 2:
        yeardata = generate_data_by_pow(working_moths)
    if functype == 3:
        yeardata = generate_data_by_sin(working_moths)
    while len(yeardata) != 12:
        yeardata.append(0)
    return yeardata

def generate_formated_lst_for_store(ID, data):
    data_lst = []
    for month in range(12):
        data_lst.append(["2020-{}".format(1 + month), ID, data[month]])
    return data_lst

def generate_formated_lst_for_worker(storeID, staffID, data):
    data_lst = []
    for month in range(12):
        data_lst.append(["2020-{}".format(1 + month), storeID, staffID, data[month]])
    return data_lst

def generate_full_data():
    full_data = []
    stores_num = random.randint(2,10)
    for i in range(stores_num):
        storeID = 100 + 100*i
        staff_num = random.randint(1,5)
        for j in range(staff_num):
            staffID = storeID + 1 + j
            staffdata = generate_formated_lst_for_worker(storeID, staffID, generate_yeardata())
            for monthdata in staffdata:
                full_data.append(monthdata)
    return full_data

def main():
    filename = sys.argv[1]
    write_to_file(filename, generate_full_data())

if __name__ == '__main__':
    main()