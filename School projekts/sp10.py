word = input("Enter a word: ")
vowels = 0
consonants = 0
upcase = 0
lowcase = 0

## Count of vowels and consonants 
for i in word:
  if i == 'a' or 'e' or 'i' or 'o' or 'u':
    vowels += 1
   elif i == 'A' or 'E' or 'I' or 'O' or 'U':
    vowels += 1
   else:
    consonants += 1

##Count of upper and lower cases
for i in word:
  if i.isupper():
    upcase += 1
   elif i.islower():
    lowcase += 1
 
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"upper case: {upcase}")
print(f"lower case: {lowcase}")
