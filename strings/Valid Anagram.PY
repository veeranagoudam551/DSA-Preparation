# Check if two strings are anagrams of each other
#Time Complexity  : O(n)
#Space Complexity : O(n)
def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    count ={}
    for char in s:
        count[char] = count.get(char,0)+1
    for char in t:
        if char not in count:
            return False
        count[char] -= 1

        if count[char]<0:
            return False
    return True 
    

s = "anagram"
t = "nagaram"
print(valid_anagram(s,t))






#The same characters
#The same number of times
#But the characters can be in a different order.