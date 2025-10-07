# Check if a string is palindrome
#Author: Narasimman
def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]

string = input('Enter a string to check palindrome: ')
if is_palindrome(string):
    print(f'"{string}" is a palindrome')
else:
    print(f'"{string}" is not a palindrome')