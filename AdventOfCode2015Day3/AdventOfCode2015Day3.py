file_input = open('input_2015_day3.txt' , 'r')

history = []

while 1:
    char = file_input.read(1)
    history += char
    if not char:
        break
print(history)



file_input.close()