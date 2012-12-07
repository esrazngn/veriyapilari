from Stack import*
import math
#2 lik 8 lik 16 lık tabandan 10 luk tabana dönüşüm
"""
>>> donusum("0x11A")
onaltilik taban
282.0
>>> donusum("0b11")
ikilik taban
3.0
>>> donusum("011")
sekizlik taban
9.0
>>> donusum("11")
onluk taban
11
>>> 
"""
def donusum(String):
    s=Stack()
    a=[]
    j=0
    sonuc=0
    for i in String:
        a=a+[i]
    if a[0]== "0":
        if a[1]=="b":
            print "ikilik taban"
            for i in a[2:]:
                x=int(i)
                s.push(x)
            while not s.isEmpty():
                b=s.pop()
                sonuc=sonuc+b*math.pow(2,j)
                j+=1
        elif a[1]=="x":
            print "onaltilik taban"
            for i in a[2:]:
                s.push(i)
            
            while not s.isEmpty():
                b=s.pop()
                if b=="A":
                    sonuc=sonuc+10*math.pow(16,j)
                elif b=="B":
                    sonuc=sonuc+11*math.pow(16,j)
                elif b=="C":
                    sonuc=sonuc+12*math.pow(16,j)
                elif b=="D":
                    sonuc=sonuc+13*math.pow(16,j)
                elif b=="E":
                    sonuc=sonuc+14*math.pow(16,j)
                elif b=="F":
                    sonuc=sonuc+15*math.pow(16,j)
                else:
                    x=int(b)
                    sonuc=sonuc+x*math.pow(16,j)
                j+=1
        else:
            print"sekizlik taban"
            for i in a[1:]:
                x=int(i)
                s.push(x)
            while not s.isEmpty():
                b=s.pop()
                sonuc=sonuc+b*math.pow(8,j)
                j+=1
    elif a[0] !="0":
        print "onluk taban"
        sonuc =int(String)
    print "sonuc =", sonuc
