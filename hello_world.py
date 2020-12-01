print("fact")
def fact(n):
    fact=1
    for i in range(1,n):
        fact = fact * i
        print fact

a = fact(3)
print(a)
