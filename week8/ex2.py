def printArguments(x,y,z):
    print("x=%d,y=%d,z=%d" % (x,y,z))
    sum = x+y+z
    print("x+y+z=%d" % sum)

printArguments(10,20,30)
printArguments(y=100,z=200,x=300)
printArguments(z=2000,y=1000,x=3000)