
from PrimeNumbers import PrimeNumbers
import time


class Primal(PrimeNumbers):
    def __init__(self):
        super().__init__()
        self._to_number: int

    def set_to_number(self, number: int):
        self._to_number = number

        self.__prozess()

    def __prozess(self):
        #(n−1)! ≡ −1(mod n)

        curr_milli = round(time.time() * 1000)
        super().append_timestamp(curr_milli)

        for n in range(2, self._to_number+1):
            if (self.__factorial(n-1) +1 ) % n == 0:
                super().append_p_numbers(n)

            if n % 100 == 0:
                curr_milli = round(time.time()* 1000)
                super().append_timestamp(curr_milli)



    def __factorial(self, num):
        factorial = 1

        for i in range(1, num+1):
            factorial = factorial * i

        return factorial
    

