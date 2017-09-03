def myfun():
    print ("function without parameters")

myfun()


def safe_div (x, y):
    if y != 0:
        z = x/y
        print z
        return z
    else:
        print("shit")

b = safe_div(10,4)
print (b)

def task1 (x):

    print ("hello ", x)

task1('world')