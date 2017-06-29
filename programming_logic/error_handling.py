try:
    # Code to be Executed
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")

except IOError:
    # When Error Occurs
    print("Error: can\'t find file or read data")

else:
    # If there's no Exception then execute this block
    print("Written content in the file successfully")
    fh.close()