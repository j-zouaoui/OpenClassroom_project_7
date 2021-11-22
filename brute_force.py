
"""
this script aims to solve 0-1 knapsack problem using brute force solution.
this concept check all the possibilities and find the best solution.
it take data form csv file gathering action data as price and benifice rate
and return a bucket of optimal actions to buy in order to get the maximum
benifice
"""
import csv

#open the csv file and get requested data

with open('csv_file\data_file_for_test.csv','r', encoding="utf-8") as csv_file:
    data_file = csv.reader(csv_file)
    data = list(data_file)

    #delate the first item as it is the title of column
    del data[0]

CAPITAL = 500

def createbinairecombination(number):
    """
    this function aims to create a list of combination with a 2**n element
    :param n:
    :return: combinations list with binary value
    """
    possibility_number_list = list(range (2**number))
    tab_binaire = [bin(item)[2:] for item in possibility_number_list]
    combinaiasons = ['0'* (number-len(k))+ k for k in tab_binaire]
    return combinaiasons


def bestInvestementBucket(capital, data_list):
    """
    the function aims to select the best solution by running all
    the combination
    :param data_list:
    :return:
    """
    #create a list of different combination (2**n) using a bin function
    datalength= len(data_list)
    combinaiasons = createbinairecombination(datalength)

    #use binaire combination to calculate the cost of invest and keep
    # only the one less than 500 euro

    invest_combination_list = []
    for combination in combinaiasons:

        invest_capital = 0
        benifice = 0

        for i in range(datalength):
            if combination[i] == '1':
                invest_capital = invest_capital + float(data_list[i][1])
                benifice = benifice + float(data_list[i][1]) * float(data_list[i][2])/100

        if invest_capital <= capital:
            invest_combination_list.append((combination, round(benifice, 2)))

    #looking for the best combination that generate the maximum benifice
    max_benifice = 0
    best_combie = 0
    investement_cost  = 0
    for combination in invest_combination_list:
        if combination[1] > max_benifice:
            max_benifice = combination[1]
            best_combie = combination

    #translate binairy combination to action list
    action_to_buy = []
    for i in range(datalength):
        if best_combie[0][i] == '1':
            investement_cost = investement_cost + float(data_list[i][1])
            action_to_buy.append(data_list[i][0])

    #return the needed information as list of action to buy,
    # const of the investement and the estimate benifice
    best_investement_bucket = [ action_to_buy, investement_cost, max_benifice]
    return best_investement_bucket

print(bestInvestementBucket(CAPITAL, data))
