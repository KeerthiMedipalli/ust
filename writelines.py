# Writing to a file using writelines()
f = open("users_1.txt", 'w')
f.writelines(["Python file programming\n", "It is for freshers\n"])
f.close()

# Reading the file and demonstrating tell() and seek()
f = open("users_1.txt", 'r')
print("Current file position:", f.tell())  # Prints initial position (0)

read_f = f.read()  # Reads the whole file
print(read_f)

print("Current file position after reading:", f.tell())  # Prints position after reading

f.seek(0)  # Move back to the beginning of the file
print("After seek(0), file position:", f.tell())

read_again = f.read()  # Read again from the beginning
print(read_again)

f.close()

# Using with statement and handling errors
with open("users_1.txt", "r") as f:
    read_f = f.read()
    print(read_f)

try:
    f = open("users1.txt", 'r')  # This file might not exist
    read_f = f.read()
    print(read_f)
except FileNotFoundError:
    print("File users1.txt not found.")
finally:
    if 'f' in locals() and not f.closed:
        f.close()
