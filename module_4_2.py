def test_function():
    def inner_function():
        print('Я в области видимости функции inner_function')

    inner_function()


test_function()
# inner_function() - name 'inner_function' is not defined
