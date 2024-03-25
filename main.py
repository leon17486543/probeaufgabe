from Primal import Primal
from SieveOfEratosthenes import SieveOfEratosthenes


#Teilaufgabe a
max_number = 100

obj_primnal = Primal()
obj_primnal.set_to_number(max_number)
p1 = obj_primnal.get_p_numbers()
s1 = obj_primnal.get_sum()
avg1 = obj_primnal.get_average()

obj_sieve = SieveOfEratosthenes()
obj_sieve.set_to_number(max_number)
p2 = obj_sieve.get_p_numbers()
s2 = obj_sieve.get_sum()
avg2 = obj_sieve.get_average()

print("Ergebnisse für '1000' \n")

print("Output Class Primal")
print(p1)
print(f"Summe: {s1}")
print(f"Average: {avg1} \n")

print("Output Class SieveOfEratosthenes")
print(p2)
print(f"Summe: {s2}")
print(f"Average: {avg2} \n")

if len(p1) == len(p2) and s1 == s2 and avg1 == avg2:
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            print("Lösungen sind unterschiedlich")
    print("Lösungen sind gleich")
else: 
    print("Lösungen sind unterschiedlich")

print("--------------")

#Teilaufgabe b + c
max_number = 1000
obj_sieve = SieveOfEratosthenes()
obj_sieve.set_to_number(max_number)
print(f"Vergangene ms je 100 Schritte (Sieve): {obj_sieve.clalc_time_between_steps()} \n")

obj_primnal = Primal()
obj_primnal.set_to_number(max_number)
print(f"Vergangene ms je 100 Schritte (Primal): {obj_primnal.clalc_time_between_steps()}")
