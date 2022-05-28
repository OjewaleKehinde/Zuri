# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    char_word = sorted(list(word))
    char_anagram = sorted(list(anagram))
    if char_word == char_anagram:
        return True
    else:
        return False
    

find_anagrams("hello", "check")
find_anagrams("below", "elbow")
find_anagrams("stool in top", "pot in tools")
