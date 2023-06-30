member = input("Enter a new member: ")
file = open('C:/Users/frenc/Downloads/members.txt', 'r')
members = file.readlines()
file.close()

members.append(member + "\n")

file = open("C:/Users/frenc/Downloads/members.txt", 'w')
members = file.writelines(members)
file.close()