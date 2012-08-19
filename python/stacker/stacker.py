###
# Stacker, a small useless subset of forth.
# Based on http://puzzlenode.com/puzzle/15-poor-mans-forth
#
# Written by Tor Erling H. Opsahl
###

class Interpreter:
    def __init__(self):
        self.stack = []
        self.return_stack = []

    def doublepop(self):
        """ pops two numbers off the stack and returns a tuple of their integer
        representation"""
        a = int(self.stack.pop())
        b = int(self.stack.pop())
        return (a, b)

    def add(self):
        """ Pops two numbers off the stack and add them together push the sum
        back on the stack """
        a, b = self.doublepop()
        self.return_stack.append(str(a + b))

    def subtract(self):
        """ Pops two numbers off the stack, subtract the first one from the last
        and push the result back on the stack"""
        a, b = self.doublepop()
        self.return_stack.append(str(b - a))

    def multiply(self):
        """ Pops two numbers off the stack, multiplies them, and pushes
        the result back on the stack """
        a, b = self.doublepop()
        self.return_stack.append(str(a * b))

    def divide(self):
        """ Pops two numbers off the stack, devides the second one on the first
        and push the result on the stack """
        a, b = self.doublepop()
        # for now we're doing integer division
        self.return_stack.append(str(b // a))

    def mod(self):
        """ Pops two numbers off the stack finds the modulo second of the first
        and pushes the result on the stack """
        a, b = self.doublepop()
        self.return_stack.append(str(b % a))

    def lt(self):
        """ Pops two numbers off the stack, checks if the one longer up on the stack
        is smaller than the one on the top, and pushes True or False to the stack """
        a, b = self.doublepop()
        self.return_stack.append(b < a)

    def gt(self):
        """ Pops two numbers off the stack, checks if the one longer up on the stack
        is greater than the one on the top, and pushes True or False to the stack """
        a, b = self.doublepop()
        self.return_stack.append(b > a)

    def equal(self):
        """ Pops two numbers off the stack, checks if the one longer up on the stack
        is equal to the one on the top, and pushes True or False to the stack """
        a, b = self.doublepop()
        self.return_stack.append(b == a)


    def execute(self, in_stack=[]):
        """ Execute a stack of commands """
        # Add in_stack to the internal stack
        self.stack.extend(in_stack)

        # start a loop so that we can do more than one operation on the set
        while self.stack != []:

            # Pop the last element off the stack to see what the command is
            current = self.stack.pop()
            
            # depending on what current is, do something to the stack
            if current == "ADD":
                self.add()
            elif current == "SUBTRACT":
                self.subtract()
            elif current == "MULTIPLY":
                self.multiply()
            elif current == "DIVIDE":
                self.divide()
            elif current == "MOD":
                self.mod()
            elif current == "<":
                self.lt()
            elif current == ">":
                self.gt()
            elif current == "=":
                self.equal()

        # reverse the return stack and get that to be the new stack
        self.return_stack.reverse()
        self.stack = self.return_stack[:]

if __name__ == "__main__":
    pass
