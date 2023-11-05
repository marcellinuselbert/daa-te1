from random import randrange
import copy
import time
import tracemalloc
import random 

def generate_dataset(size):
    ordered_list = list(range(1, size + 1))
    randomized_list = ordered_list.copy()
    reversed_list = list(reversed(ordered_list))
    

    random.shuffle(randomized_list)
    dataset={}

    dataset["sorted"]=ordered_list
    dataset["random"]=randomized_list
    dataset["reversed"]=reversed_list

    return dataset


class Quicksort:
    @staticmethod
    def quicksort(alist, start, end):
        if start < end:
            pIndex = Quicksort.partition(alist, start, end)
            Quicksort.quicksort(alist, start, pIndex-1)
            Quicksort.quicksort(alist, pIndex+1, end)
        
        return alist

    @staticmethod
    def partition(alist, start, end):
        pivot = randrange(start, end)
        alist[pivot], alist[end] = alist[end], alist[pivot]
        pIndex = start-1
        
        for i in range(start, end):
            if alist[i] <= alist[end]:
                pIndex += 1
                alist[i], alist[pIndex] = alist[pIndex], alist[i]
                
        pIndex += 1
        alist[pIndex], alist[end] = alist[end], alist[pIndex]
        
        return pIndex


class ClusteredBinaryInsertionSort:
    @staticmethod
    def clustered_binary_insertion_sort(a_list):
        pop = 0
        for i in range(1,len(a_list)):
            cop = i 
            key = a_list[cop]

            if key >= a_list[pop]:
                place = ClusteredBinaryInsertionSort.binary_loc_finder(a_list,pop+1,cop-1,key)
            else:
                place = ClusteredBinaryInsertionSort.binary_loc_finder(a_list,0,pop-1,key)

            pop = place 
            a_list = ClusteredBinaryInsertionSort.place_inserter(a_list,pop,cop)
        
        return a_list
        

    @staticmethod
    def binary_loc_finder(a_list, start, end, key):
        if start == end:

            if a_list[start] > key:
                return start
            else:
                return start+1

        if start > end:
            return start 
        
        else:
            middle = (start+end)//2

            if a_list[middle] < key:
                return ClusteredBinaryInsertionSort.binary_loc_finder(a_list,middle+1,end,key)
            
            elif a_list[middle] > key:
                return ClusteredBinaryInsertionSort.binary_loc_finder(a_list,start,middle-1,key)
            
            else:
                return middle

    @staticmethod
    def place_inserter(a_list,start,end):
        temp = a_list[end]
        for i in range(end,start,-1):
            a_list[i] = a_list[i-1]
        
        a_list[start] = temp
        return a_list



dataset_small = generate_dataset(200)
dataset_medium = generate_dataset(2000)
dataset_large = generate_dataset(20000)



for data in [dataset_small,dataset_medium,dataset_large]:
    print("Size: ", len(data["sorted"]))
    print("Randomized Quicksort\n")
    data_qs = copy.deepcopy(data)
    tracemalloc.start()  

    for key, value in data_qs.items():

        start_time = time.time()
        sorted_list = Quicksort.quicksort(value, 0, len(value) - 1)
        end_time = time.time()


        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.clear_traces()

        print(f"Time taken with dataset {key}: {(end_time - start_time) * 1000} ms")
        print(f"Peak memory usage: {peak / 10**6} MB")

    print("\n" + "-" * 20 + "\n")
    print("Clustered Binary Insertion Sort\n")



    data_cbis = copy.deepcopy(data)

    for key, value in data_cbis.items():


        tracemalloc.start() 

        start_time = time.time()
        sorted_list = ClusteredBinaryInsertionSort.clustered_binary_insertion_sort(value)
        end_time = time.time()


        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.clear_traces()


        print(f"Time taken with dataset {key}: {(end_time - start_time) * 1000} ms")
        print(f"Peak memory usage: {peak / 10**6} MB")

    print("\n")


