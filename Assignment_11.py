file_name = "sample.txt"

# 1. Writing to a file (overwrite mode)
try:
    with open(file_name, "w") as file:
        file.write("Hello, this is the first line.\n")
        file.write("File handling in Python is simple!\n")
    print("File written successfully.")
except Exception as e:
    print("Error while writing:", e)

# 2. Reading from the file
try:
    with open(file_name, "r") as file:
        print("\nReading file content:")
        for line in file:
            print(line.strip())
except Exception as e:
    print("Error while reading:", e)

# 3. Appending data to the file
try:
    with open(file_name, "a") as file:
        file.write("\nThis line is appended later.")
    print("\nData appended successfully.")
except Exception as e:
    print("Error while appending:", e)

# 4. Reading again to show updated content
try:
    with open(file_name, "r") as file:
        print("\nReading updated file content:")
        for line in file:
            print(line.strip())
except Exception as e:
    print("Error while reading:", e)