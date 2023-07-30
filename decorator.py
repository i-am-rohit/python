# @ use for decorator


def dec_func(func):
    def wrap():
        print("This is Awesom Function")
    func()
    return  wrap

@dec_func
def func1():
    print("This is function 1")

func1()


@dec_func
def func2():
    print("This is function 2")
#

func2()
#
# var1 = dec_func(func1)
# var1()
# var2 = dec_func(func2)
# var2()