# Tran Minh Hieu - B2207521

def cau01():
    list = []
    for n in range(100, 300 + 1):
        tmp = n
        flag = True
        while tmp != 0:
            if (tmp % 10) % 2 != 0:
                flag = False
                break
            else:
                tmp = int(tmp / 10)
        if(flag):
            list.append(n)
    res = ','.join(map(str, list))
    print(res)

def cau02():
    chuoi = input('Nhap chuoi cac so cach nhau bang dau ",": ')
    list = chuoi.split(',')
    list = [int(x) for x in list if int(x) % 2 != 0]
    print(list)

def cau03():
    tudien = {}
    for i in range(0, 20):
        tudien.update({(i + 1): (i + 1) ** 2})
    print(tudien)

def cau04():
    list = [12, 24, 35, 70, 88, 120, 155]
    for i in [5, 4, 0]:
        list.pop(i)
    print(list)

def cau05():
    list1 =  [12, 3, 6, 78, 35, 55, 120]
    list2 = [12, 24, 35, 78, 88, 120, 155]
    res = [i for i in list1 if i in list2]
    print(res)

def cau06():
    list = [(i + 1) ** 2 for i in range(0, 20)]
    print(list[5:])

def cau07():
    list = []
    while len(list) < 7:
        n = input(f'Nhap so thu {len(list) + 1}: ')
        try:
            num = int(n)
            list.append(num)
        except:
            print('Gia tri khong hop le, vui long nhap lai!!!')
    tuple1 = tuple(list)

    list = [n for n in tuple1 if n % 2 == 0]
    tuple2 = tuple(list)
    print(tuple2)

def cau08():
    chuoi = input('Nhap vao chuoi: ')
    res = {}
    for c in chuoi:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    print(res)

cau08()
    