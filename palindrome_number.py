# Transforming int into string
def isPalindrome(x):
        if x == 0: return True
        if x > 0:
                x = str(x)
                if x == x[::-1]:
                        return True
                else:
                        return False
        else: return False

isPalindrome(x=-121)

# Not transforming int into string
def isPalindrome2(x):
        if x == 0: return True
        if x > 0:
                temp_number = x
                reverse = 0
                while temp_number != 0:
                        last_digit = temp_number % 10
                        reverse = reverse * 10 + last_digit
                        temp_number = int(temp_number/10)
                if x == reverse: return True
                else: return False
        else: return False
        
isPalindrome2(x=121)
