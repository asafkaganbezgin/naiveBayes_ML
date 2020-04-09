# Important Notes

For question 4, the results could be observed by changing global constants on top of the files. Specifically;

If the observer wants to examine the results with respect to the alpha value, than he/she should change the **ALPHA** value in file _question4/model/naiveBayes_alpha.py_.

>       ALPHA = 0

Likewise, the total number of training data instances could be changed so that how much training instances the model is going to be trained on could be adjusted.

>       TOTAL_8MER = 6062

For plotting graphs, go to _question4/drawPlot.py_. Initially the function _plotAT()_ plots the two cases where the numbers of the data instances used to train model is different. However, if the observer wants to see only one lot at a time, you can simply comment out the part where you draw the other line respectively.

>       plt.plot(alpha_1, accuracy_1, label="All data")
>
>       plt.plot(alpha_2, accuracy_2, label="Only 75 data")
