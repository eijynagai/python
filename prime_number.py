# program to check if a number is prime
# example: python prime_number.py 1313

def is_prime(num):
    return all([(num % i)  for i in range(2, int(num**0.5)+1)]) and num>1

if __name__ == '__main__':
    import sys
    print(is_prime(int(sys.argv[1])))