# this program covers the evaluation of real time process scheduling algorithms
# first, we will write 1 million random numbers to 10 separate files
# then we will combine the outputs into a single text file


import time
import random


start_time = time.time()
# Generate 1 million random numbers
numbers = [random.randint(1, 1000) for i in range(1000000)]

# Write the numbers to 10 separate files
for i in range(10):
    with open(f"file{i}.txt", "w") as file:
        # Calculate the range of numbers to write to this file
        start_index = i * 100000
        end_index = (i + 1) * 100000
        # Write the numbers to the file
        for num in numbers[start_index:end_index]:
            file.write(str(num) + "\n")

# Combine the outputs into a single text file
with open("combined_file.txt", "w") as output_file:
    # Open each input file and copy its contents to the output file
    for i in range(10):
        with open(f"file{i}.txt", "r") as input_file:
            output_file.write(input_file.read())
            
end_time = time.time()
print(f"Execution time: {end_time - start_time:.2f} seconds")
