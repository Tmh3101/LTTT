# Tran Minh Hieu - B2207521

# Câu 1:
class Human:
    def __init__(self, hoTen, namSinh, queQuan, ngheNghiep):
        self.hoTen = hoTen
        self.namSinh = namSinh
        self.queQuan = queQuan
        self.ngheNghiep = ngheNghiep

    def live(self, noicutru):
        print(f'{self.hoTen} dang song o {noicutru}')

    def work(self, diachicoquan):
        print(f'{self.hoTen} dang lam {self.ngheNghiep} tai {diachicoquan}')

# Câu 2:
def cau02():
    n = int(input('Nhap so luong nguoi: '))

    human_list = []
    for i in range(0, n):
        hoTen = input(f'Nhap ho ten nguoi thu {i + 1}: ')
        namSinh = int(input(f'Nhap nam sinh nguoi thu {i + 1}: '))
        queQuan = input(f'Nhap que quan nguoi thu {i + 1}: ')
        ngheNghiep = input(f'Nhap vao nghe nghiep nguoi thu {i + 1}: ')
        human_list.append(Human(hoTen, namSinh, queQuan, ngheNghiep))

    for i in range(0, len(human_list)):
        diachicoquan = input(f'Nhap vao dia chi co quan cua {human_list[i].hoTen}: ')
        human_list[i].work(diachicoquan)

# Câu 3:
class Student(Human):
    def __init__(self, hoTen, namSinh, queQuan, mssv, nganh, diemTB):
        super().__init__(hoTen, namSinh, queQuan, 'student')
        self.mssv = mssv
        self.nganh = nganh
        self.diemTB = diemTB

    def getInfo(self):
        print('Ten:', self.hoTen)
        print('Nam sinh:', self.namSinh)
        print('Que quan:', self.queQuan)
        print('MSSV:', self.mssv)
        print('Nganh:', self.nganh)
        print('Diem trung binh:', self.diemTB)

    def study(self, lop):
        print(f'sinh vien {self.hoTen} co MSSV la {self.mssv} thuoc nganh {self.nganh} dang hoc tai phong hoc {lop}')
    
    def rank(self):
        xeploai = ''
        if self.diemTB < 4:
            xeploai = 'Loai Yeu'
        elif 4 <= self.diemTB < 6:
            xeploai = 'Loai Trung binh'
        elif 6 <= self.diemTB < 8:
            xeploai = 'Loai Kha'
        else:
            xeploai = 'Loai Gioi'
        print(f'Sinh vien {self.hoTen} co MSSV la {self.mssv} voi diem trung binh la {self.diemTB} duoc xep loai la {xeploai}')

# Câu 4;
def cau04():
    student_list = []
    for i in range(0, 2):
        print(f'Nhap thong tin sinh vien thu {i + 1}:')
        hoTen = input('Nhap ten: ')
        namSinh = int(input('Nhap nam sinh: '))
        queQuan = input('Nhap que quan: ')
        mssv = input('Nhap MSSV: ')
        nganh = input('Nhap nganh: ')
        diemTB = float(input('Nhap diem trung binh: '))
        student_list.append(Student(hoTen, namSinh, queQuan, mssv, nganh, diemTB))

    for i in range(0, len(student_list)):
        student_list[i].getInfo()
        student_list[i].rank()

# Câu 5:
def cau05():
    hoTen = input('Nhap ho ten: ')
    while len(hoTen) > 25:
        hoTen = input('Ho ten khong vuot qua 25 ky tu!, nhap lai: ')
    
    namSinh = input('Nhap nam sinh: ')
    while not namSinh.isdigit() or len(namSinh) != 4:
        namSinh = input('Nam sinh phai co 4 chu so, nhap lai: ')

    queQuan = input('Nhap que quan: ')
    while len(queQuan) > 50:
        queQuan = input('Que quan khong vuot qua 50 ky tu !, nhap lai: ')
    
    mssv = input('Nhap MSSV: ')
    while not mssv.isdigit() or len(mssv) > 5:
        if len(mssv) > 5:
            mssv = input('MSSV khong qua 5 ky tu !, nhap lai: ')
        else: mssv = input('MSSV chi chua cac ky tu so !, nhap lai: ')

    nganh = input('Nhap nganh: ')
    while len(nganh) > 40:
        nganh = input('Nganh hoc khong vuot qua 40 ky tu !, nhap lai: ')

    diemTB = float(input('Nhap diem trung binh: '))
    while not 0 <= diemTB <= 10:
        diemTB = float(input('Diem trung binh khong hop le (0 <= DTB <= 10), nhap lai: '))
    
    student = Student(hoTen, namSinh, queQuan, mssv, nganh, diemTB)
    student.getInfo()


cau05()


