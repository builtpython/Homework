
array = [-25, -10, -7, -3, 2, 4, 8, 10]

class ZeroSum:
    def __init__(self, array):
        self.array = array
    def Sum_three(self):
        output = []
        for x in range(len(self.array)):
            for z in range(x + 1, len(self.array)):
                for i in range(z + 1, len(self.array)):
                    if self.array[i] + self.array[z] + self.array[x] == 0:
                        output.append([self.array[i], self.array[x], self.array[z]])
        return output

print(ZeroSum(array).Sum_three())



