



def branch1():
    rows = 3
    for length in range(1, rows + 1):
        print("* " * length)


def branch2():
    rows = 3
    for _ in range(2):
        branch1()


def branch3():
    rows = 3

    for _ in range(3):
        branch1()

print('hi')
response = input('branch?:')
# while True:

if response == '1':
    branch1()
elif response == '2':
    branch2()
elif response == '3':
    branch3()
else:
    print('noob')
exit()
