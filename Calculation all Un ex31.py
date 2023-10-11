n=int(input("type a number greater than 2 :"))
while n<2 :
    n=int(input("type a number greater than 2 :"))
Ui=0
Um=1
for i in range (2,n+1):
    Uf=Um+Ui
    print("U",i,"=",Uf)
    Ui=Um
    Um=Uf