# sort.py
# grace nguyen
# 09/22/2022
#
# purpose: implement the merge sort algorithm, whose worst case is O(nlogn)!
from array import *;
import random;
import math;


# user input functions
def getSize():
    # let user define data set size: integer greater than 0
    strDataSize = "";
    intDataSize = -1; # returned value
    keepGoing = True;
    
    while keepGoing:
        try:
            strDataSize = input("Please input an integer greater than 0: ");
            intDataSize = int(strDataSize);
            
            if intDataSize > 0:
                keepGoing = False;
            else:
                print("Value must be greater than zero.");
                keepGoing = True; 
        except:
            print("Please input an integer!");
    
    return intDataSize;

def getMaximum():
    # get the user defined maximum value for data set
    keepGoing = True;
    intMax = -1;
    strMax = "";
    
    while keepGoing:
        try:
            strMax = input("Input dataset maximum value: ");
            intMax = int(strMax);
            
            if intMax < 1:
                print("Maximum value must be greater than 1!");
                keepGoing = True;
            else:
                keepGoing = False;
        except:
            print("Maximum value must be an integer greater than 1. Try again.");
            
    return intMax;

# merge sort functions
# -- the overall algorithm follows the 'divide and merge' strategy
def split(data):
    # if array length is greater than 1:
    # recursively splits the array in half
    if len(data) == 1:
        return data; # implied - already sorted
    
    # for odd lengths, add the 'extra' middle to first half
    middleIndex = math.ceil(len(data)/2);
    length = len(data);
    
    arr1 = [data[i] for i in range(0, middleIndex)];
    arr2 = [data[i] for i in range (middleIndex, length)];
    
    # recursively split 
    arr1 = split(arr1);
    arr2 = split(arr2);
    
    # merge from small -> large
    return merge(arr1, arr2);


def merge(arr1, arr2):
    # merges two arrays toegether, and sort them
    arr3 = []; # the merged array to be returned  

    while (len(arr1) > 0) or (len(arr2) > 0):
        try:
            if arr1[0] > arr2[0]:
                arr3.append(arr2[0]);
                arr2.pop(0);
            else:
                arr3.append(arr1[0]);
                arr1.pop(0);
        except:
            # this will most likely be a seg fault, in case the two
            # arrays are of different length
            if len(arr1) > 0:
                arr3.append(arr1[0]);
                arr1.pop(0);
            else:
                arr3.append(arr2[0]);
                arr2.pop(0);

    return arr3;
            

# main function
def main():
    dataSize = getSize();
    userMax = getMaximum();
   
    data = [random.randint(1, userMax) for i in range(0, dataSize)];
    sortedData = split(data);
    
    print("\n----Sort Data----\t\t\t----Sorted Data----"); # formatting
    
    # print the data side-by side
    for i in range(0, len(data)):
        num = i + 1;
        print("Unsorted#{})\t{}\t\t\tSorted#{})\t{}".format(num, data[i], num, sortedData[i]));

# namespace
if __name__ == "__main__":
    main();