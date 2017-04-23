import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

def distance(p1, p2):
    """
    Function calculates distance between two points. Note: p1 and p2 are given as numpy arrays so operations are executed elementwise allowing multidimensional points
    :param p1: point as np.array[]
    :param p2: point as np.array[]
    :return: distance 
    """
    dist = np.sqrt(np.sum(np.power(p1-p2, 2)))
    return dist

#Finding the mode (i.e. most commonly occuring element in a static sample) by hand
def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] =  1

    maxi = max(vote_counts.values())
    winners = [vote for vote, count in vote_counts.items() if count==maxi]
    return np.random.choice(winners)

# Finding the mode using mode function from SciPy
def majority_vote_short(votes):
    """
    Return the most common element i.e. the mode of input array
    ! If several elements occure with maximum count, the first one will allways be picked and returned
    :param votes: 
    :return: 
    """
    mode, count = ss.mstats.mode(votes)
    return mode

#search for k Neareast Neighbors
def find_nearest_neighbors(new_point, points, k=5):
    """
    Takes a (multidimensional) np.array of points and returns an array of k points with least distance to new point
    :param new_point: 1Darray of data coordinates (i.e. point) to be classified
    :param points: multidimensional np.array of "coordinates"
    :param k: number of neighbors to return
    :return: np.array with indices of k nearest neighbors of new point in points
    """
    distances = np.zeros(len(points))
    for i in range(len(distances)):
        distances[i] = distance(new_point, points[i])
    distance_sorted_indices = np.argsort(distances)
    k_nearest = distance_sorted_indices[:k]
    return k_nearest

# extend find_nearest_neighbors() with class prediction
def knn_predict(new_point, points, point_classes, k=5):
    """
    Find k nearest neighbors of a new point among given points, uses the majority_votes function to find the most common class among those neighbors and predicts the class of the new point accordingly
    :param new_point: 
    :param points: 
    :param point_classes: 
    :param k: 
    :return: 
    """
    k_nearest = find_nearest_neighbors(new_point, points, k)
    return majority_vote(point_classes[k_nearest])

def generate_synthetic_data(nr_obs=50):
    """Generate two sets of points with normal distributions(mean, std) with rvs(nr_of_rows, nr_of_columns)
    @:param: nr_obs Number of observations, i.e. points in each class"""
    cat1= ss.norm(0, 1).rvs((nr_obs, 2))
    cat2= ss.norm(1, 1).rvs((nr_obs, 2))
    #cat3= ss.norm(4, 3).rvs((nr_obs, 2))
    points = np.concatenate((cat1, cat2), axis = 0)
    outcomes = np.concatenate((np.repeat(0,nr_obs), np.repeat(1,nr_obs)))
    return (points, outcomes)

def make_prediction_grid(predictors, predictor_classes, limits, h, k):
    """
    Classify each point in a generated prediction grid according to provided predictor points and corresponding classes
    :param limits: four tuple (Int, Int, Int, Int) for (x_min, x_max, y_min, y_max) grid dimension
    :param predictors np.array of classified points
    :param predictor_classes np.array of classifications for predictor points
    :return: three-tuple (xx, yy, prediction grid), grid of predicted point classes and two arrays containing their x- and y-coordinates in the np.meshgrid
    """
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)
    #store the predicted classes {0,1} in prediction grid
    prediction_grid = np.zeros(xx.shape, dtype=int)
    #loop over the 1D-Datapoint array and predict their class, enumerate gives us the index locations of x and y in the respective vectors
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            #generate a point p with current x and y values
            p= np.array([x,y])
            prediction_grid[j,i]= knn_predict(p, predictors, predictor_classes, k)
    return (xx, yy, prediction_grid)


"""Example: enumerate()
    seasons = ["spring","summer","fall","winter"]
    list(enumerate(seasons)) => [(1, 'spring'),(2, 'summer'),(3, 'fall'),(4, 'winter')]
"""
def plot_prediction_grid (xx, yy, prediction_grid, filename, predictors, predictor_classes):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = predictor_classes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)
"""
#'testdataset'
points= np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2,],[3,3]])
p = np.array([2.5, 2])
p1 = np.array([1,1])
p2 = np.array([4,4])
point_classes=np.array([0,0,0,0,0,1,1,1,1])

#plot x- agains y-coordinates
plt.plot(points[:,0], points[:,1], "ro")
plt.plot(p[0], p[1], "bo")
plt.axis([0.5, 3.5, 0.5, 3.5])

#plot synthetic data
n = 50
(synpoints, outcomes) = generate_synthetic_data(n)
plt.figure()
#first category  in synpoints from 0 to n-1
plt.plot(synpoints[:n,0], synpoints[:n,1], "ro")
#second category from n to 2n -1
plt.plot(synpoints[n:(2*n),0], synpoints[n:(2*n),1], "s", markersize=7,
markeredgewidth=1,markeredgecolor='#b55f1a', markerfacecolor='None')
plt.plot(synpoints[(2*n):,0], synpoints[(2*n):,1], "g^")
plt.savefig('synData.pdf')
plt.show()
votes= [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,5]
print(knn_predict(p, points,point_classes, 3))
#print(majority_vote(votes), majority_vote_short(votes))

(synpoints, outcomes) = generate_synthetic_data(100)
k=10
filename= "knn_synth_10.pdf"
meshlimits = (-3, 4, -3, 4)
stepwidth = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(synpoints, outcomes, meshlimits, stepwidth, k)
plot_prediction_grid(xx, yy, prediction_grid, filename, synpoints, outcomes)
"""