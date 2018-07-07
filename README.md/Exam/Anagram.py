chars = 256
def anag(s1, s2):
    arr1 = [0]*chars
    arr2 = [0]*chars
    for i in s1:
        arr1[ord(i)] += 1
    for i in s2:
        arr2[ord(i)] += 1
    if len(s1) != len(s2):
        return 0
    for i in range(chars):
        if arr1[i] != arr2[i]:
            return 0 
    return 1 
word1 = input()
word = word1.replace(" ","")
word2 = input()
word3 = word2.replace(" ","")
if anag(word.lower(), word3.lower()):
    print ("True")
else:
    print ("False")
 


# Test case1: anagram, nagaram – true
# Test case2: Keep, Peek – true
# Test case3: Mother In Law, Hitler Woman – true
# Test case4: School Master, The Classroom – true
# Test case5: ASTRONOMERS, NO MORE STARS – true
# Test case6: Toss, Shot – false
# Test case7: joy, enjoy – false
# Test case8: Debit Card, Bad Credit – true
# Test case9: SiLeNt CAT, LisTen AcT – true
# Test case10: Dormitory, Dirty Room – true
