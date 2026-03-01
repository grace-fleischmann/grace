#homework 4 

# ---Lists---
# list operations 
fav_foods = ["lemon chicken", "pasta primavera", "butter chicken", "bruchetta", "pad see ew"]

print(fav_foods[1])
print(fav_foods[-1])
fav_foods.append("broccoli")
fav_foods.insert(0,"apple")
fav_foods.remove("butter chicken")
print(len(fav_foods))
for food in fav_foods:
    print(food.upper())

first_food = fav_foods[:1] + fav_foods[-1:]
if "potato" in fav_foods:
    print("A potato!")
else:
    print("No potato!")

# slicing and striding 

numbers = list(range(21))

def get_first_15(numbers):
    return numbers[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    lst.reverse()
    return lst[::-1][::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

# ---nested lists---
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
#---nested list opperations---
print(numbers[0])
print(numbers[1][1])
numbers.append([10,11,12])
def sum_nested(lst):
    total = 0 
    for row in lst: 
        for num in row: 
            total += num 
    return total 

# --- 5x5 list ---
def make_5x5():
    grid = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
            grid.append(row)
    return grid 

def mult_of3(lst):
    for i in range(len(lst)):
        for j in range(len(list[i])):
            if lst[i][j] % 3 ==0:
                lst[i][j] = "?"
    return lst

def not_a_question_mark(lst):
    sum = 0 
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] != "?":
                sum += lst[i][j]
    return sum

#dictionaries 
# --- dictionary operations --- 
ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100 
del ages["Mariam"]
for name, age in ages.items():
    print(name,age)


#fav function 
print(sum_nested(numbers))
