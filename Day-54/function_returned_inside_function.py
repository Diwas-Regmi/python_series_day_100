def outer_func():
    print("im outer")
    def nested_func():
        print("I'm inner")

    return nested_func # the parenthesis are not given because it will activate the func

inner_func = outer_func()
inner_func() # now the inner function has nested_func without parenthesis and the parenthesis is given to inner_func() so that it will activate the function