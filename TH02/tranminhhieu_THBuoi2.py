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
        if (flag):
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
    list1 = [12, 3, 6, 78, 35, 55, 120]
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


def cau09():
    chuoi = input('Nhap vao mot cau: ')
    print(chuoi[::-1])


def cau10():
    chuoi = ''
    while len(chuoi) < 2:
        chuoi = input('Nhap vao chuoi: ')
        if len(chuoi) < 2:
            print('Chuoi nhap vao phai co tu 2 ky tu!!!')
    tmp1 = chuoi[:2]
    tmp2 = chuoi[len(chuoi) - 2:]
    res = ''.join(map(str, tmp1 + tmp2))
    print(res)


def cau11():
    chuoi1 = list(input('Nhap vao chuoi 1: '))
    chuoi2 = list(input('Nhap vao chuoi 2: '))

    res = f'{chuoi1},{chuoi2}'
    res = list(res)
    res[:2], res[len(chuoi1) + 2:len(chuoi1) + 4] = res[len(chuoi1) + 2:len(chuoi1) + 4], res[:2]
    res = ''.join(res)
    print(res)


def cau13():
    chuoi = input('Nhap vao chuoi: ')
    c = chuoi[0]
    res = c + chuoi.replace(c, '@')[1:len(chuoi)]
    print(res)


def getsuffix(a, b):
    res_set = set()
    for c1 in a:
        for c2 in b:
            if c1.startswith(c2) and c1[len(c2):] != '':
                res_set.add(c1[len(c2):])
            elif c2.startswith(c1) and c2[len(c1):] != '':
                res_set.add(c2[len(c1):])
    return res_set


def cau14():
    a = ['a', 'ac', 'ab']
    b = ['c', 'abc']
    print(getsuffix(a, b))


def kiemTraBangMa(a):
    S0 = a
    S1 = getsuffix(S0, S0)
    S1_old = S1

    while len(S1) > 0:
        S2 = getsuffix(S0, S1)
        Stmp = S2.intersection(S0)

        if len(S2) == 0:
            print('Day la bang ma tach duoc')
        elif len(Stmp) != 0:
            print('Day la bang ma khong tach duoc')
            break
        elif S2 == S1_old:
            print('Day la bang ma khong tach duoc')
            break
        S1_old = S1
        S1 = S2


def cau15():
    kiemTraBangMa(['a', 'ac', 'ab', 'c', 'abc'])


def cau16():
    a = ["abc", "a", "ab", "b", "bcad"]
    b = ["a", "ad", "bbcde", "c", "deb", "ebd"]
    c = ["a", "ad", "bbcde", "c", "deb", "ebad"]
    print('Kiem tra bang ma a: ', a)
    kiemTraBangMa(a)
    print('Kiem tra bang ma b: ', b)
    kiemTraBangMa(b)
    print('Kiem tra bang ma c: ', c)
    kiemTraBangMa(c)
