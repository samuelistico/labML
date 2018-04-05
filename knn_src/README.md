-To run knn you need python 3.7 or greater

-This example uses the datasets: post-operative, cmc and covtype

-to change the dataset change the global variable dSet to 0, 1 or 2 accordingly

-We also use the K values of 1,3,5,7,9,30,45 and 60. You can modify these values in nn array

-The percentage of the training set is determined by a variable called split

A basic result will be like this:

Train set: 406708
Test set: 174304
k = 45
0. Predicted '2', Result '1'
1. Predicted '1', Result '1'
2. Predicted '2', Result '2'
3. Predicted '3', Result '3'
4. Predicted '2', Result '2'
5. Predicted '2', Result '2'
6. Predicted '1', Result '2'
7. Predicted '1', Result '1'
8. Predicted '1', Result '2'
Accuracy: 47.28506787330316%

Followed by the Avgerage of the number of times repeated. This number is determined in a for loop below the code 