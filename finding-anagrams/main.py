# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    if(sorted(word) == sorted(anagram)):
        print(True)
        return True
    else:
        print(False)
        return False
word1 = input("Enter first word: ")
anagram1 = input("Enter second word: ")
find_anagram(word1, anagram1)

