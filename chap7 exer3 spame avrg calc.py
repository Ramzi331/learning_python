spam = 0
count = 0
filename = input("please inter file name:\n")
if filename == ("na na boo boo"):
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
else:
    try:
        fhandle = open(filename)
    except:
        print("wrong file name!")
        quit()
    for line in fhandle:
        if line.startswith("X-DSPAM-Confidence"):
            start = line.find(":")
            spam += float(line[start+1:])
            count += 1
    print("average: ",spam/count)