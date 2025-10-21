import string

text = input("Enter a phrase: ")

clean_text = "".join(ch for ch in text if ch not in string.punctuation)

words = clean_text.split()

capitalized = [word.capitalize() for word in words]

hashtag = "#" + "".join(capitalized)

hashtag = hashtag[:140]

print(hashtag)
