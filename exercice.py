#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(n) -> float:
    return abs(n)


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    for n in prefixes:
        return n + suffixes


def prime_integer_summation() -> int:
    for n in range(1,100):
        k=0
        while k*k < n:
            if k%n ==0:
                return false
            k=k+1
            print(k)
                
                   
    return 0


def factorial(number: int) -> int:
    return math.factorial(number)


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
