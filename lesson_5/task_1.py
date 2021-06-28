prime_number = int(input("Enter a prime number and check whether it prime or not: "))


def is_prime(prime_number):
    if prime_number >= 0 and prime_number <= 1000:
        for number in range(2, prime_number):
            if prime_number % number != 0:
                print("True")
                break
            else:
                print("False")
            return prime_number
    else:
        print("False")


is_prime(prime_number)
