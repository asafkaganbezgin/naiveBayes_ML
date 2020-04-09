from question1 import predict
import math

# Constants
TOTAL_8MER = 493
TOTAL_AA = 20
TOTAL_SEQ = 8


def cleaveSeq(prob_0, prob_1, seq_train):

    # variables to be updated
    prdtProb_0 = 0
    prdtProb_1 = 0
    guess = ""

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
                        # Adding the probability results
                        prdtProb_0 = prdtProb_0 + 0
                        prdtProb_1 = prdtProb_1 + 0
                    # If the probability is not 0, repeat similar operations as above
                    else:
                        prdtProb_0 = prdtProb_0 + math.log(prob_0[j][k])
                        prdtProb_1 = prdtProb_1 + math.log(prob_1[j][k])
                    break
        # Labeling decisions and updating the cleavage points
        if prdtProb_0 > prdtProb_1:
            pass
        elif prdtProb_0 < prdtProb_1:
            cleave_index = i
            guess = guess + str(int((cleave_index + cleave_index + 7) / 2 - 0.5)) + \
                "-" + str(int((cleave_index + cleave_index + 7) / 2 + 0.5)) + ", "

        prdtProb_0 = 0
        prdtProb_1 = 0

    print(guess[:-2])
