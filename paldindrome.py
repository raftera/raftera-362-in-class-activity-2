def user_palindrome():
    string = input("Enter a string to test if it's a palindrome.")
    if palindrome(string):
        print(string + " is a palindrome.")
    else:
        print(string + " is not a palindrome.")


def palindrome(string):
    if string == string[::-1]:
        return 1
    return 0