input = raw_input()

a = int(input.split(' ')[0])
b = int(input.split(' ')[1])
c = int(input.split(' ')[2])

i = b-a
j = c-b


print max(i,j) - 1