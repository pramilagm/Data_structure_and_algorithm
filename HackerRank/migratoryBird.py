# You have been asked to help study the population of birds migrating across the continent. Each type of bird you are interested in will be identified by an integer value. Each time a particular kind of bird is spotted, its id number will be added to your array of sightings. You would like to be able to find out which type of bird is most common given a list of sightings. Your task is to print the type number of that bird and if two or more types of birds are equally common, choose the type with the smallest ID number.

# For example, assume your bird sightings are of types . There are two each of types  and , and one sighting of type . Pick the lower of the two types seen twice:

# Function Description

# Complete the migratoryBirds function in the editor below. It should return the lowest type number of the most frequently sighted bird.

# migratoryBirds has the following parameter(s):

# arr: an array of integers representing types of birds sighted
# Input Format

# The first line contains an integer denoting , the number of birds sighted and reported in the array .
# The second line describes  as  space-separated integers representing the type numbers of each bird sighted.

# Constraints

# It is guaranteed that each type is , , , , or .
# Output Format

# Print the type number of the most common bird; if two or more types of birds are equally common, choose the type with the smallest ID number.

# Sample Input 0

# 6
# 1 4 4 4 5 3
# Sample Output 0

# 4


def migratoryBirds(arr):

    count = [0]*6
    for t in map(int, arr):
        count[t] += 1
    print(count.index(max(count)))
    # hash = {}
    # for item in arr:
    #     if item in hash:
    #         hash[item] += 1
    #     else:
    #         hash[item] = 1

    # max_val = max(hash.values())

    # for key, val in hash.items():

    #     if val == max_val:
    #         pass


arr = [1, 2,  4, 5, 4, 3, 2, 1, 3, 4]
migratoryBirds(arr)
