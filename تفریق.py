input1 = [3, 5, 4]
input2 = [2, 4, 5, 5]

def Tafriq_2_Tabe (input1, input2):
    i=0
    j=0
    m=0
    Tafazol = []
    while len(input1) > len(input2):
        input2=list(reversed(input2))
        input2.append(0)
        i+=1
        input2=list(reversed(input2))
            
    while len(input1) < len(input2):
        input1 = list(reversed(input1))
        input1.append(0)
        j+=1
        input1 = list(reversed(input1))
        
    while m<len(input1):
        a = int(input1[m]) - int(input2[m])
        Tafazol.append(a)
        m +=1
    return(Tafazol)
result = Tafriq_2_Tabe(input1, input2)
print(result)