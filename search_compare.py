import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    end = time.time()
    total_time = end - start
    return found, total_time


def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    end = time.time()
    total_time = end - start
    return found, total_time


def binary_search_iterative(a_list,item):
    start = time.time()
    first = 0

    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    total_time = end - start
    return found, total_time
    
    
def binary_search_recursive(a_list,item):
    start = time.time()
    if len(a_list) == 0:
        end = time.time()
        total_time = end - start
        return False, total_time
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            end = time.time()
            total_time = end - start
            return True, total_time
        else:
            if item < a_list[midpoint]:
                end = time.time()
                total_time = end - start
                return binary_search_recursive(a_list[:midpoint], item), total_time
            else:
                end = time.time()
                total_time = end - start
                return binary_search_recursive(a_list[midpoint + 1:], item), total_time


if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 10000]

    for the_size in list_sizes:
        total_time = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            # sorting is not needed for sequential search.
            mylist = sorted(mylist)

            start = time.time()
            check = binary_search_iterative(mylist, -1)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            # sorting is not needed for sequential search.
            mylist = sorted(mylist)

            start = time.time()
            check = binary_search_recursive(mylist, -1)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Binary Search Recursive took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        for i in range(100):
            mylist = get_me_random_list(the_size)
            start = time.time()
            check = sequential_search(mylist, -1)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        for i in range(100):
            mylist = get_me_random_list(the_size)
            mylist = sorted(mylist)

            start = time.time()
            check = ordered_sequential_search(mylist, -1)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Ordered Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")