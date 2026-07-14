text = input("Enter a string: ")

vowel_count = 0
consonant_count = 0

vowels = "aeiouAEIOU"

for letter in text:
    if letter.isalpha():
        if letter in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)