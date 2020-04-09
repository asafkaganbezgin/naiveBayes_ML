# Opening the raw file and storing in a variable
def loadData(path, pointerName):

    try:
        fp = open(path, "r")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        pointerName = fp.read()
    finally:
        fp.close()

    return pointerName


# Creating a processed data file
def processData(path, rawPointer):

    try:
        fp = open(path, "w")
    except Exception as e:
        print(e)
    else:
        for line in rawPointer:
            if line != ",":
                fp.write(line)
    finally:
        fp.close()


# Copying txt into an array
def copyToArr(path):

    rows, columns = (6062, 161)
    arr = [[-1 for i in range(columns)] for j in range(rows)]
    try:
        fp = open(path, "r")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        file = fp.read()
        row, col = 0, 0
        for index in file:
            if index != "\n":
                arr[row][col] = index
                col = col + 1
            if index == "\n":
                row = row + 1
                col = 0
    finally:
        fp.close()

    return arr


# Creating a one dimensional array which holds the information in gag secuence data
def seqToArr(seq_pointer):

    array = []
    for index in seq_pointer:
        array.append(index)
    return array


# Copying the sequence txt data(493x160) in to a two dimensional array
def copySeqToArr(path):

    rows, columns = (493, 160)
    arr = [[-1 for i in range(columns)] for j in range(rows)]
    try:
        fp = open(path, "r")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        file = fp.read()
        row, col = 0, 0
        for index in file:
            if index != "\n":
                arr[row][col] = index
                col = col + 1
            if index == "\n":
                row = row + 1
                col = 0
    finally:
        fp.close()

    return arr
