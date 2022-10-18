word = input("Input a number: ")
revword = word[::-1]

if word == revword:
  print("The number is a palindrome")
else:
  print("The number is not a palindrome")
