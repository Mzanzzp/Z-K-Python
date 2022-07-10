from time import sleep

def delay(func, x, *args, **kwargs):
    sleep(x)
    return func(*args, **kwargs)

def ala():
    print("ala ma kota")

def potegi(a, b):
    return print(a**b)

delay(ala, 2)
delay(potegi, 3, 5, 2)
