def someFunc(x, y, z):
    print("x is", x, "\ny is", y, "\nz is", z)

someFunc(1,2,3)
someFunc(y=2, z=3, x=1)
someFunc(y=3, x=2, z=1)

def showMsg(title, body="", prefix="INFO", suffix=".",sep=""):
    print(prefix,title,sep,body,suffix)

showMsg("File opened")
showMsg("File not opened", prefix="ERROR" )
showMsg("File missing", body="Insert Disk", suffix="Press return" )

showMsg("File opened", sep="-", suffix="Press return",)