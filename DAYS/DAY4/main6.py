
# mini project: Hiding your treasure

line1 = [ " ", " ", " "]
line2 = [ " ", " ", " "]
line3 = [ " ", " ", " "]

map = [line1, line2, line3]
print(f"{line1}\n{line2}\n{line3}")


print("Hiding your treasure! X marks the spot.")

position = input('Where do you want to put the treasure: a1,a2,a3,b1,b2,b3,c1,c2,c3')
print(position, type(position)) # both digit are in string format

# Since strings are the sequence of characters which are stored based on index data structure. Therefore fetching the first digit using index position and converting it into lower case.
letter = position[0].lower()
print('letter is ',letter)

# taking one temporary list to create logic
abc = ['a', 'b', 'c']

# matching the letter with the temporary list to get the letter index
letter_index = abc.index(letter)

# Since strings are the sequence of characters which are stored based on index data structure. Therefore fetching the first digit using index position and converting it into number.

# subtracting it from -1 because available index positions are from 0-2 in the nested list and  fetched element's value can be a"1", a"2", a"3"
print(position[1])
number_index = int(position[1]) - 1

print(number_index , letter_index)

# updating the map's sub list hence it will also update the original list because map is referring to the same list, map is not copying the list.
map[number_index][letter_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")
