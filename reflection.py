#function takes co-ordinates of a point and returns co-ordinates corresponding to reflection against y=-x
def reflect(x,y):
    a=[[0, -1, 0],
       [-1, 0, 0],
       [ 0, 0, 1]]
    b=[[x],
       [y],
       [1]]
    result=[[0],
            [0],
            [0]]
    for i in range(3):
        for j in range(1):
            for k in range(3):
                result[i][j] += a[i][k] * b[k][j]
    result.pop(2)
    return result

#getting user inputs
x=[0,0,0,0,0,0,0,0,0,0]
y=[0,0,0,0,0,0,0,0,0,0]
num=int(input("Enter number of sides : "))
for i in range(num):
    print("Enter co-ordinates of point ",i+1)
    x[i]=int(input())
    y[i]=int(input())

#printing reflected points
print("The modified points are: ")
for i in range(num):
    result=reflect(x[i],y[i])
    print("Point ",i," : ",result)