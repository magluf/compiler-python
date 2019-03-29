import sys

file = sys.argv[1]

read_file = open(file, 'r')
token = ""
for line_idx, line in enumerate(read_file, start=1):
    for position, i in enumerate(range(len(line))):
        token += line[i]
        if (line[i] == ' '):
            print("look_ahead = " + str(position))
            print(token)
            break

read_file.close()
