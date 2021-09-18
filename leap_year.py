# Program to return if a year is leap or not

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == '__main__':
    import sys
    print(is_leap(int(sys.argv[1])))