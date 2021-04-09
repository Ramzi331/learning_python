def computegrade (sscore):
    try:
        score = float(sscore)
        if score > 1.0 or score < 0.0:
            print("bad score!")
        elif score <= 0.6:
            print("F")
        elif score <= 0.7:
            print("D")
        elif score <= 0.8:
            print("C")
        elif score <= 0.9:
            print("B")
        elif score <= 1.0:
            print("A")
    except:
        print("bad score!")

computegrade(99)
