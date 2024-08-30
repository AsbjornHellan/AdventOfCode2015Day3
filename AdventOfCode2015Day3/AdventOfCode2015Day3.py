file_input = open('input_2015_day3.txt' , 'r')

dir_north = '^'
dir_south = 'v'
dir_east = '>'
dir_west = '<'

square_north = '^>v<'
square_east = '>v<^'
square_south = 'v<^>'
square_west = '<^>v'
north_south = '^v'
south_north = 'V^'
east_west = '><'
west_east = '<>'



presents_delivered = 0

while 1:
    char = file_input.read(1)
    print(char)
    # How many houses receive at least one present?
    
    # Present for each house
    if char == dir_north:
        presents_delivered += 1
    elif char == dir_south:
        presents_delivered += 1
    elif char == dir_east:
        presents_delivered += 1
    elif char == dir_west:
        presents_delivered += 1

    # Subtract 1 present for each return
    # Subtract 2 presents for each square
    
    if not char:
        break
print(presents_delivered)


file_input.close()