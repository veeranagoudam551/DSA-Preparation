def to_lower(s):
        result=""
        for ch in s:
            if 'A' <=ch <='Z':
                result=result+chr(ord(ch)+32)
            else:
                result=result+ch
        return result
    
s="HELLO"
print(to_lower(s))