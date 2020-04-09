# import fileOp
import fileOp
from question1.model import naiveBayes
from question1 import predict
from question2 import encode
from question2 import cleave
from question3 import lowestHighest
from question4.model import naiveBayes_alpha
from question4 import predict_alpha
from question4 import drawPlot
from question5 import information

if __name__ == "__main__":

    run = True

    while(run):
        question = input(
            "\nEnter the name of the question you want to see the " +
            "solution of(Type \"exit\" to exit the program): ")
        if question != "question1" and question != "question2" and question != "question3" \
                and question != "question4" and question != "question5" \
                and question != "question6" and question != "exit":
            print("\nPlease enter \"question1\", \"question2\", \"question3\", " +
                  "\"question4\", \"question5\" or \"question6\"(\"exit\" to exit)")
        else:
            if question == "exit":
                run = False
            if question == "question1":
                # Loading the training data into a variable and processing by removing the commas.
                train_raw = None
                train_raw = fileOp.loadData(
                    "./dataset/raw/q2_train_set.txt", train_raw)
                fileOp.processData(
                    "./dataset/processed/q2_train_set.txt", train_raw)

                # Putting the processed training data into a two dimensional array
                train_array = fileOp.copyToArr(
                    "./dataset/processed/q2_train_set.txt")

                # training the model
                prediction_table = naiveBayes.trainModel(train_array)

                # Loading the test data into a variable and processing by removing the commas.
                test_raw = None
                test_raw = fileOp.loadData(
                    "./dataset/raw/q2_test_set.txt", test_raw)
                fileOp.processData(
                    "./dataset/processed/q2_test_set.txt", test_raw)

                # Putting the processed test data into a two dimensional array
                test_array = fileOp.copyToArr(
                    "./dataset/processed/q2_test_set.txt")

                # Give apply the model on the test data and print the results.
                predict.predictEntries(
                    prediction_table[0], prediction_table[1], test_array, prediction_table[2], prediction_table[3])

            if question == "question2":
                # Loading the training data into a variable and processing by removing the commas.
                train_raw = None
                train_raw = fileOp.loadData(
                    "./dataset/raw/q2_train_set.txt", train_raw)
                fileOp.processData(
                    "./dataset/processed/q2_train_set.txt", train_raw)

                # Putting the processed training data into a two dimensional array
                train_array = fileOp.copyToArr(
                    "./dataset/processed/q2_train_set.txt")

                # training the model
                prediction_table = naiveBayes.trainModel(train_array)
                # Loading the raw sequence data.
                seq_raw = None
                seq_raw = fileOp.loadData(
                    "./dataset/raw/q2_gag_sequence.txt", seq_raw)

                # Copying the data to a one dimensional array.
                seq_array = fileOp.seqToArr(seq_raw)

                # Creating one-hot-encoded dataset from the given one dimensional seq array.
                encode.oneHotEncode(seq_array)

                # Storing the seq data in txt file inside a two dimensional array
                seq_train = fileOp.copySeqToArr(
                    "./dataset/processed/q2_gag_sequence_train.txt")

                # Cleaving the protein sequence
                cleave.cleaveSeq(
                    prediction_table[0], prediction_table[1], seq_train)

            if question == "question3":
                # Loading the training data into a variable and processing by removing the commas.
                train_raw = None
                train_raw = fileOp.loadData(
                    "./dataset/raw/q2_train_set.txt", train_raw)
                fileOp.processData(
                    "./dataset/processed/q2_train_set.txt", train_raw)

                # Putting the processed training data into a two dimensional array
                train_array = fileOp.copyToArr(
                    "./dataset/processed/q2_train_set.txt")

                # training the model
                prediction_table = naiveBayes.trainModel(train_array)
                # Loading the raw sequence data.
                seq_raw = None
                seq_raw = fileOp.loadData(
                    "./dataset/raw/q2_gag_sequence.txt", seq_raw)

                # Copying the data to a one dimensional array.
                seq_array = fileOp.seqToArr(seq_raw)

                # Creating one-hot-encoded dataset from the given one dimensional seq array.
                encode.oneHotEncode(seq_array)

                # Storing the seq data in txt file inside a two dimensional array
                seq_train = fileOp.copySeqToArr(
                    "./dataset/processed/q2_gag_sequence_train.txt")

                # Cleaving the protein sequence
                lowestHighest.cleaveSeq(
                    prediction_table[0], prediction_table[1], seq_train)

            if question == "question4":
                # Loading the training data into a variable and processing by removing the commas.
                train_raw = None
                train_raw = fileOp.loadData(
                    "./dataset/raw/q2_train_set.txt", train_raw)
                fileOp.processData(
                    "./dataset/processed/q2_train_set.txt", train_raw)

                # Putting the processed training data into a two dimensional array
                train_array = fileOp.copyToArr(
                    "./dataset/processed/q2_train_set.txt")

                # training the model
                prediction_table_alpha = naiveBayes_alpha.trainModel(
                    train_array)

                # Loading the test data into a variable and processing by removing the commas.
                test_raw = None
                test_raw = fileOp.loadData(
                    "./dataset/raw/q2_test_set.txt", test_raw)
                fileOp.processData(
                    "./dataset/processed/q2_test_set.txt", test_raw)

                # Putting the processed test data into a two dimensional array
                test_array = fileOp.copyToArr(
                    "./dataset/processed/q2_test_set.txt")

                # Give apply the model on the test data and print the results.
                predict_alpha.predictEntries(
                    prediction_table_alpha[0], prediction_table_alpha[1], test_array,
                    prediction_table_alpha[2], prediction_table_alpha[3])

                drawPlot.plotAT()

            if question == "question5":
                # Loading the training data into a variable and processing by removing the commas.
                train_raw = None
                train_raw = fileOp.loadData(
                    "./dataset/raw/q2_train_set.txt", train_raw)
                fileOp.processData(
                    "./dataset/processed/q2_train_set.txt", train_raw)
                # Putting the processed training data into a two dimensional array
                train_array = fileOp.copyToArr(
                    "./dataset/processed/q2_train_set.txt")
                # Counting the occurrance of the features with respect to the labels
                count_array = information.countOccurrance(train_array)
                # Calculating the information of the indices
                info_array = information.calculateInfo(count_array)
                # Sorting info array in descending order
                info_array.sort(reverse=True)
                # Printing the mutual information in descending order.
                for i in range(len(info_array)):
                    print(info_array[i])

            if question == "question6":
                print(".. to be done")

    print()
