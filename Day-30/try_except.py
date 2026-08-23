try:
    a = 90
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a)
    print(a_dict["key"])
    # if a_dict["key"]:
    #     raise SyntaxError("this is just a made up raise by mr diwas")

except SyntaxError as message:
    print(message)

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Diwas Regmi")

except KeyError as message:
    print(f"The key {message} does not exist.")
except NameError as error:
    print(error)
    print(f"The variable {error}")

else:
    print(file.read())
finally:
    file.close()
    print("The File was Closed.")