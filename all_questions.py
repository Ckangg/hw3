# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "In the single linkage method, the outlier point will have limitation influence. But in k-means clustering, the outlier point will influence the centroids"

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "because the first centroids are selected randomly for k-means, but the agglometrative hierarchical clustering will do a deterministic process, so it will get the same results "

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "with the number of data points increasing, the proximity matrix will be complicated and it will spend more time to calculate it, so agglomerative hierarchical clustering will be slower "

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "the centroid will be the average value of all the points in a cluster, the sse maybe decrease, because the points will be assigned more suitable, but there maybe some special case. "

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "sse is the total variance of in the cluster, so if sse is smaller, the points in the cluster will be more concentrated "

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "the bss means the separation between different clusters, the bss increase means that the different clusters are more far away form each other"

    # type: bool (True/False)
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "the sse is for the data points in a cluster, the ssb is for the centroids and the total average value of the whole data"

    # type: bool (True/False)
    answers["(h)"] = False

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "because the centroids are selected randomly, so at first the sse+bss may be larger, but with the step goes on, the sse+bss will finally be constant "

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "the cohesion increases means the data points in a cluster become more closer and more concentrated, but the centroids will not be faraway from each other "

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "at first the two centroid will collect the points in the two circles as clusters, because they are faraway form each other, it can think that they are the two separate system to get the results. So the centroid will be the midle point of each circle"

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "it is hard for k-means method to cluster this shape points, so as a result it maybe two centroids, one of them will in the upper part of the whole plot, another will in the lower part and each cluster will contain two shaded regions"

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4*R**2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] ="4*a**2+4*b**2+4*R**2"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "5*R**2"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 0

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "because A and B only have 100points, smaller than C, in order to find the min sse, the centroid will going to C, but the centroids are in the B firstly, so B will get a centroid"

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Because there is a centroid in the A at first, so it will has a centroid finally, because the c have larger datapoints, so there will be a centroid move to C, another will still in B"

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "the first centroid will move to the midle of the two circle, because they have the same number of points, because C have a large number of points, so the two centroids will stay in C and separate it into two part."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set({"Group A", "Group B"})

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "single linkage is to find the minimum of two points in different group. So I choose A and B"

    # type: set
    answers["(b)"] = set({"Group A", "Group C"})

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "this method is to find the maximum distance of two points in different group, so I choose A and C"

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set({'BCEFIJLM'})

    # type: set
    answers["(a) boundary"] = set({'DG'})

    # type: set
    answers["(a) noise"] = set({'AH'})

    # type: set
    answers["(b) cluster 1"] = set({'BCDEFG'})

    # type: set
    answers["(b) cluster 2"] = set({'JLIM'})

    # type: set
    answers["(b) cluster 3"] = set({'None'})

    # type: set
    answers["(b) cluster 4"] = set({'None'})

    # type: set
    answers["(c)-a core"] = set({'BCDEFGIJLM'})

    # type: set
    answers["(c)-a boundary"] = set({'AH'})

    # type: set
    answers["(c)-a noise"] = set({'None'})

    # type: set
    answers["(c)-b cluster 1"] = set({'ABCDEFG'})

    # type: set
    answers["(c)-b cluster 2"] = set({'HIJLM'})

    # type: set
    answers["(c)-b cluster 3"] = set({'None'})

    # type: set
    answers["(c)-b cluster 4"] = set({'None'})

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "cluster4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "the cluster4 has the most average distribution"

    # type: string
    answers["(b)"] = "cluster1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "the cluster1 almost made by water, so the entropy will be low"

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "the color blocks on the diag are purified, it means that the points in the clusters are highly converged"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "all the points of different clusters are converged to the centroids, so the color blocks of the matrix plots should be purified"

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "there are two color blocks on diag is not purified, it means that there will be points in two clusters are not highly converged "

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "because the color blocks are not the same color or similar color, it means that the distances are obvious different values"

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "there are two color blocks on diag is not purified, it means that there will be points in two clusters are not highly converged "

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "there are two color blocks are the similar color, it means that there will be the same distance for two clusters."

    # type: string
    answers["(b) Row 1"] = "A"

    # type: string
    answers["(b) Row 2"] = "B"

    # type: string
    answers["(b) Row 3"] = "C"

    # type: string
    answers["(b) Row 4"] = "D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "the first color block and the fourth color block are unpurified, so it should be the A  which the points are not converged to centroid"

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "the second color block of the colum1 means that this cluster is nearbt the row1, and B is more converged than C which means that the (2,3) color block should be more purified.so it is B"

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "the third color block of the colum1 means that this cluster is as the midle distance of A, so it is C "

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "the first color block and the fourth color block are unpurified, so it should be the D which the points are not converged to centroid"

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['hierarchical','overlapping','complete']

    # type: list
    answers["(b)"] = ['partitional','exclusive','complete']

    # type: list
    answers["(c)"] = ['partitional','exclusive','incomplete']

    # type: list
    answers["(d)"] = ['hierarchical','overlapping','incomplete']

    # type: list
    answers["(e)"] = ['partitional','exclusive','complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "one student has only one letter, and every one will get the grade."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "Yes"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "for a, we can make a small eps, so there will be a boundary between the light side and the dark side, so it will distinguish the different part. For B, we can use a large min_samples, so it will distinguish the dark side, we get what we want."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "No"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "k-means is not a good way to cluster irregular shape datasets. it also assumes that clusters are spherical and similar size, it is not useful in this case."

    # type: string
    answers["(c)"] = "spectral clustering"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
