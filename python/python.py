import threading as thr


def func():
    print("hello")
    
def func2():
    print("hi")
    
def func3():
    print("yaxshimisiz?")
    
t1 = thr.Thread(target=func)
t2 = thr.Thread(target=func2)
t3 = thr.Thread(target=func3)

t1.start()
t2.start()
t3.start()
    
    
    
qizil = input("toxtang! qizil yondi: ")
sariq = input("tayyorlaning! sariq yondi: ")
yashil = input("yurishingiz mumkin! yashil yondi: ")

