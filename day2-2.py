if __name__ == '__main__':
    file = open("day2-2.txt", "r")
    data = file.read().split('\n')

    h0=0    #position horizontal
    v0=0    #position vertical
    GOAL=0
    print(data)
    for r in data :
        k, P = r.split(' ')
        P = int(P)
        if k == "forward":
            h0 += P
            v0 += P * GOAL
        elif k == "down":
            GOAL += P
        elif k == "up":
            GOAL -= P
        print("Réponse 2: ", h0 * v0)