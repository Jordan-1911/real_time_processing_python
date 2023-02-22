import time

def read_file_1(filename):
    start = time.time()  # start time
    # load into memory and print
    f = open("file1.txt", "r")
    new_file = "newfile1_py.txt"
    f2 = open(new_file, "w")
    f2.writelines(f.readlines()*2)
    end = time.time()  # end time
    print("The execution time for reading the content into memory in Python3 is: ", (end - start), "in seconds")  # time elapsed
    
def read_file_2(filename):
    start = time.time()  # start time
    
    # read file one line at a time in memory and print
    with open("file1.txt") as input_file:
        with open("newfile2_py.txt", "w") as output_file:
            for line in input_file:
                num = int(line)
                result = num * 2
                
                output_file.write(str(result) + "\n")
            
    end = time.time()  # end time
    print("The execution time for reading one row at a time in Python3 is: ", (end - start), "in seconds")  # time elapsed
            

def read_file_3(filename):
    start = time.time()  # start time

    with open("file1.txt", "r") as input_file:
        content = input_file.read()
        
        # split into two
        half = len(content) // 2
        first_half = content[:half]
        second_half = content[half:]
        
        # write the first half to the output file
        with open("output1.txt", "w") as output1:
            for line in first_half.splitlines():
                num = int(line)
                result = num * 2
                output1.write(str(result) + "\n")
        
        # write the second half to the output file
        with open("output2.txt", "w") as output2:
            for line in second_half.splitlines():
                num = int(line)
                result = num * 2
                output2.write(str(result) + "\n")

    end = time.time()  # end time
    print("The execution time for splitting into 2 parts in Python3 is: ", (end - start), "in seconds")  # time elapsed
    
    
filename = "file1.txt"
read_file_1(filename)
read_file_2(filename)
read_file_3(filename)