# Python og Pita workshop
- [Link til slides](https://bit.ly/2MDHOdR)
- Kode eksempler ligger i `eksempler` mappen

## Installation af Python 3
- **Windows:** https://realpython.com/installing-python/#windows
- **MacOS:** https://realpython.com/installing-python/#macos-mac-os-x
- **Linux:** https://realpython.com/installing-python/#linux

## Del 1 - Opgaver
### Opgave 1.
TODO

### Opgave 2.
TODO

### Opgave 3.
TODO

### Opgave 4.
TODO

## Del 2 - Opgaver
### Opgave 1.
TODO

### Opgave 2.
Lav en klasse, som representerer en person. Den skal kunne printe en person med navn `name` og alder `age`, som `name (age years old)`. Derudover skal det være mulig at sammenligne to personer på deres alder. 

**Skabelon:**
```python
class Person:
	pass

person1 = Person("Alice", 17)
person2 = Person("Bob", 19)
person3 = Person("Charles", 24)

print(person1)           # Output: "Alice (17 years old)"
print(person2)           # Output: "Bob (19 years old)"
print(person2)           # Output: "Charles (24 years old)"
print(person1 > person3) # Output: False
print(person2 > person1) # Output: True
```

### Opgave 3.
Lav en funktion, som tjekker hvorvidt et given tal `n` er et primtal. Det kan gøres ved at alle løbe talene fra 2 til sqrt(n) og tjekke hvorvidt tallet går op i `n`

**Skabelon:**
```python
def is_prime(n):
	pass

print(is_prime(7))  # Output: True
print(is_prime(16)) # Output: False
print(is_prime(23)) # Output: True
```

### Opgave 4
Lav en funktion som laver bineær søgning over en liste og et element. Det vil sige en funktion `binary_search` som tager en liste `lst` og et element `elm` og retunerer et index `i` hvor `lst[i] == elm` 
	
**Skabelon:**
```python
def binary_search(lst, elm):
	pass

print(binary_search([1,5,9,12], 5))     # Output: 1
print(binary_search([8,12,16,42], 42))  # Output: 3
print(binary_search([15,22,51,72], 15)) # Output: 0
```

## Brugbare biblioteker
- https://docs.python.org/3/library/math.html
- http://mypy-lang.org/
- https://www.sympy.org/en/index.html
- https://docs.scipy.org/doc/numpy/reference/
- https://matplotlib.org/contents.html
- https://ipython.readthedocs.io/en/stable/

