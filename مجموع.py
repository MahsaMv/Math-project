input1 = [3, 5, 2, 7, 4]
input2 = [2, 4, 5]
def Majmoe_2_Tabe (input1, input2):
    i=0
    sum = []
    while len(input1) != len(input2):
        input2=list(reversed(input2))
        input2.append(0)
        i+=1
        input2=list(reversed(input2))
    j=0    
    while j<len(input1):
        a = int(input1[j]) + int(input2[j])
        sum.append(a)
        j +=1
    return(sum)
result = Majmoe_2_Tabe(input1, input2)
#print(result)