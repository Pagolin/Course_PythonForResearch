from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import WeekThree.Classification as my_cl
import  numpy as np

#iris is an example dataset for classification of 150 iris flowers into three species
iris = datasets.load_iris()
predictors = iris.data[:, 0:2] # all rows, but only columns 0 and 1

outcomes = iris.target
#plot column 0 against column 1
plt.plot(predictors[outcomes==0][:, 0], predictors[outcomes==0][:, 1], "ro")
plt.plot(predictors[outcomes==1][:, 0], predictors[outcomes==0][:, 1], "go")
plt.plot(predictors[outcomes==2][:, 0], predictors[outcomes==0][:, 1], "bo")

plt.savefig("iris.pdf")

# Classify with handmade function
k=5; filename= "iris_grid.pdf"; meshlimits = (4, 8, 1.5, 4.5); stepwidth = 0.1
(xx, yy, prediction_grid) = my_cl.make_prediction_grid(predictors, outcomes, meshlimits, stepwidth, k)
my_cl.plot_prediction_grid(xx, yy, prediction_grid, filename, predictors, outcomes)

#Classifier from sklearn
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(predictors, outcomes) # fit the model using (X, y) as training data and target values, comparable to points and classes in examples before
sk_predictions = knn.predict(predictors)
my_predictions= np.array([my_cl.knn_predict(p, predictors, outcomes, 5) for p in predictors])
#sk_predictions == my_predictions yields an array of boolean values, np. mean turns them to 1 and 0
percent_equal= 100* np.mean(sk_predictions == my_predictions)
print(percent_equal)