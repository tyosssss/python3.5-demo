
x = 'global'

def func():
    x = 'func scope'
    def func_func():
        x = 'func_func scope'
        print(x)

    func_func()
    print(x)

func()
print(x)