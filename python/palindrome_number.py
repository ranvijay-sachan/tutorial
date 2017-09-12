num = raw_input("enter number:")
rev = reversed(num)
if list(num) == list(rev):
    print "palindrome"
else:
    print "not palindrome"


def is_palindrome(text, ignoreCase=True):
    if ignoreCase:
        text = text.lower()
    return text == text[::-1]

if __name__ == '__main__':
    print is_palindrome('rar')