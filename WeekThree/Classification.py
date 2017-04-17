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
    points = np.concatenate((cat1, cat2), axis = 0)
    outcomes = np.concatenate((np.repeat(0,nr_obs), np.repeat(1,nr_obs)))
    return (points, outcomes)




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
n = 20
(synpoints, outcomes) = generate_synthetic_data(n)
plt.figure()
#first category  in synpoints from 0 to n-1
plt.plot(synpoints[:n,0], synpoints[:n,1], "ro")
#second category from n to 2n -1
plt.plot(synpoints[n:,0], synpoints[n:,1], "bo")
plt.savefig('synData.pdf')

votes= [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,5]
print(knn_predict(p, points,point_classes, 3))
#print(majority_vote(votes), majority_vote_short(votes))
