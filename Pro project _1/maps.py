lists = ["1", "2", "3", "4", "5"]
print(lists)
new_lists = list(map(int, lists))
print(new_lists)


# another example of maps
prices = [100,200,300,400,500]

new_prices = list(map(lambda x: x - x*5/100, prices))
print(new_prices)

# another example
names = ["ram", "shyam", "diwas"]
new_names_ordered = list(map(lambda x: str.capitalize(x), names))
print(new_names_ordered)

# celcius to farhenheit

celsius_temp = [25,30,15, 10,35]
celc_far = list(map(lambda x: (x*1.8) +32, celsius_temp))
print(celc_far)




#extract initials from name using map

names = ["diwas regmi", "alice chaudhary", "pheobe christ", "john cena"]
names_new = list(map(str.title, names))
seperated_names = list(map(lambda x: x.split(), names_new))
print(seperated_names)
name_org = list(map(lambda x : "".join([name[0] for name in x]), seperated_names))


print(name_org)



# reverse list using map

word = "abcdefghijklmnop"
print(word[3:9:3])

words = ["Python", "Java", "JavaScript", "C++"]

