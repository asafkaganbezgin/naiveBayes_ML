from question1 import predict
import math

# Constants
TOTAL_8MER = 493
TOTAL_AA = 20
TOTAL_SEQ = 8


def cleaveSeq(prob_0, prob_1, seq_train):

    # Variables to be updated
    prdtProb_0 = 0
    prdtProb_1 = 0
    highest_prob = 0
    lowest_prob = 1
    index_low = 0
    index_high = 0

    # Iterating over every single 8-mer sequence
    for i in range(TOTAL_8MER):
        # Sliding 8-mer window
        for j in range(TOTAL_SEQ):
            # Iterating over one-hot-encode
            for k in range(TOTAL_AA):
                # If the one-hot-encode is "1"
                if seq_train[i][k + (j * TOTAL_AA)] == "1":
                    # If the probability is 0 for the specific amino acid
                    if prob_0[j][k] == 0 or prob_1[j][k] == 0:
                        # Updating the lowest probability with label 0 and
                        # highest probability with label 1
                        if prob_0[j][k] < lowest_prob:
                            lowest_prob = prob_0[j][k]
                        if prob_1[j][k] > highest_prob:
                            highest_prob = prob_1[j][k]
                        # Adding the probability results
                        prdtProb_0 = prdtProb_0 + 0
                        prdtProb_1 = prdtProb_1 + 0
                    # If the probability is not 0, repeat similar operations as above
                    else:
                        if prob_0[j][k] < lowest_prob:
                            lowest_prob = prob_0[j][k]
                            index_low = i
                        if prob_1[j][k] > highest_prob:
                            highest_prob = prob_1[j][k]
                            index_high = i
                        prdtProb_0 = prdtProb_0 + math.log(prob_0[j][k])
                        prdtProb_1 = prdtProb_1 + math.log(prob_1[j][k])
                    break

        prdtProb_0 = 0
        prdtProb_1 = 0

    print("The lowest probability of label 0: " + str(lowest_prob + 1))
    print("The 8-mer with the lowest probability is the 8-mer on line " 
            + str(index_low) + " in the training dataset")
    print("The highest probability of label 1: " + str(highest_prob + 1))
    print("The 8-mer with the highest probability is the 8-mer on line " 
            + str(index_high) + " in the training dataset")
    print("NOTE: First line in the training dataset is 1 not 0" + 
            " according to the information given above")
