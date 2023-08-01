"""def msg(m):
    print ("-"*30)
    print(m)
    print ("-"*30)
if __name__ == "__main__":
    msg("Michael")
    msg("Codigo Brazuca")
    msg("oioi")
    msg("ola")"""


"""def test(x):
    print(f"O dobro de {x} e {x*2}")
    return x*2
v = test(5)
print(v)"""


"""def test(msg):
    print(msg)

def dumb():
    return test

v = dumb()
print(v)"""

        #Para receber mais de um argumentos 
"""def test(*args):
    for i in args:
        print(i)
    print(args)
test(1,2,3, "Michael", 5)"""

"""lista = [1,2,3,4,5]

n1,n2, *n = lista

print(n1,n1,n )"""


def tes (*args, **kwargs):
    print(args)
    print(kwargs["Nome"])