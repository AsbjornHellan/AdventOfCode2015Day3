# How many houses receive at least one present?
file_input = open('input_2015_day3.txt' , 'r')



town = []

while 1:
    char = file_input.read(1)
    town += char
    if not char:
        break
print(town)
print(len(town))

# Delive one present to each visit
presents_delivered = 0
for house in town:
        presents_delivered += 1

# Subtract one present for each move backward
pre_house = '>'
for house in town:
    if pre_house == '>' and house == '<':
        presents_delivered -= 1
    pre_house = house

for house in town:
    if pre_house == '<' and house == '>':
        presents_delivered -= 1
    pre_house = house

for house in town:
    if pre_house == '^' and house == 'v':
        presents_delivered -= 1
    pre_house = house

for house in town:
    if pre_house == 'v' and house == '^':
        presents_delivered -= 1
    pre_house = house

# Subtract one presents for each square move


print(presents_delivered)

file_input.close()