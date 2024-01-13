input1 = [3, 5, 2, 7]
X0 = 0
def Meghdar_Tabe (input1):
    sum = 0
    i = -1
    t = 0
    while t < len(input1):
        sum += input1[i]*(X0**t)
        i-=1
        t+=1
    return sum
result = Meghdar_Tabe(input1)
print(result)