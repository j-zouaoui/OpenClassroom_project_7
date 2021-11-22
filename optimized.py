"""
this script aims to solve 0-1 knapsack problem using dynamic programming
it take data form csv file gathering action data as price and benifice rate
and return a bucket of optimal actions to buy in order to get the maximum
benifice
"""
# encoding="utf-8"

import csv


def getdata(url):
    """
    this function allows to read a csv file based on given url and remove the invalid data
    :param url: the link to the native csv file
    :return: sorted data
    """
    csv_file = open(url, 'r',  encoding="utf-8")
    data_file = csv.reader(csv_file)
    data = list(data_file)
    del(data[0])
    index_of_data_to_remove = []
    removed_data = []

    #pick up the index of data with negative price
    for i, action in enumerate(data):
        action_price = float(action[1])
        if action_price < 0:
            index_of_data_to_remove.append(i)

    #remove inconsistante data from the previous list
    for index in index_of_data_to_remove[::-1]:
        removed_data.append(data[index])
        del(data[index])

    print("removed data are:", removed_data)
    return data


def knapsack(W,data):
    """
    this function aims to solve the 0-1 knapsack problem using dynamic program
    :param W: the maxim capital. W is used as it is the one used for algorithm
    :param data:
    :return: best solution with the combination of the items
    """

    data_length = len(data)
    k = [[0 for x in range(W+1)] for x in range(data_length+1)]

    #Build  table[][] in buttom up manner
    for i in range(data_length + 1):
        action_price = float(data[i-1][1])
        benifice_rate = float(data[i-1][2])
        val = action_price * benifice_rate/100
        for w in range(W + 1):
            if i ==0 or w == 0 :
                k[i][w] = 0
            elif action_price <= w:
                k[i][w] = max(val + k[i-1][int(w-action_price)],  k[i-1][w] )
            else:
                k[i][w] = k[i-1][w]
    #part of code to get item involved in the optimal solution

    picked = []
    set_trace(k, data_length, W, data, picked)
    return k[data_length][W], picked


# find which item are picked
def set_trace(k, data_length, W, data, picked):
    """
    this function aims to keep track of the optimal solution items
    :param k:
    :param n:length of data
    :param W: maximum weigth for this cas it is the maximum capital
    :param data: action information extracted from csv file
    :param picked: sotred element of path
    :return: None
    """
    for i in range(data_length, 0, -1):
        if k[i][W] != k[i-1][W]:
            picked.append(data[i-1])
            set_trace(k, i-1, int(W-float(data[i-1][1])), data, picked)
            break


# Driver code
CAPITAL = 500
sorted_data = getdata("csv_file/dataset2_Python+P7.csv")
optimal_bucket = knapsack(CAPITAL, sorted_data)
print(round(float(optimal_bucket[0]),2))

invest_cost = 0
for item in optimal_bucket[1]:
    invest_cost += float(item[1])
print(round(invest_cost,2))
