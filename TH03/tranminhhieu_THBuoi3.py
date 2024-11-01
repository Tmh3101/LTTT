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

        return xeploai
        

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
        print(f'Sinh vien {student_list[i].hoTen} co MSSV la {student_list[i].mssv} voi diem trung binh la {student_list[i].diemTB} duoc xep loai la {student_list[i].rank()}')


def createStudent():
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
    
    return Student(hoTen, namSinh, queQuan, mssv, nganh, diemTB)

# Câu 5:
def cau05():
    student = createStudent()
    student.getInfo()

def printStudentListInfo(student_list):
    for i in range(0, len(student_list)):
        print('----------------------------------------------------------------------------------------------------------')
        print(f'\t\t\t\t\t\tSinh Vien {i + 1}')
        print('----------------------------------------------------------------------------------------------------------')
        print(f'Ho ten: {student_list[i].hoTen}')
        print(f'Nam sinh: {student_list[i].namSinh}')
        print(f'Que quan: {student_list[i].queQuan}')
        print(f'MSSV: {student_list[i].mssv}')
        print(f'Nganh hoc: {student_list[i].nganh}')
        print(f'Diem trung binh: {student_list[i].diemTB}')
        print(f'Xep loai: {student_list[i].rank()}')

def cau06():
    n = int(input('Nhap so luong sinh vien: '))
    student_list = []
    for i in range(0, n):
        print(f'Nhap thong tin cho sinh vien thu {i + 1}: ')
        student_list.append(createStudent())

    printStudentListInfo(student_list)


class Node():
    def __init__(self, probability, symbol, left=None, right=None):
        self.probability = probability
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''
    
def CalculateProbability(data):
    dict = {}
    for c in data:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1 

    return dict

the_codes = {}
def CalculateCodes(node, value = ''):
    # a huffman code for current node
    newValue = value + str(node.code)
    
    if (node.left):
        CalculateCodes(node.left, newValue)
    if (node.right):
        CalculateCodes(node.right, newValue)
    
    if (not node.left and not node.right):
        the_codes[node.symbol] = newValue

    return the_codes

""" A supporting function in order to get the encoded result """
def OutputEncoded(the_data, coding):
    encodingOutput = []
    for element in the_data:
        # print(coding[element], end='')
        encodingOutput.append(coding[element])
    
    the_string = ''.join([str(item) for item in encodingOutput])
    return the_string

""" A supporting function in order to calculate the space difference between compressed and non-compressed data """
def TotalGain(the_data, coding):
    # total bit space to store the data before compression
    beforeCompression = len(the_data) * 8
    afterCompression = 0
    the_symbols = coding.keys()
    
    for symbol in the_symbols:
        the_count = the_data.count(symbol)
        # calculating how many bit is required for that symbol in total
        afterCompression += the_count * len(coding[symbol])
    
    print("Space usage before compression (in bits):", beforeCompression)
    print("Space usage after compression (in bits):", afterCompression)

def HuffmanEncoding(the_data):
    symbolWithProbs = CalculateProbability(the_data)
    the_symbols = symbolWithProbs.keys()
    the_probabilities = symbolWithProbs.values()
    
    print("symbols: ", the_symbols)
    print("probabilities: ", the_probabilities)
    
    the_nodes = []
    
    # converting symbols and probabilities into huffman tree nodes
    for symbol in the_symbols:
        the_nodes.append(Node(symbolWithProbs.get(symbol), symbol))
    
    while len(the_nodes) > 1:
        # sorting all the nodes in ascending order based on their probability
        the_nodes = sorted(the_nodes, key=lambda x: x.probability)
        
        # picking two smallest nodes
        right = the_nodes[0]
        left = the_nodes[1]
        
        left.code = 0
        right.code = 1
        
        # combining the 2 smallest nodes to create new node
        newNode = Node(left.probability + right.probability, left.symbol + right.symbol, left, right)
        
        the_nodes.remove(left)
        the_nodes.remove(right)
        the_nodes.append(newNode)
    
    huffmanEncoding = CalculateCodes(the_nodes[0])
    print("symbols with codes: ", huffmanEncoding)
    TotalGain(the_data, huffmanEncoding)
    encodedOutput = OutputEncoded(the_data, huffmanEncoding)
    
    return encodedOutput, the_nodes[0]

def HuffmanDecoding(encodedData, huffmanTree):
    treeHead = huffmanTree
    decodedOutput = []
    
    for x in encodedData:
        if x == '1':
            huffmanTree = huffmanTree.right
        elif x == '0':
            huffmanTree = huffmanTree.left
        
        try:
            if huffmanTree.left.symbol == None and huffmanTree.right.symbol == None:
                pass
        except AttributeError:
            decodedOutput.append(huffmanTree.symbol)
            huffmanTree = treeHead
    
    string = ''.join([str(item) for item in decodedOutput])
    return string

the_data = 'AAAAAAABBCCCCCCDDDEEEEEEEEE'
output, node =  HuffmanEncoding(the_data)
print('Output:', output)
print('Root of huffman tree:', node.symbol)
print('===Deconding===')
data = HuffmanDecoding(output, node)
print(data)
