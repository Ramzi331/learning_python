spam = 0
count = 0
while True:
    filename = input("please inter file name:\n")
    try:
        fhandle = open(filename)
    except:
        print("wrong file name!")
        continue
    for line in fhandle:
        if line.startswith("X-DSPAM-Confidence"):
            start = line.find(":")
            spam += float(line[start+1:])
            count += 1
        else:
            continue
    print("average: ",spam/count)
    quit()