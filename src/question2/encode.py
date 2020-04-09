# Constants
TOTAL_AA = 160
NUM_ENCODE_AA = 20


# Return constants in switch
def selectAA(argument):
    switch = {
        "g": 0,
        "p": 1,
        "a": 2,
        "v": 3,
        "l": 4,
        "i": 5,
        "m": 6,
        "c": 7,
        "f": 8,
        "y": 9,
        "w": 10,
        "h": 11,
        "k": 12,
        "r": 13,
        "q": 14,
        "n": 15,
        "e": 16,
        "d": 17,
        "s": 18,
        "t": 19
    }
    return switch.get(argument, "Invalid amino acid")


# Creating one-hot-encoded dataset from the one dimensional gag sequence array
def oneHotEncode(seq_array):

    try:
        fp = open("./dataset/processed/q2_gag_sequence_train.txt", "w+")
    except Exception as e:
        print(e)
    else:
        for i in range(len(seq_array) - 7):
            for j in range(8):
                for k in range(selectAA(seq_array[j + i])):
                    fp.write("0")
                fp.write("1")
                if selectAA(seq_array[j + i]) <= 19:
                    for k in range(19 - selectAA(seq_array[j + i])):
                        fp.write("0")
            fp.write("\n")
    finally:
        fp.close()
