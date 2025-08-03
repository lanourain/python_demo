import csv

# 推荐写法
# 以dict方式获取csv结果，自动跳过title行
with open('for_csv_demo_test.csv', 'r') as c:
    reader = csv.DictReader(c)
    # reader = csv.DictReader(c, ['A', 'B', 'C'])  没有标题也可以预设标题
    for row in reader:
        for column in row:
            print(row[column])

print('------------')
# 以list方式获取csv结果，适合没有title的csv，有title的需要跳过第一行
with open('for_csv_demo_test.csv', 'r') as c:
    reader = csv.reader(c)
    csv_data = list(reader)
    print(csv_data)
    # '''
    # [['C', 'D', '', '', ''], ['C1', 'D11', '', '', '']]
    # '''
    print(csv_data[0][0])
    # C
