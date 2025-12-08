###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"
# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
x = movie.upper
print('Title in upper:', movie.upper())

# print title in small letters
print('Title in lower:', movie.lower())

# print how many times the vowel "e" appears in the title
print('how many times e appears:', movie.count("e"))

# print where in the text is the word "Lord"
print('where is the word "lord":', movie.find("Lord"))

# print where in the text is the word "dragon"
word = "dragon"
index_word = movie.find(word)
if index_word != -1:
    print(f'where is "dragon": nie ma')
else:
    print(f'where is "dragon": nie ma')