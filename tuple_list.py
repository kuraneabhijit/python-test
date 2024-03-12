tuple_1=('Saaaaa','Pune',411038)
tuple_2=('Raaaa','Mumbai',411043)
print("tuple 1 0th index",tuple_1[0])

print('tuple merge',tuple_1+tuple_2)

list_1=['aa','bb','cc']
list_2=['xx','yy','zz']

print('list merge',list_1+list_2)

numbers=(1,3) * 4
print(numbers)
# o/p (1,3,1,3,1,3,1,3)


digits=[1,3] * 4
print(digits)
# o/p [1,3,1,3,1,3,1,3]

#swapping
first=1
second=2
print('before swapping',first,second)
first,second=second,first
print('after swapping',first,second)

test1=('abb',33)
test2=('bbc',44)
dict_1={test1:'afa',test2:'kfk'}
print(dict_1)

for kk in dict_1:
    print(kk)

list_test=[3,5,2,53,55,22]
print(list_test[-4:-2])


