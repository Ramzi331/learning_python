total = 0
count = 0
while True:
    num = input("inter a number: ")
    if num == ("done"):
        print ("total:   ",total,"\ncount:   ",count,"\naverage: ",total/count,"\nDone!")
        quit()
    else:
        try:
            num = float(num)
        except:
            print("numbers only please!")
            continue
        total += num
        count += 1