## cara membuat list
data_range = range(0,10,2) #range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

## membuat list dengan for loop, list comperhension
#bisa kuadrat
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)    

## membuat list dengan for pake if
#genap
list_pake_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_pake_for_if)
#ganjil
list_pake_for_if = [i for i in range(0,10) if i %2 != 0]
print(list_pake_for_if)
#5 hilang
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)