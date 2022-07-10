from kalkulator import operations

#odczytaj dane z dane.txt
# operacja a b


with open('dane.txt') as f:
    data = f.read().splitlines()

    for i in data:
        op, a, b = i.split() # to samo co i.split(" ")
        a, b = int(a), int(b)
        print(operations[op](a,b))