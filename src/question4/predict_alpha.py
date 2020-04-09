import math
from .model import naiveBayes_alpha

# Constants
TOTAL_8MER = 528
LABEL = 160
TOTAL_AA = 20
TOTAL_SEQ = 8


# Predicting the labels of the test data and calculating the success rate
# by comparing the actual labels and predicted ones.
def predictEntries(prob_0, prob_1, test_array, prb_total_0, prb_total_1):

    prdtProb_0 = 0
    prdtProb_1 = 0
    guess = ""
    correct = 0

    for i in range(TOTAL_8MER):
        actualLabel = test_array[i][LABEL]
        for j in range(TOTAL_SEQ):
            for k in range(TOTAL_AA):
                if test_array[i][k + (j * TOTAL_AA)] == "1":
                    if prob_0[j][k] == 0 or prob_1[j][k] == 0:
                        prdtProb_0 = prdtProb_0 + 0
                        prdtProb_1 = prdtProb_1 + 0
                    else:
                        prdtProb_0 = prdtProb_0 + math.log(prob_0[j][k])
                        prdtProb_1 = prdtProb_1 + math.log(prob_1[j][k])
                    break
        if prdtProb_0 + math.log(prb_total_0) > prdtProb_1 + math.log(prb_total_1):
            guess = "0"
            if guess == actualLabel:
                correct = correct + 1
            print("Predicted " + guess + " and actual label is " + actualLabel)
        elif prdtProb_0 + math.log(prb_total_0) < prdtProb_1 + math.log(prb_total_1):
            guess = "1"
            if guess == actualLabel:
                correct = correct + 1
            print("Predicted " + guess + " and actual label is " + actualLabel)

        prdtProb_0 = 0
        prdtProb_1 = 0

    print("\nThe accurracy rate is: %" + str(correct / TOTAL_8MER * 100))
