# inheritance in Python via ()
class MyList(list):
    # instance methods -> operate on instance of class
    # (self) is allways passed as the first argument of instance methods
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))

x = [1,2,3,4,58,5,4]
y = MyList(x)

print(x==y)
print(dir(y))