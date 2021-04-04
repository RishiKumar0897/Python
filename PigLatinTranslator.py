print("Welcome to Pig Latin!")

pyg = 'ay'

original = input("Enter a word to have it translated to pig latin! ")

if len(original) > 0:
    word = original.lower()
    first_letter = original[0]
    print(original)
   
else:
    print("empty")

new_word = word + first_letter + pyg
new_word = new_word[1:]
print(new_word)