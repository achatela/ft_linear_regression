import sys

def get_thetas():
    thetaZero = 0
    thetaOne = 0
    return (thetaZero, thetaOne)


def main():
    try:
        mileage = int(input("Enter the mileage: "))
    except:
        print("The mileage is not a number !")
        exit()
    if mileage < 0:
        print("The mileage cannot be negative !")
        exit()
    thetaZero, thetaOne = get_thetas()
    estimatePrice = thetaZero + (thetaOne * mileage)
    print("The estimation is :", estimatePrice)

main()