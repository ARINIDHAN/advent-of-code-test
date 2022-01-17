if __name__ == '__main__':
    file = open("day2.txt", "r")
    data = file.read().split('\n')

    Ph, Pv, GOAL = 0, 0, 0
    Ph=0    #position horizontal
    Pv=0    #position vertical
    GOAL=0
    print(data)

    for a in data:
        k,P = a.split(' ')
        P = int(P)
        if k == "forward":
            Ph += P
        elif k == "down":
            Pv += P
        elif k == "up":
            Pv -= P

    print("SOLUTION 1: ", Ph*Pv)
