###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Sassan Mtr


from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cows = {}
    file = open(filename)
    for line in file:
        split_line = line.split(",")
        cows[split_line[0]]=split_line[1][0]
    file.close()
    return cows
     

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # First we produce a dictionary in which the keys are the number of space ships and values are
    # the list of cows in that spaceship. Then, we produce a list of list out of this dictionary
    cows_copy = cows.copy()
    allocated_cows = {}
    counter = 1
    while bool(cows_copy) is True:
        allocated_cows[counter] = []
        available_space = limit
        while bool(cows_copy) is True:
            if available_space < int(min(cows_copy.values())):
                counter += 1
                break
            else:
                # sort the current values of dictionary in accending order
                for i in sorted(cows_copy.values(), reverse = True):
                    if int(i) <= available_space:
                        # candidate is the key and allocated_cows is the value
                        candidate = list(cows_copy.keys())[list(cows_copy.values()).index(i)]
                        # add the chosen cow to the current spaceship and delete it from cows_copy
                        allocated_cows[counter].append(candidate)
                        available_space -= int(cows_copy[candidate])
                        del cows_copy[candidate]
    l = []
    for i in allocated_cows:
        l.append(allocated_cows[i])
    return l
                                                                              
# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    int_cows = {k: sum(map(int, v)) for k, v in cows.items()} #make values of dictionary int (from string)
    optimal_sol = [0] * (len(list(cows.keys())) + 1)
    for partition in get_partitions(list(cows.keys())): # partition is list of list 
        if len(partition) < len(optimal_sol):
            weigths = []
            for lst in partition:   # Each partition contains some lists
                new_weigths = 0
                for i in lst:  # loop over each element of the lists
                    new_weigths += int_cows[i]
                weigths.append(new_weigths)
            if max(weigths) <= limit and max(weigths) > 0:
                optimal_sol = partition
    return optimal_sol        
       
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    start_greedy = time.time()
    greedy = greedy_cow_transport(cows,limit=10)
    end_greedy = time.time()
    diff_greedy = end_greedy - start_greedy
    #
    start_brute = time.time()
    brute = brute_force_cow_transport(cows,limit=10)
    end_brute = time.time()
    diff_brute = end_brute - start_brute
    #
    print("For the Greedy algorithm: The number of trips is " , len(greedy), 
          " and it takes ", diff_greedy, " to perform the algorithm." )

    print("For the Brute force algorithm: The number of trips is " , len(brute), 
          " and it takes ", diff_brute, " to perform the algorithm." )






