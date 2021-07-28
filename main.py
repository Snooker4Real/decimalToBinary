# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def decimalToBinary(n):
    return bin(n).replace("0b", "")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(decimalToBinary(8))
    print(decimalToBinary(18))
    print(decimalToBinary(7))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
