# Open file
# FLAGS: 'r' read, 'w' write, 'a' append

file_path = "..\resources\test.txt"
file = open(file_path, 'w')

# Reads entire file
#string_var = file.read()

# Read single line
#string_var = file.readline()

# Write string to a file
var = "Mohamed"
file.write(var)

# Close file
file.close()

