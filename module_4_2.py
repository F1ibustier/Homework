# Пространство имен
# coded by f1ibustier

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
#inner_function() в этом месте вызов внутренней функции выдает ошибку
test_function()
