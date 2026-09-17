def outer_func():
    print("I'm Outer !")

    def nested_func():
        print("I'm Inner")

    nested_func() # the nested_function can only be called inside the main func
    # without nested function called the output is only gonna be im outer


# nested_func() will throw an error because the func only exist inside another func
outer_func()