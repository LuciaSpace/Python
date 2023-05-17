def func():
    print("안녕하세요")
    print("김정은입니다.")
func()

for i in range(3):
    func()

def func_add(a,b):
    return a+b
c=func_add(1,2)
print(c)

def func_mux(a,b):
    mux=a*b
    return mux
d=func_mux(2,3)
print(d)

def func_add_mux(a,b):
    add=a+b
    mux=a*b
    return add,mux
a,b=func_add_mux(1,3)
print(a,b)

_,d=func_add_mux(1,3)
print(d)