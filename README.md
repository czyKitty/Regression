# Regression

reg.py&nbsp;
Description:This program takes 3 command line arguements: name of the training data file, name of the validation data file, and the degree of polynomial. The program would do regression with given degress polynomial. It would generate the plot with training data(grey), validation date(green), and regression line(blue). The polynomial function and average loss value would be print on the screen.&nbsp;
To run:python3 reg.py <trainFile> <validationFile> <degree>

evaluate.py&nbsp;
Description:This program takes 2 command line arguements: name of the data file and the degree of polynomial. The program would use the original data to generate 10 pair of training and validation data for 1-fold validation. It would then use reg.py to plot each data with given degree polynomial.&nbsp;
To run:python3 evaluate.py <dataFile> <degree>
