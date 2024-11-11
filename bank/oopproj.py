from bankacc import *

bala=Bankacc(1000,"Bala")
rag=Bankacc(2000,"Rag")
bala.getbalance()
rag.getbalance()
bala.deposit(2000)
rag.withdraw(1000)
bala.transfer(100,rag)

biju=Interestacc(2000,"biju")
biju.getbalance()
biju.deposit(100)
biju.transfer(350,bala)

bri=Savingacc(1000,"brian")
bri.getbalance()
bri.deposit(100)
bri.transfer(20230,rag)
bri.transfer(200,rag)

abi=Rd(10000,1)
ebi=joinrd(1000,1,"ebi")