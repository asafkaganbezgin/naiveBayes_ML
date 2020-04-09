import matplotlib.pyplot as plt


def plotAT():

    # Graphic data
    alpha_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    accuracy_1 = [94.5075, 94.69, 94.5075, 94.5075, 94.5075, 94.5075,
                  94.1287, 93.75, 93.5606, 92.9924, 92.8030]
    # Plotting the first line
    plt.plot(alpha_1, accuracy_1, label="All data")

    alpha_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    accuracy_2 = [42.9924, 48.2954, 24.8106, 18.75, 18.5606,
                  18.3712, 18.3712, 18.3712, 18.3712, 18.3712, 18.3712]
    # Plotting the second line
    plt.plot(alpha_2, accuracy_2, label="Only 75 data")

    # Naming the axis
    plt.xlabel("Alpha")
    plt.ylabel("Accuracy")

    # Title of the graph
    plt.title("Alpha vs. Accuracy Graphic")

    # Show legend on the plot
    plt.legend()

    # Show the plot
    plt.show()
