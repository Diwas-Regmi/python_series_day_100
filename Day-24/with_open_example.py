file = open("hi.txt")
content = file.read()
print(content)
                    # modes = r(read), w(write), a(append)
                    # ^^
                    # ..
                    # ..
                    # ..
with open("hi.txt", mode = r) as file:
    content = file.read()
    print(content)