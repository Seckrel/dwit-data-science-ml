class Constant:
    PI = 3.14
    GRAVITY = 9.8

    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify constant")


consts = Constant()
print(consts.PI)

consts.PI = 3  # breaks code at this point
print(consts.PI)
