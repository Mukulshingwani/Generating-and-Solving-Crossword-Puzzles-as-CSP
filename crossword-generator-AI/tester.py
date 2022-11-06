# import os, glob

# folder_name = r"./NN3/*.vid"

# list_ = glob.glob(folder_name)
# for name in list_:
#     pre, ext = os.path.splitext(name)
#     os.rename(name, pre + ".mp4")

file1 = open('testing.txt', 'r')
Lines = file1.readlines()
words = []
# Strips the newline character
for line in Lines:
    words.append(line.strip().split()[2] + "\n")

with open("words_file.txt", "w") as file1:
    # Writing data to a file
    file1.writelines(words)