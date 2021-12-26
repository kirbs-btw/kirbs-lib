import time

def randomint(len):
    """
    creates a random integer by using the system time

    :param len: number of digits of the int
    :return: random integer
    """
    num = ""
    rand = time.time() * 100000
    randsrc = ""
    for j in range(1, 10):
        randsrc = randsrc + str(rand*j)[0:12]


    for i in range(1, len):
        num = num + str(randsrc)[i*3]

    return num

def randList(len, size):
    arr = []
    for i in range(size):
        arr.append(randomint(len))
    return arr

if __name__ == '__main__':
    print(randomint(5))
    #print(randList(10, 100000))