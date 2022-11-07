# 2) Explain overloading and overriding by writing a sample program
# Method overloading

# Overloading using Default Argument

def add(a =0 ,b = 0, c =0):
    result = a+ b+ c
    print(f'Addition is : {result}')
    
add()
add(10)
add(10, 20)

# By using conditional statement

def mul(a=None, b=None, c=None):
    if a ==None and b==None and c==None:
        print('No argument  pass')
    elif b==None and c==None:
        print(f'Multiplication is : {10*1}')
    elif c==None:
        print(f'Multiplication is : {a*b}')
    else:
        result = a* b*c
        print(f'Multiplication is : {result}')
        
        
# overriding -- 1 

class Calc:
    def add(self,a,b):
        print(a+b)
class AdcancedCalc(Calc):
    def add(self, *nums):
        tot = 0
        for i in nums:
            tot = tot + i
        print(tot)
ac = AdcancedCalc()
ac.add(1,2,3,4)


# overriding -- 2
class Parent:
    def m1(self, a,b):
        print('m1--parent', a,b)
class Child(Parent):
    def m1(self,a,b):
        super().m1(a,b)
        #Parent.m1(self,a,b)
        print('m1--child',a,b)

ch = Child()
ch.m1(10,20)