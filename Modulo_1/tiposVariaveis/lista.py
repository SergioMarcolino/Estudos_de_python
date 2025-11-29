#List, collection of elements 

my_list = [1, 2, 3, 4, 5]

print(f"Minha lista de exempplo: {my_list}")

print("Indece 0 da minha lista: ", my_list[0])
print("fatiamento da lista : ", my_list[1:7])
print("fatiamento da lista : ", my_list[:5])
print("fatiamento da lista : ", my_list[2:])


my_list [0] = "ola"
print(my_list)
#List Metods
#append(), adds an element to the list 
my_list.append(1)
print(my_list)

#Index 
indice = my_list.index(1)
print(indice)

# Insert

my_list.insert(7, "mundo")
print(my_list)

# pop

elemento_removido = my_list.pop(2)
print(elemento_removido)
print(my_list)

# remove
my_list.remove(True)
print(my_list)

#sort

my_list.sort()
print(my_list)