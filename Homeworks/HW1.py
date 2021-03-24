#HOMEWORK 1 - Selman Dedeakayoğulları

#1) How would you define Machine Learning?

# In my opinion, Machine Learning is the way of solving the problems which we encountered with some of algorithms that our machine can understand.

#2) What are the differences between Supervised and Unsupervised Learning? Specify example 3 algorithms for each of these.

# Basically, the difference is the "training data". In Supervised Learning there is a data to train our algorithm which Unsupervised has not.

# Supervised Examples: Hand-Writing Detection, Object Detection, Prediction Algorithms

# Unsupervised Examples: Sex Detection, Race Detection (eg. German, Turkish), Customer Segmentations

#3) What are the test and validation set, and why would you want to use them?

# Test dataset is the data we are using to test our final machine learning model. Validation dataset is the data we are using to determine which model is the best for our goal and we are using it while tuning our hyperparameters.
# If we don't use them our model may have high incorrect prediction rate.

#5) How you can explore continuous and discrete variables?

# Continuous variables are measurable. We can show them with line graphs
# Discrete variables are countable. We can show them with scatter graphs

#6) Analyse the plot given below. (What is the plot and variable type, check the distribution and make comment about how you can preprocess it.)

# Our plot is histogram. Our variable type is continuous.
# There is some zeros in graph and there may be some missing values in the dataset. 
# We should assign the missing values to our median.
# There is some anomalies in between 0 and 1. Our data may be an imbalanced data , there may be some duplicated values in dataset or some outliers.
