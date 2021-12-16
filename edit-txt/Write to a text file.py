# READ FROM ONE FILE AND WRITE TO ANOTHER
#READ
in_file = open('read.txt', "r")

#WRITE
out_file = open("write.txt", "w")

with in_file, out_file:
    for line in in_file:
        try:
            num = int(line)

        except ValueError as err:
            print(err)

        else:
            string = f'{num}^2 = {num ** 2}\n'
            out_file.write(string)
