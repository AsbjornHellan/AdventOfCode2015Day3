# How many houses receive at least one present?
file_input = open('input_2015_day3.txt' , 'r')



history = []

while 1:
    char = file_input.read(1)
    history += char
    if not char:
        break
print(history)
print(len(history))

dir_north = '^'
dir_south = 'v'
dir_east = '>'
dir_west = '<'
presents_delivered = 0

# Delive one present for each visit
for house in history:
    if house == dir_north or house == dir_south or house == dir_east or house == dir_west:
        presents_delivered += 1

# Subtract one present for each move forward and backward
pre_visit = '>'
for house in history:
    if house == '^' and pre_visit == 'v':
        presents_delivered -= 1
    pre_visit = house
for house in history:
    if house == 'v' and pre_visit == '^':
        presents_delivered -= 1
    pre_visit = house
for house in history:
    if house == '>' and pre_visit == '<':
        presents_delivered -= 1
    pre_visit = house
for house in history:
    if house == '<' and pre_visit == '>':
        presents_delivered -= 1
    pre_visit = house

# Subtract two presents for each square move
        

print(presents_delivered)

file_input.close()