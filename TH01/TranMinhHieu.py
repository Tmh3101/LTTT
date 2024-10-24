# Tran Minh Hieu - B2207521

# Cau 1:
name = input('Nhap ten: ')
print('Hello ' + name + ' Welcome to Python')

# Cau 2:
n = int(input('Nhap vao so n: '))
while not(0 < n < 10):
    n = int(input('n khong hop le (0 < n < 10), nhap lai: '))

m = 0
res = 0
for i in range(1, 5):
    m = m * 10 + n
    print(f'{m}', end='')
    res += m
    if i != 4:
        print(' + ', end='')

print(f' = {res}')

# Cau 3
a = int(input('Nhap a: '))
b = int(input('Nhap b: '))
while b == 0:
    b = int(input('b khong hop le, nhap lai: '))

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} ** {b} = {a ** b}')


import math


# Cau 4
r = float(input('Nhap vao ban kinh (r): '))
print(f'Chu vi hinh tron = {2 * math.pi * r}')
print(f'Dien tich hinh tron = {math.pi * (r ** 2)}')


# Cau 5
n = int(input('Nhap vao so n: '))
while n < 0:
    n = int(input('n khong hop le (n >= 0), nhap lai: '))

res = n
for i in range(1, n):
    res *= i

print(f'{n}! = {res}')

# Cau 6
def phuongTrinhBac2():
    a = float(input('Nhap a: '))
    while a == 0:
        a = float(input('Gia tri a khong hop le (a != 0), nhap lai: '))

    b = float(input('Nhap b: '))
    c = float(input('Nhap c: '))

    delta = b**2 - 4*a*c
    if delta < 0:
        print('Phuong trinh vo nghiem')
    elif delta == 0:
        print(f'Phuong trinh co nghiem kep: x1 = x2 = {-(b / (2 * a))}')
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print('Phuong trinh co 2 nghiem phan biet:')
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')


phuongTrinhBac2()


# Cau 7
for i in range(5000, 7000 + 1):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=' ')


# Cau 8
n = int(input('Nhap va so thap phan n: '))
res = []
while n != 0:
    res.append(n % 2)
    n = int(n / 2)

res.reverse()
for i in range(0, len(res)):
    print(res[i], end='')


# Cau 9
a = int(input('Nhap a: '))
while a < 0:
    a = int(input('Gia tri a khong hop le (a >= 0), nhap lai: '))

b = int(input('Nhap b: '))
while b < 0:
    b = int(input('Gia tri a khong hop le (b >= 0), nhap lai: '))

min_number = min(a, b)
if a == 0 or b == 0:
    print(f'UCLN = {a + b}')
else:
    for i in range(min_number, 0, -1):
        if a % i == 0 and b % i == 0:
            print(f'UCLN = {i}')
            print(f'BCNN = {int((a * b) / i)}')
            break


# Cau 10
def kiemTraSoNguyenTo(x):
    for j in range(2, int(math.sqrt(x) + 1)):
        if x % j == 0:
            return False
    return True


n = int(input('Nhap so nguyen n: '))
for i in range(2, n):
    if kiemTraSoNguyenTo(i):
        print(i, end=' ')


# Cau 11
for i in range(1000, 9999 + 1):
    if kiemTraSoNguyenTo(i):
        print(i, end=' ')


# Cau 12
n = int(input('Nhap so nguyen n: '))
while n < 0:
    n = int(input('Gia tri a khong hop le (n >= 0), nhap lai: '))
res = 0
arr = []
while n != 0:
    res += n % 10
    arr.insert(0, int(n % 10))
    n = int(n / 10)


for i in range(0, len(arr)):
    print(f'{arr[i]}', end='')
    if i != len(arr) - 1:
        print(' + ', end='')
print(f' = {res}')


# Cau 13
for i in range(1000, 2000 + 1):
    n = i
    check = False
    while n != 0:
        if (n % 10) % 2 == 0:
            check = True
            break
        n = int(n / 10)

    if not check:
        print(i, end=' ')


# Cau 14
n = int(input('Nhap so nguyen n: '))
while n < 0:
    n = int(input('Gia tri a khong hop le (n >= 0), nhap lai: '))

res = 0
for i in range(1, n + 1):
    res += i / (i + 1)

print(res)


# Cau 15
def getEntropy(array):
    res = 0
    for k in range(len(array)):
        if array[k] != 0:
            res -= array[k] * math.log2(array[k])

    return res


n = int(input('Nhap vao so luong phan tu trong day: '))
arr = []
for i in range(n):
    arr.append(float(input(f'Nhap phan tu thu {i + 1}: ')))

print(getEntropy(arr))

# Cau 16
X = [1/7, 6/7]
y_x1 = [1/4, 2/4, 1/4, 0]
y_x2 = [1/8, 3/8, 3/8, 1/8]
y = []

for i in range(len(y_x1)):
    y.append(X[0] * y_x1[i] + X[1] * y_x2[i])

H_y = getEntropy(y)
H_y_x = X[0] * getEntropy(y_x1) + X[1] * getEntropy(y_x2)
print(f'Luong tinh: {H_y - H_y_x}')

