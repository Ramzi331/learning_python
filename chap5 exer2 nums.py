total = 0
count = 0
numlist = []

while True:
    num = input("inter a number: ")
    if num == ("done"):
        print ("total:   ",total,"\ncount:   ",count,"\nmin: ",min(numlist),"\nmax :",max(numlist),"\nDone!")
        quit()
    else:
        try:
            num = float(num)
        except:
            print("numbers only please!")
            continue
        total += num
        count += 1
        numlist.append(num)