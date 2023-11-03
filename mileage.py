import sys

def main():
    mileage = 0
    try:
        if len(sys.argv) == 2:
            mileage = float(sys.argv[1])
        else:
            print("Program has to be excecuted as following: python3 estimage.py <mileage>")
            exit(1)
    except:
        print("Wrong arguments")
        exit(1)

    thetaZero = 0
    thetaOne = 0
    estimatePrice = thetaZero + (thetaOne * mileage)
    print("The estimation is :", estimatePrice)

main()