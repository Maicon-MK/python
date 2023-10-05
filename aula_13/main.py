# x = range(1,11)
# for interavel in x:
#     print(interavel)


# x = range(1,11)
# print(next(iter(x)))#iter recebe um argumento  e retor o interador desse objeto


#old scool

# class Iter:
#     def __init__(self, numero):
#         self.numero = numero

#     def __inter__(self):
#         self.current = -1
#         return self
    
# #next
# #iter

#     def __next__(self):
#         self.current += 1

#         if self.current >= self.numero:
#             raise StopIteration
#         return self.current
    
# x = Iter(5)
# print(x.__iter__())
# for interavel in x:
#     print(interavel)


# def Gen(n):
#     for i in range(n):
#         yield i 
# for i in Gen(5):
#     print(i)

 
