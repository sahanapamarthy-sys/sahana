favorite_food = ["pizza", "pasta", "paneer butter masala", "burritos", "burgers"]

print(favorite_food[1]) #second in the list 

print(favorite_food[-1]) #last using negative indexing

favorite_food.append("mac and cheese") #append to end

print(favorite_food) #printing appended line 

favorite_food.insert(0, "apple") #inserting at apple in the front

print(favorite_food) #printing apple in front 

del favorite_food[2] #deleting third in list 
print(favorite_food) 

print(len(favorite_food)) #printing length of list 

for food in favorite_food: 
	uppercase = food.upper() #Error: At first i didnt assign a variable to food.upper() and just did food.upper() and printed food which didnt do anything uppercase. 
	print(uppercase)
#making new list with only 2 values 
new_list = list() 
new_list.append(favorite_food[0])
new_list.append(favorite_food[-1]) 

print(new_list) 


if "potato" in favorite_food:  #Error: I initally used a for loop to iterate through every food in the list but it ended up giving too many No potato. I simplified and just used a simple if statement. 
	print("A potato!")
else:
	print("no potato")

numbers_list = list(range(0,21))
print(numbers_list)

def get_first_15(numbers_list):
	return numbers_list[0:16]
print(get_first_15(numbers_list))

numbers_15= get_first_15(numbers_list)

def get_every_fifth(numbers_15): 
	return numbers_15[::5]
print(get_every_fifth(numbers_15))

numbers_5 = get_every_fifth(numbers_15)

def reverse_stride(numbers_5): 
	reversed_num = numbers_5[::-1]
	final_product = reversed_num[::3]
	return final_product
print(reverse_stride(numbers_5))

list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [7,8,9]
numbers = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

print(numbers[2]) #printing the third row 

print(numbers[1][1]) #second column and second row 

numbers.append([10,11,12])
print(numbers)

def sum_nested(numbers): 
	for row in numbers: 
		sum_total = sum(row)
		print(sum_total)

(sum_nested(numbers))

def nested_for_loop():
	nested_list = list()
	row = list()
	for i in range(5): 
		row = [5*i +1, 5*i +2, 5*i +3, 5*i +4, 5*i+5]
		nested_list.append(row)
	return nested_list
print(nested_for_loop())
	
new_list = nested_for_loop()


def multiples_3(new_list): 
	for row in new_list: 
		for i in range(len(row)): #Error: that int len(row) is not iterable and i ended up forgetting the range function 
			if row[i] % 3  == 0: 
				row[i] = "?"
	return new_list 

surprise_list = (multiples_3(new_list))
for row in surprise_list:
    print(row)

def not_question(surprise_list): 
    total = 0 
    for row in surprise_list: 
        for i in range(len(row)):
            if row[i] != "?":  # only sum numbers
                total += row[i]
    return total

print(not_question(surprise_list))

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])

ages["Mira"] = 100

print(ages["Mira"])

ages["Milana"] = 52

print(ages)

del ages["Mariam"]
print(ages)

for names in ages.items(): 
	print(names)


#favorite function

numbers_list = list(range(0,21))
print(numbers_list)

def get_first_15(numbers_list):
	return numbers_list[0:16]
print(get_first_15(numbers_list))








