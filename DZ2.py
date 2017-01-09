list_even = []
list_odd = []
def numnum():
    while True:
        try:
            print('Enter any number')
            number = int(input())
        except ValueError:
             print('Is it too hard to enter a number?')
             continue
        else:
            break
    if number % 2 == 0:
        list_even.append(number)
    elif number % 2 != 0:
        list_odd.append(number)
numnum()
def sorting_asc(sortlist):
    a = sortlist
    for i in range(len(a)):
        idxMin = i
        for j in range(i+1, len(a)):
            if a[j] < a[idxMin]:
                idxMin = j
        tmp = a[idxMin]
        a[idxMin] = a[i]
        a[i] = tmp
    return a
def sorting_desc(sortlist):
    a = sortlist
    for i in range(len(a)):
        idxMax = i
        for j in range(i+1, len(a)):
            if a[j] > a[idxMax]:
                idxMax = j
        tmp = a[idxMax]
        a[idxMax] = a[i]
        a[i] = tmp
    return a
while True:
    print('Do you want to continue? Yes/No')
    contin = input() 
    if contin in ['Yes', 'yes', 'y', 'Y']:
        numnum()
        continue
    elif contin in ['No', 'no', 'n', 'N']:
        print('Your lists:')   
        print(list_even)
        print(list_odd)
        print('Sort the lists in ascending or descending order? asc/desc')
        sort = input()
        if sort in ['asc', 'Asc']:
            print(sorting_asc(list_even))
            print(sorting_asc(list_odd))
        elif sort in ['desc', 'Desc']:
            print(sorting_desc(list_even))
            print(sorting_desc(list_odd))
        break
