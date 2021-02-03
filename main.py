def countA(w):
    count = w["a"]
    
    for i in range(0,len(w)):
        if w[i]:
            return count
        
    return False
    
print(countA("cat"))
