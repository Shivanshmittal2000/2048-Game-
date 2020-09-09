import random
def start_game():
    mat=[[0 for i in range(4)] for j in range(4)]
    return mat
def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while mat[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2
    return mat
# compress means all non-zero numbers are come on one side
def compress(mat):
    changed=False
    for i in range(4):
        index=0
        for j in range(4):
            if mat[i][j]!=0:
                mat[i][j],mat[i][index]=mat[i][index],mat[i][j]
                if j!=index:
                    changed=True
                index+=1
    return mat,changed
#Another way of making the compress function
# def compress(mat):
#     new_matrix=[[0 for i in range(4)] for j in range(4)]
#     for i in range(4):
#         index=0
#         for j in range(4):
#             if mat[i][j]!=0:
#                 new_marixt[i][index]=mat[i][j]
#                 index+=1
#     return new_matrix
# consecutive elemnets are combine
def merge(mat):
    changed=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]=2*mat[i][j]
                mat[i][j+1]=0
                changed=True
    return mat,changed
def reverse(mat):
    for i in range(4):
        k=3
        for j in range(2):
            mat[i][j],mat[i][k]=mat[i][k],mat[i][j]
            k-=1
    return mat
def transpose(mat):
    newmatrix=[]
    for i in range(4):
        a=[]
        for j in range(4):
            a.append(mat[j][i])
#             print(a)
        newmatrix.append(a)
#         print(newmatrix)
    return newmatrix
def move_left(mat):
    matrix,change1=compress(mat)
    matrix,change2=merge(matrix)
    changed=change1 or change2
    matrix,nouse=compress(matrix)
    return matrix,changed
def move_right(mat):
    matrix=reverse(mat)
    matrix,change1=compress(matrix)
    matrix,change2=merge(matrix)
    changed=change1 or change2
    matrix,nouse=compress(matrix)
    matrix=reverse(matrix)
    return matrix,changed
def move_up(mat):
    matrix=transpose(mat)
    matrix,change1=compress(matrix)
    matrix,change2=merge(matrix)
    changed=change1 or change2
    matrix,nouse=compress(matrix)
    matrix=transpose(matrix)
    return matrix,changed
# Another way of moving up
# def move_up(mat):
#     matrix=transpose(mat)
#     matrix,changed=move_left(matrix)
#     matrix=transpose(matrix)
#     return matrix,changed
def move_down(mat):
    matrix=transpose(mat)
    matrix=reverse(matrix)
    matrix,change1=compress(matrix)
    matrix,change2=merge(matrix)
    changed=change1 or change2
    matrix,nouse=compress(matrix)
    matrix=reverse(matrix)
    matrix=transpose(matrix)
    return matrix,changed
# Another way of moveing down
# def move_down(mat):
#     matrix=transpose(mat)
#     matrix,changed=move_right(matrix)
#     matrix=transpose(matrix)
#     return matrix,changed
def current_state(mat):
    # check in the matrix anywhere 2048 is find then won the game
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return 'WON'
    # check game is not over condition
    # a. if anywhere 0 is present or not
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return 'GAME NOT OVER'
    # b. check two consecutive elements are same or not except last row and last column
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]:
                return 'GAME NOT OVER'
    # c. Check last row 
    for i in range(3):
        if mat[3][i]==mat[3][i+1]:
            return 'GAME NOT OVER'
    # d. Check last column
    for j in range(3):
        if mat[j][3]==mat[j+1][3]:
            return 'GAME NOT OVER'
    #otherwise game is lost
    return  'LOST'