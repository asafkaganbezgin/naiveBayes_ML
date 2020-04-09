# Constants
TOTAL_8MER = 6062
LABEL = 160
TOTAL_SEQ = 8
TOTAL_AA = 20
ALPHA = 0


# training the model
def trainModel(train_array):

    # Creating probability tables.
    rows, columns = (TOTAL_SEQ, TOTAL_AA)
    prob_0 = [[0 for i in range(columns)] for j in range(rows)]
    prob_1 = [[0 for i in range(columns)] for j in range(rows)]

    # Finding the number of instances with label 0.
    NUM_LAB_0 = 0
    for i in range(TOTAL_8MER):
        if train_array[i][LABEL] == "0":
            NUM_LAB_0 = NUM_LAB_0 + 1

    # Finding the number of instances with label 1.
    NUM_LAB_1 = 0
    for i in range(TOTAL_8MER):
        if train_array[i][LABEL] == "1":
            NUM_LAB_1 = NUM_LAB_1 + 1

    # Estimating the probability that any particular 8-mer will belong to class 0.
    PI_Y_0 = NUM_LAB_0 / TOTAL_8MER
    # Estimating the probability that any particular 8-mer will belong to class 1.
    PI_Y_1 = NUM_LAB_1 / TOTAL_8MER

    # Calculating the probability of every amino acid in each sequence with label 0.
    # Probability table of entries with label 0
    for i in range(TOTAL_8MER):
        if train_array[i][LABEL] == "0":
            for j in range(TOTAL_SEQ):
                for k in range(TOTAL_AA):
                    if train_array[i][k + (j * TOTAL_AA)] == "1":
                        if prob_0[j][k] == 0:
                            prob_0[j][k] = (
                                prob_0[j][k] + 1) * (1 / (NUM_LAB_0 + 2 * ALPHA))
                        else:
                            prob_0[j][k] = prob_0[j][k] + \
                                (1 / (NUM_LAB_0 + 2 * ALPHA))
        elif train_array[i][LABEL] == "1":
            for j in range(TOTAL_SEQ):
                for k in range(TOTAL_AA):
                    if train_array[i][k + (j * TOTAL_AA)] == "1":
                        if prob_1[j][k] == 0:
                            prob_1[j][k] = (
                                prob_1[j][k] + 1) * (1 / (NUM_LAB_1 + 2 * ALPHA))
                        else:
                            prob_1[j][k] = prob_1[j][k] + \
                                (1 / (NUM_LAB_1 + 2 * ALPHA))

    # Adding alpha value
    for i in range(TOTAL_SEQ):
        for j in range(TOTAL_AA):
            prob_0[i][j] = prob_0[i][j] + (ALPHA / (NUM_LAB_0 + 2 * ALPHA))

    for i in range(TOTAL_SEQ):
        for j in range(TOTAL_AA):
            prob_1[i][j] = prob_1[i][j] + (ALPHA / (NUM_LAB_1 + 2 * ALPHA))

    return prob_0, prob_1, PI_Y_0, PI_Y_1
