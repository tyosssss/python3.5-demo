# coding=utf-8
# 格式化输出 9*9 乘法表
def multiply_9x9():
    return [[(x, y, x * y) for y in range(1, 10) if x >= y] for x in range(1, 10)]


# 使用str.rjust
def format_print_by_str_method():
    rets = multiply_9x9()

    print('format_print_by_str_method:')
    for row in rets:
        message = ''

        for item in row:
            x, y, z = item
            message += str(x) + ' x ' + str(y) + ' = ' + str(z).rjust(2) + '  '

        print(message)


# 使用模板方法输出
def format_print_by_template_method():
    rets = multiply_9x9()

    print('format_print_by_template_method:')
    for row in rets:
        message = ''

        for item in row:
            x, y, z = item
            message += '{0:d} x {1:d} = {2:2d}  '.format(x, y, z)

        print(message)


format_print_by_str_method()
format_print_by_template_method()
