import csv

def estimatePrice(mileage, theta0, theta1):
    return float(theta0) + (float(theta1) * float(mileage))

def parse_csv():
   dataList = []
   with open('data.csv', newline='') as csvfile:
       reader = csv.DictReader(csvfile)
       for row in reader:
           dataList.append(dict(row))
   return dataList

def main():
    dataDict = []
    dataDict = parse_csv()

    # theta0 = y-intercept = c
    # theta1 = slope = m
    m = 0
    c = 0

    L = 0.0000000001 # Learning rate
    epochs = 100

    for r in range(epochs):
        c_tmp = sum(estimatePrice(item['km'], c, m) - float(item['price']) for item in dataDict)
        m_tmp = sum((estimatePrice(item['km'], c, m) - float(item['price'])) * float(item['km']) for item in dataDict)
        c = c - L * (1/len(dataDict)) * c_tmp
        m = m - L * (1/len(dataDict)) * m_tmp
        # print(m, c)

    print(estimatePrice(24000, c, m))

main()

