x=int(input())
for i in range(1,x+1):
    print(" "*2*(x-i),end="")
    print("*   "*i)
for i in range(x-1,0,-1):
    print(" "*2*(x-i),end="")
    print("*   "*i)

#Output
#             *   
#           *   *
#         *   *   *
#       *   *   *   *
#     *   *   *   *   *
#   *   *   *   *   *   *
# *   *   *   *   *   *   *
#   *   *   *   *   *   *
#     *   *   *   *   *
#       *   *   *   *
#         *   *   *
#           *   *
#             *