import time
from PrimeNumbers import PrimeNumbers

class SieveOfEratosthenes(PrimeNumbers):
    def __init__(self):
        super().__init__()
        self._to_number: int
        

    def set_to_number(self, number: int):
        self._to_number = number
        self.__prozess()

    def __prozess(self):
        sieve = [True] * (self._to_number +1)

        curr_milli = round(time.time() * 1000)
        super().append_timestamp(curr_milli)
        

        sieve[0] = False
        sieve[1] = False

        for i in range(0, self._to_number+1):
            if sieve[i]:
                super().append_p_numbers(i)

                for n in range(2, self._to_number+1):
                    prod = n * i
                    if prod > self._to_number:
                        break
                    sieve[prod] = False

            if i % 100 == 0 and i != 0:
                curr_milli = round(time.time()* 1000)
                super().append_timestamp(curr_milli)



