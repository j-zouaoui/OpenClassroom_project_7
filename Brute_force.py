import csv

#open the csv file and get requested data
csv_file = open('csv_file\data_file_for_test.csv','r')
data_file = csv.reader(csv_file)
data = list(data_file)

#delate the first item as it is the title of column
del data[0]

def bestInvestementBucket(data_list):
    #create a list of different combination (2**n) using a bin function
    n = len(data_list)
    possibility_number_list = [i for i in range (2**n)]

    tab_binaire = [bin(item)[2:] for item in possibility_number_list]
    combinaiasons = ['0'* (n-len(k))+ k for k in tab_binaire]

    #use binaire combination to calculate the cost of invest and keep only the one less than 500 euro
    capital = 500
    invest_combination_list = []
    for combination in combinaiasons:

        invest_capital = 0
        benifice = 0
        action_bucket = []

        for i in range(n):
            if combination[i] == '1':
                invest_capital = invest_capital + float(data_list[i][1])
                benifice = benifice + float(data_list[i][1]) * float(data_list[i][2])/100

        if invest_capital <= capital:
            invest_combination_list.append((combination, round(benifice, 2)))

    #looking for the best combination that generate the maximum benifice
    max_benifice = 0
    best_combie = 0
    investement_cost  = 0
    for i in range(len(invest_combination_list)):
        if invest_combination_list[i][1] > max_benifice:
            max_benifice = invest_combination_list[i][1]
            best_combie = invest_combination_list[i]

    #translate binairy combination to action list
    action_to_buy = []
    for i in range(n):
        if best_combie[0][i] == '1':
            investement_cost = investement_cost + float(data_list[i][1])
            action_to_buy.append(data_list[i][0])

    #return the needed information as list of action to buy, const of the investement and the estimate benifice
    best_investement_bucket = [ action_to_buy, investement_cost, max_benifice]
    return best_investement_bucket

print(bestInvestementBucket(data))









