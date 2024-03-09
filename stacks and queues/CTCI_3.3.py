'''
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 
Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack
once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack.
Implement a function popAt(index) which performs a pop operation on a specific sub-stack.

1. Describe the question
We need to create our own data structure where if a stack's length hits a certain number, we create a new stack.
2. What are the constraints
3. What are some examples given, and can you solve it by hand?

4. Any other insights you find
'''

class SetOfStacks:
    def __init__(self, limit):
        self.stacks = []
        self.latestStack = []
        self.stacks.append(self.latestStack)
        self.limit = limit

    def push(self, elem):
        if len(self.latestStack) < self.limit:
            self.latestStack.append(elem)
        else:
            self.latestStack = [elem]
            self.stacks.append(self.latestStack)

    def pop(self):
        if len(self.latestStack) >= 1:
            pop = self.latestStack.pop()
            if self.latestStack == []:
                self.stacks.pop()
                self.latestStack = self.stacks[-1]
            return pop
        
    def popAt(self, index):
        pop = self.stacks[index].pop()
        index += 1
        self.stacks[index - 1].append(self.stacks[index][0])
        while index < len(self.stacks):
            for i, val in enumerate(self.stacks[index]):
                if i == 0:
                    self.stacks[index - 1][-1] = val
                else:
                    self.stacks[index][i-1] = val
            index += 1
        self.stacks[-1].pop()
        return pop





stack = SetOfStacks(2)

stack.push(1)
stack.push(2)
stack.push(1)
stack.push(2)
stack.push(1)
stack.push(2)
stack.push(1)
stack.push(2)
stack.push(1)
stack.push(2)
stack.popAt(2)
# stack.pop()
# stack.pop()
# stack.push(2)
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.popAt(1)


print(stack.latestStack)
print(stack.stacks)


