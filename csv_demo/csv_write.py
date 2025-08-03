import csv
# 追加模式打开文件
with open('for_csv_demo_test.csv', 'a', newline='') as csvfile:
    # 创建 csv 写对象
    outputWriter = csv.writer(csvfile)
    # 通过写对象写入一行数据
    outputWriter.writerow(['a', 'b', 'c'])

