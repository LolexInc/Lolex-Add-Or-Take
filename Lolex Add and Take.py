import time
print("Welcome to Lolex Add and Take version 1.1.")
startnum = float(input("Please enter your starting number."))
addortakenum = float(input("Please input the number to be added. If you wish to take a number please put a - and then the number you wish to be taken."))
endnum = float(input("Please enter your end number."))
waittime = float(input("How long do you wish to wait before each operation is performed?"))
while addortakenum == 0:
    addortakenum = float(input("0 for an add or take number is illegal. Please enter a legal number."))
while startnum == endnum:
    startnum = float(input("Your start number equals your end number.Please enter a new start number."))
    endnum = float(input("Please enter a new end number."))
while waittime < 0 or waittime > 4194304:
    waittime = float(input("Please enter a valid wait time. Less than 0 or bigger than 4194304 seconds is invalid."))
if endnum>startnum:
 while endnum>startnum:
    print(startnum)
    if addortakenum<0:
        startnum = startnum-addortakenum
    if addortakenum>0:
        startnum = startnum+addortakenum
    time.sleep(waittime)
 if startnum == endnum or startnum>endnum:
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
