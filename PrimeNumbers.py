class PrimeNumbers():
    def __init__(self):
        self.__p_numbers = []
        self.timeStamps = []

    def get_p_numbers(self):
        return self.__p_numbers

    #set methode 'fehlt' in aufgaben beschreibung
    def append_p_numbers(self, number_to_add):
        self.__p_numbers.append(number_to_add)


    def get_sum(self):
        s = 0
        for prime in self.__p_numbers:
            s = s+prime
        
        return s

    def get_average(self):
        s = self.get_sum()

        avg = s /len(self.__p_numbers)

        return avg
    
    #Zeitmessung
    def append_timestamp(self, ts):
        self.timeStamps.append(ts)

    def clalc_time_between_steps(self):
        differences = []
        for i in range(len(self.timeStamps)-1):
            diff = self.timeStamps[i + 1] - self.timeStamps[i]
            differences.append(diff)

        return differences