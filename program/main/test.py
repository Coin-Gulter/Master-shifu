

class A():
    def __init__(self, same, A):
        self.same = same
        self.A = A

    def printing(self):
        print('A: = ', self.A)
        print('A: same -' , self.same)

class B():
    def __init__(self, same, B):
        self.same = same
        self.B = B

    def printing(self):
        print('B: = ', self.B)
        print('B: same - ' , self.same)

class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        self.same = '-C-'
        self.A = 'a'
        self.B = 'b'

    def use(self):
        self.printing()


if __name__ == "__main__":
    c = C()
    c.use()