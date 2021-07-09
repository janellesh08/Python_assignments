print("Is that word a palindrome? Let's find out!")

word = input("Enter the word here: ")

rev_word = ""

for x in range(len(word) -1, -1, -1):
    rev_word += word[x]

if word == rev_word:
    print("Yep! That's a palindrome for you!")

elif( word != rev_word):
    print("Nope! This is not a palindrome. Sorry.")


