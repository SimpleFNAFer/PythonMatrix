def Summatr(a, b):
	cn = []
	s = []
	for i in range(len(a)):
		for j in range(len(a[i])):
			s.append(int(int(a[i][j])+int(b[i][j])))
		cn.append(s)
		s = []
			
	return cn
	
def Mnmatr(a, b):
	cn = []
	s = []
	for i in range(len(a)):
		for j in range(len(a[i])):
			s.append(int(int(a[i][j])*int(b[i][j])))
		cn.append(s)
		s = []
			
	return cn
	
def Vichmatr(a, b):
	cn = []
	s = []
	for i in range(len(a)):
		for j in range(len(a[i])):
			s.append(int(int(a[i][j])-int(b[i][j])))
		cn.append(s)
		s = []
			
	return cn

ai, aj = input('Введите размерность матриц\n').split(' ')
ai = int(ai)
aj = int(aj)

A = []
B = []
C = []

print('Введите матрицу А')
for i in range(0, ai):
	s = input().split(' ')
	A.append(s)

print('Введите матрицу В')		
for i in range(0, ai):
	s = input().split(' ')
	B.append(s)
	
e = input('Выберите + или * или -\n')
if (e == '*'):
	C = Mnmatr(A,B)
if (e == '+'):
	C = Summatr(A,B)
if (e == '-'):
	C = Vichmatr(A,B)
	
for i in range(len(C)):
	s = ''
	for j in range(len(C[i])):
		s += str(C[i][j]) + ' '
	print(s)


