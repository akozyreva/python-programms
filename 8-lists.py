"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed
by  lines of commands where each command will be of the  types listed above.
Iterate through each command in order and perform
the corresponding operation on your list.
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.
"""

N = int(raw_input())
list = []


def list_functions_without_arg(command):
    if command == 'print':
        print list
    elif command == 'sort':
        list.sort()
    elif command == 'pop':
        list.pop(len(list)-1)
    elif command == 'reverse':
        list.reverse()


def list_functions_with_one_arg(command, arg):
    if command == 'remove':
        list.remove(int(arg))
    elif command == 'append':
        list.append(int(arg))


def list_insert(pos, arg):
    list.insert(int(pos), int(arg))


commands = ['insert', 'print', 'remove', 'append', 'sort', 'pop', 'reverse']
for i in range(N):
    command = raw_input()
    # try to find coincidence and understand the number of arguments
    fun_with_arg = len(command.split())
    index = commands.index(command.split()[0]) + 1
    command = command.split()
    # if function has only one argument
    if index and fun_with_arg == 1:
        list_functions_without_arg(command[0])
    elif index and fun_with_arg == 2:
       list_functions_with_one_arg(command[0], command[1])
    # we have only ony function for the 3 arguments -  insert
    elif index and fun_with_arg == 3:
        list_insert(command[1], command[2])

