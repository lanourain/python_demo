import csv
with open('for_csv_demo_test.csv', 'r') as c:
    reader = csv.reader(c)
    csv_data = list(reader)
    print(csv_data)
    # '''
    # [['C', 'D', '', '', ''], ['C1', 'D11', '', '', '']]
    # '''
    print(csv_data[0][0])
    # C