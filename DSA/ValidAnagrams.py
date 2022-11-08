def validAnagrams(s1,s2):
    if(len(s1)!=len(s2)):
        return False
    hash1={}
    hash2={}
    for letter in s1:
        if letter in hash1.keys():
            hash1[letter]+=1
        else:
            hash1[letter]=1
    for letter in s2:
        if letter in hash2.keys():
            hash2[letter]+=1
        else:
            hash2[letter]=1
    for key in hash1.keys():
        if key not in hash2.keys() or hash2[key]!=hash1[key]:
            return False

    return True

print(validAnagrams("aabc","cabaz"))
