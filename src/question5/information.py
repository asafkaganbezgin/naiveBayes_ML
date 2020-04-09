import math
from decimal import Decimal

# Constants
TOTAL_8MER = 6062
LABEL = 160
FEATURES = 160
TOTAL_SEQ = 8
TOTAL_AA = 20
NUM_LABEL = 2


# Counting the occurrances of the indexes one by one with respect to the labels.
def countOccurrance(train_array):

    # Defining the rows and the columns of the count array.
    rows, columns = (NUM_LABEL, FEATURES)

    # Defining the array with "0" in all instances.
    count_array = [[0 for i in range(columns)] for j in range(rows)]

    # Counting the features and updating the count_array.
    # Iterate over all rows in training data.
    for i in range(TOTAL_8MER):
        # The operations if the label of the row is equal to "0".
        if train_array[i][LABEL] == "0":
            # Iterating over all features one by one.
            for j in range(FEATURES):
                # If the index is equal to "1" then increase the corresponding
                # index of the count_array.
                if train_array[i][j] == "1":
                    count_array[0][j] = count_array[0][j] + 1
        # The operations if the label of the row is equal to "1".
        if train_array[i][LABEL] == "1":
            # Iterating over all features one by one.
            for j in range(FEATURES):
                # If the index is equal to "1" then increase the corresponding
                # index of the count_array
                if train_array[i][j] == "1":
                    count_array[1][j] = count_array[1][j] + 1

    return count_array

# Calculating information for each feature.


def calculateInfo(count_array):

    # Information array to be returned by the function
    info_array = [0 for i in range(FEATURES)]

    # Filling the info_array
    for i in range(len(info_array)):
        # Calculating N11
        N_11 = count_array[1][i]
        # Calculating N10
        N_10 = count_array[0][i]
        # Calculating N01
        N_01 = 0
        for j in range(FEATURES):
            if j != i:
                N_01 = N_01 + count_array[1][j]
        # Calculating N00
        N_00 = 0
        for j in range(FEATURES):
            if j != i:
                N_00 = N_00 + count_array[0][j]
        # Calculating N
        N = N_00 + N_01 + N_10 + N_11
        # If the denominator gets 0, set the value to infinity
        if (N_11 + N_10) * (N_11 + N_01) == 0 or \
           (N_01 + N_00) * (N_01 + N_11) == 0 or \
           (N_10 + N_11) * (N_10 + N_00) == 0 or \
           (N_00 + N_01) * (N_00 + N_10) == 0:
            info_array[i] = math.inf
        # If the numerator gets 0, set the value to 0
        elif N_00 == 0 or N_01 == 0 or N_10 == 0 or N_11 == 0:
            info_array[i] = 0
        # If there is no value error, calculate the mutual information
        else:
            info_array[i] = (N_11 / N) * math.log(((N * N_11) / ((N_11 + N_10) * (N_11 + N_01))), 2) \
                + (N_01 / N) * math.log(((N * N_01) / ((N_01 + N_00) * (N_01 + N_11))), 2) \
                + (N_10 / N) * math.log(((N * N_10) / ((N_10 + N_11) * (N_10 + N_00))), 2) \
                + (N_00 / N) * math.log(((N * N_00) / ((N_00 + N_01) * (N_00 + N_10))), 2)

        N_00 = 0
        N_01 = 0
        N_10 = 0
        N_11 = 0
        N = 0

    return info_array
