class Student:
	name=""
	age=0
	marks=[]

	def __init__(self,x,y,l):
		self.name=x
		self.age=y
		self.marks=l

	def accept(self):
		self.name=input("Enter Name: ")
		self.age=input("Enter Age: ")
		print("Enter Marks: ")
		l=input()
		l=l.split()
		x=[]
		for i in range(len(l)):
			x.append(int(l[i]))
		self.marks=x

	def display(self):
		print(self.name)
		print(self.age)
		print(self.marks)

s1=Student('X',10,[0,0,0])
s1.accept()
s1.display()

s2=Student('Y',10,[0,0,0])
s2.accept()
s2.display()
