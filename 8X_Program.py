# Lekce 7 příklad 1
file_contents = open("text1.txt", "r")
print('druhý řádek souboru: ', file_contents.readlines()[1])
file_contents.close()

# Lekce 7 příklad 2
weird_thing = open("text1.txt", "r")
print("každý druhý znak: ", weird_thing.readline()[1::2])
weird_thing.close()

# Lekce 7 příklad 3
# a.
file = open('text2.txt', "r")
line_contents = file.readline()
longest_line_length = 0
count = 0
while line_contents:
 line_contents = file.readline()

 count += 1

 if len(line_contents) > longest_line_length:
    longest_line_length = len(line_contents)
file.close()

print('počet řádků souboru:', count)
print('nejdelší řádek má ' + str(longest_line_length) + ' znaků')
# b.
for count, line in enumerate(file):
    pass
print("Počet řádků: ", count + 1)







