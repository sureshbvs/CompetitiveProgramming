def uniqueMorse( words):
    keys = [chr(i) for i in range(97,123)]
    values = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",
              ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = values[i]
        #print(dict)
    l = []
    for word in words:
        #print(i)
        string = ' '
        for letter in word:
            string += dict[letter]
            #print(string)
        l.append(string)        
    return len(set(l))
#words = ["gin","zen","gig","msg"] #o/p:2
#words = ["a","z","g","m"]         #o/p:4
#words = ["bhi","vsv","sgh","vbi"]  #o/p:3
#words = ["a","b","c","d"]           #o/p:4
words = ["hig","sip","pot"]          #o/p:2
print(uniqueMorse(words))
