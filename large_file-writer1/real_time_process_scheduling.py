# this program covers the evaluation of real time process scheduling algorithms
# first, we will read a text file 


import time
import random

def rng():
    # Open the file for writing
    with open("file1.txt", "w") as file:
        # Generate 10 million lines of random integers
        for i in range(10000000):
            # Generate a random integer between 1 and 1000
            random_int = random.randint(1, 1000)
            # Write the integer to the file, followed by a newline character
            file.write(str(random_int) + "\n")


def read_file_1(filename):
    start = time.time()  # start time
    # load into memory and print
    f = open("file1.txt", "r")
    new_file = "newfile1_py.txt"
    f2 = open(new_file, "w")
    f2.writelines(f.readlines()*2)
    end = time.time()  # end time
    print("The execution time for reading the content into memory in Python3 is: ", (end - start), "in seconds")  # time elapsed


filename = "file1.txt"
read_file_1(filename)

# rng()