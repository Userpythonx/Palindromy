def palindromy(word):
    word=word.lower().replace(" ", " ")
    return word ==word [::-1]

word = "kayak"
if palindromy(word):
    print(f"{word} jest palindromem")
else:
    print(f"{word} nie jest palindromem")

palindromy("kajak")
