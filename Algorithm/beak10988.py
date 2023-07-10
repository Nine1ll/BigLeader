import sys

palindrome = list(sys.stdin.readline())
palindrome = palindrome[:len(palindrome)-1]

if list(reversed(palindrome)) == palindrome:
    print(1)
else:
    print(0)
