# Open file
# FLAGS: 'r' read, 'w' write, 'a' append
file_path = "test.txt"
file = open(file_path, 'r')

# Reads entire file
string_var = file.read()
print(string_var)

# Read single line
string_var = file.readline()

# Write string to a file
var = "Mohamed"
file.write(var)

# Close file
file.close()

