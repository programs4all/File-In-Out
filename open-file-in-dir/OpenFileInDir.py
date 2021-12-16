file_loc = "Data/data.txt"
file = open(file_loc, "w+")

with file as f:
    f.write("This is a text file created from python")
    