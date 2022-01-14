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
    

    
# palindrome by removing one character

Python easy to understand O(n) time O(1) space solution.

    def isPalindrome(self, start, end, s, deletionAllowed):
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            elif deletionAllowed:
                return self.isPalindrome(start+1, end, s, False) or self.isPalindrome(start, end-1, s, False)
            else:
                return False
        return True
    
    def validPalindrome(self, s: str) -> bool:
        deletionAllowed = True
        return self.isPalindrome(0, len(s)-1, s, deletionAllowed)
