def find_anagrams(word, anagram):
    char_word = sorted(list(word))
    char_anagram = sorted(list(anagram))
    if char_word == char_anagram:
        return True
    else:
        return False
    

find_anagrams("hello", "check")
find_anagrams("below", "elbow")
find_anagrams("stool in top", "pot in tools")
