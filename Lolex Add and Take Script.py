import time
startnum = int(input("Please enter your starting number."))
addortakenum = int(input("Please input the number to be added. If you wish to take a number please put a - and then the number you wish to be taken."))
endnum=int(input("Please enter your end number."))
waittime = int(input("How long do you wish to wait before each operation is performed?"))
if endnum>startnum:
 while endnum>startnum:
    print(startnum)
    if addortakenum<int(0):
        startnum = startnum-addortakenum
    if addortakenum>int(0):
        startnum = startnum+addortakenum
    time.sleep(waittime)
 if startnum ==endnum or startnum>endnum:
    print("The closest number to your target number was:",startnum)
    time.sleep (1)
elif startnum>endnum:
 while startnum>endnum:
    print (startnum)
    if addortakenum<0:
        startnum = startnum+addortakenum
    if addortakenum>0:
        startnum = startnum = startnum-addortakenum
    time.sleep (waittime)
 if startnum == endnum or startnum<endnum:
    print ("The closest number to your target end number was:",startnum)
    time.sleep (1)
