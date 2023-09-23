"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Number can't be smaller than 1")
    list = [2]
    cnt = 1
    curNo = 2
    while cnt < number_of_primes:
        curNo += 1
        prime = True
        for i in range(2,curNo):
            if curNo % i == 0:
                prime = False
        if prime:
            cnt+=1
            list.append(curNo)
    return list