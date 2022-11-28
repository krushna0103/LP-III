# N Queen 

def queen(n):
    def backTrack(i):
        if i == n:
            result.append(list(board))
            
        
        for j in range(n):

            if j not in column and j-i not in diagonal and j+i not in ofDiagonal:
                column.add(j)
                diagonal.add(j-i)
                ofDiagonal.add(j+i)
                board.append("-" * j + "Q" + "-" * (n-j-1))
                backTrack(i+1)
                
                column.remove(j)
                diagonal.remove(j-i)
                ofDiagonal.remove(j+i)
                board.pop()
                
    result = []
    board = []
    column = set()
    diagonal = set()
    ofDiagonal = set()

    backTrack(0)
    return result


v1 = int(input("\nEnter No of Queens : "))
v2 = queen(v1)

# Two print all possibilities
# for p in v2:
#     for i in p:
#         for j in i:
#             print(j, end=" ")
#         print()
#     print("\n")

# Only print first Posibility
for i in v2[0]:
    for j in i:
        print(j,end=" ")
    print()