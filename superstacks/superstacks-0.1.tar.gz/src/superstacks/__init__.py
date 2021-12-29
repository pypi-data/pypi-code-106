class StackError(BaseException):
    def __init__(self, msg=""):
        self.msq = msg
    def __repr__(self):
        return self.msg
class stacks:
    def __init__(self, size):
        self.size = size-1
        self.stacklist = [ ]
        self.top = -1
    def push(self, value):
        self.stacklist.append(value)
        self.top += 1
        if self.top > self.size:
            raise StackError("CRITICAL ERROR: STACK OVERFLOW")
    def pop(self):
        if self.top == -1:
            return "stack empty"
        elif self.top < -1:
            raise StackError("CRITICAL ERROR: STACK UNDERFLOW")
        else:
            self.top -= 1
            r = self.stacklist[-1]
            del self.stacklist[-1]
            return r
    def isempty(self):
        if self.top > -1:
            return False
        else:
            return True
    def peek(self):
        if self.top == -1:
            return "stack empty"
        else:
            return self.stacklist[-1]
