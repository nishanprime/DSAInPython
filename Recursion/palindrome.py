def isPalindrome(str):
    if len(str) <=1:
        return  True
    if str[0]==str[len(str)-1]:
        return isPalindrome(str[1:len(str)-1])
    return False

print(isPalindrome('abaccaba'))