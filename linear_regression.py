import csv
import matplotlib.pyplot as plt

def estimatePrice(mileage, theta0, theta1):
    return float(theta0) + (float(theta1) * int(mileage))

def normalize(data):
    min_km = 9999999
    max_km = 0
    min_price = 9999999
    max_price = 0
    for item in data:
        if int(item['km']) > max_km:
            max_km = int(item['km'])
        if int(item['km']) < min_km:
            min_km = int(item['km'])
        if int(item['price']) > max_price:
            max_price = int(item['price'])
        if int(item['price']) < min_price:
            min_price = int(item['price'])
    print(min_km, max_km, min_price, max_price)
    tmp_data = []
    for item in data:
        tmp_km = (int(item['km']) - min_km) / (max_km - min_km)
        tmp_price = (int(item['price']) - min_price) / (max_price - min_price)
        tmp_data.append({'km': tmp_km, 'price': tmp_price})
    print(tmp_data)
    return tmp_data



def parse_csv():
    dataList = []
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dataList.append(dict(row))
    return dataList

def main():
    dataDictUnormalized = []
    dataDictUnormalized = parse_csv()

    dataDict = normalize(dataDictUnormalized)
    # theta0 = y-intercept = c
    # theta1 = slope = m
    m = 0.0
    c = 0.0

    L = 0.000000000001 # Learning rate
    epochs = 100
    prev_cost = float('inf')
    tol = 1e-6

    for r in range(epochs):
        c_tmp = 0.0
        m_tmp = 0.0
        # for item in dataDict:
            # c_tmp += (m * int(item['km']) + c) - int(item['price'])
            # m_tmp += ((m * int(item['km']) + c) - int(item['price'])) * int(item['km'])
        c_tmp = sum(estimatePrice(item['km'], c, m) - int(item['price']) for item in dataDict)
        m_tmp = sum((estimatePrice(item['km'], c, m) - int(item['price'])) * int(item['km']) for item in dataDict)
        c = c - L * (1/len(dataDict)) * c_tmp
        m = m - L * (1/len(dataDict)) * m_tmp
        # print(m, c)

        # current_cost = sum((float(estimatePrice(item['km'], c, m)) - int(item['price']))**2 for item in dataDict)

        # if abs(current_cost - prev_cost) < tol:
        #     break

        # prev_cost = current_cost

    print(c, m)
    print(estimatePrice(24000, c, m))
    # line = [str(int(estimatePrice(24000, c, m))), str(int(estimatePrice(240000, c, m)))]
    # priceLine = [str(24000), str(240000)]
    # dataDict.sort(key=lambda x: x['price'], reverse=True)
    # plt.figure(1)
    # plt.plot([data['km'] for data in dataDict], [data['price'] for data in dataDict], 'o')
    # plt.plot(priceLine, line, '-m')
    # plt.grid(True)
    # plt.show()
    # plt.close()

main()

