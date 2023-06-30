filenames = ['C:/Users/frenc/Downloads/a.txt', 'C:/Users/frenc/Downloads/b.txt', 'C:/Users/frenc/Downloads/c.txt']
for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)

file = open("data.txt", 'w')

file.write("100.12\n")
file.write("111.13\n")

file.close()