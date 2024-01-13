input1 = [5, 3, 7, 2, 6]
input2 = [4, 1, 5, 2]

def Zarb(input1, input2):
    i = 0
    zarb=[]
    
    while i < len(input1) + len(input2)-1:
        zarb.append(0)
        i+=1
        
    i=0
    while i<len(input1):
        j = 0
        while j<len(input2):
            zarb[i+j] += input1[i] * input2[j]
            j+=1
        i+=1
    return zarb
result = Zarb(input1, input2)
print(result)