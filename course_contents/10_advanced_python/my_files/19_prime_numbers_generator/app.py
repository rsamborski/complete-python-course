"""
Take a look at the code in the problem description where we test if a number is prime.
Refactor the code and put it into the function below to turn the prime_generator() function into a generator.

Implement your generator so that others can get a prime number generator like this:

g = prime_generator(100)    # g can generate prime numbers under 100
next(g) # get next prime like this

Reminder: you don't need to change the function name nor the argument
"""


def prime_generator(bound):
    for n in range(2, bound):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n


class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes
        self.n = 2

    def __next__(self):
        while self.n < self.stop:
            n = self.n
            self.n += 1

            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                return n

        raise StopIteration()


pg = PrimeGenerator(20)

for i in range(5):
    print(next(pg))
