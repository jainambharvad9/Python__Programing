def myrev(mystr):
    length = len(mystr)
    for i in range(length -1,-1,-1):
        yield mystr[i]
        
for char in myrev("JAINAM BHARVAD"):
    print(char)