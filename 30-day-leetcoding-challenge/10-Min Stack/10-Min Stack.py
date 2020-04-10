class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list=[]

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> None:
        self.list.pop()

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return sorted(self.list)[0]
        # sorted是真的蠢

    def printList(self):
        print(self.list)

# 大佬方法 sb才用sorted
# def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min_values = []
        

#     def push(self, x: int) -> None:
#         self.stack.append(x)
        
#         if not self.min_values or x<=self.min_values[-1]:
#             self.min_values.append(x)
        

#     def pop(self) -> None:
#         num = self.stack.pop()
        
#         if num==self.min_values[-1]:
#             self.min_values.pop()
        

#     def top(self) -> int:
#         return self.stack[-1]
        

#     def getMin(self) -> int:
#         return self.min_values[-1]




if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-1)
    obj.printList()
    obj.push(1)
    obj.printList()
    obj.push(3)
    obj.printList()
    obj.push(5)
    obj.printList()
    obj.pop()
    obj.printList()
    param_3 = obj.top()
    print(param_3)
    param_4 = obj.getMin()
    print(param_4)
