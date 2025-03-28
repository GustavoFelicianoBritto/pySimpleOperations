num = int( input("Insira o número a ser calculado: "))


print(f"\nSoma\n------------------\n")
for i in range(11):
    print(f"{num} + {i} = {num+i}")
print(f"\nSubtração\n------------------\n")
for i in range(11):
    print(f"{num} - {i} = {num-i}")
print(f"\nMultiplicação\n------------------\n")
for i in range(11):
    print(f"{num} * {i} = {num * i}")
print(f"\nDivisão\n------------------\n")
for i in range(11):
    if(i>0):
        print(f"{num} / {i} = {num/i:.2f} " )