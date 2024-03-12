'''
    Day 61
    Create a program to implement a stack using a list

    push: Adds an element to the top of the stack.
    pop: Removes the topmost element from the stack.
    is_empty : Checks whether the stack is empty.
    get_size: Get the size of the stack
    top_item : Displays the topmost element of the stack.

    Output:
    The stack is empty: True
    Push numbers from 0 to 9 to the stack
    The stack is empty: False
    Stack size is: 10
    The top element is: 9
    Poped item: 9
    Poped item: 8
    Poped item: 7
    Poped item: 6
    Poped item: 5
    Stack size is: 5
    The top element is: 4
    Poped item: 4
    Poped item: 3
    Poped item: 2
    Poped item: 1
    Poped item: 0
    Error: Popping from an empty stack

'''

class MyStack():

    def __init__(self) -> None:
        self.my_list = []

    def push(self, item):
        ''' Insert item '''
        self.my_list.append(item)

    def pop(self):
        ''' Pop item '''
        if self.is_empty():
            raise Exception("Error: Popping from an empty stack")
        return self.my_list.pop()

    def is_empty(self):
        ''' Check if the stack is empty -> Boolean '''
        return len(self.my_list) == 0

    def get_size(self) -> bool:
        ''' Get stack size '''
        return len(self.my_list)

    def top_item(self):
        ''' Displays the topmost item '''
        if self.is_empty():
            raise Exception("Error: The stack is empty.")
        top_index = len(self.my_list)-1
        return self.my_list[top_index]

if __name__ == "__main__":

    my_stack = MyStack()

    print(f"The stack is empty: {my_stack.is_empty()}")
    print("Push numbers from 0 to 9 to the stack")

    for i in range(0, 10):
        my_stack.push(i)

    print(f"The stack is empty: {my_stack.is_empty()}")
    print(f"Stack size is: {my_stack.get_size()}")
    print(f"The top element is: {my_stack.top_item()}")

    for _ in range(0, 5):
        try:
            print(f"Poped item: {my_stack.pop()}")
        except Exception as e:
            print(e)

    print(f"Stack size is: {my_stack.get_size()}")
    print(f"The top element is: {my_stack.top_item()}")

    for _ in range(0, 6):
        try:
            print(f"Poped item: {my_stack.pop()}")
        except Exception as e:
            print(e)
