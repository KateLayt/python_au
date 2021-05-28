import matplotlib.pyplot as plt
import random
import math
import sys


def read_all_lines_from(filename):
    file = open(filename)
    result = file.readlines()
    file.close
    return result


def convert_filelines_to_dicts(filelines):
    dict_list = []
    for line in filelines:
        line = line.strip().lstrip('[').rstrip(']')
        linedata = line.split(', ')
        dict_list.append({'date': linedata[0], 'storeID': linedata[1], 'staffID': linedata[2], 'amount': linedata[3]})
    return dict_list


def sort_by_storeID(dictlist):
    return sorted(dictlist, key = lambda x: x['storeID'])


def get_dicts_for_store(storeID, dictlist):
    storedicts = []
    for dict in dictlist:
        if dict['storeID'] == str(storeID):
            storedicts.append(dict)
    return storedicts


def count_store_data(storelst):
    data = []
    for month in range (1,13):
        month_prod = 0
        for dict in storelst:
            if dict['date'] == '2020-{}'.format(month):
                month_prod += int(dict['amount'])
        data.append(month_prod)
    return data


def create_plot_for_store(storeID, dictlist):
    data = count_store_data(get_dicts_for_store(storeID, dictlist))
    months = [i for i in range(1,13)]
    plt.plot(months, data, color = 'blue', marker = 'o')
    plt.title(str(storeID))
    plt.show()


def main():
    filename = sys.argv[1]
    fulldata = sort_by_storeID(convert_filelines_to_dicts(read_all_lines_from(filename)))
    ID_lst = []
    for dict in fulldata:
        if not(dict['storeID'] in ID_lst):
            ID_lst.append(dict['storeID'])
    for storeID in ID_lst:
        create_plot_for_store(storeID, fulldata)


if __name__ == '__main__':
    main()

