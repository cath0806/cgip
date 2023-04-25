import turtle
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
result1=[0,0,0,0,0,0,0,0,0,0]
num=int(input("Enter number of sides : "))
for i in range(num):
    print("Enter co-ordinates of point ",i+1)
    x[i]=int(input())
    y[i]=int(input())

#printing reflected points
print("The modified points are: ")
for i in range(num):
    result1[i]=reflect(x[i],y[i])
    print("Point ",i," : ",result1[i])
t = turtle.Turtle()
s=turtle.Screen().bgcolor("black")

# Set the window size and coordinates
turtle.setup(600, 600)
turtle.setworldcoordinates(-10, -10, 10, 10)

# Draw the x and y axes
t.pencolor("white")
t.penup()
t.goto(-10, 0)
t.pendown()
t.goto(10, 0)
t.penup()
t.goto(0, -10)
t.pendown()
t.goto(0, 10)
# Draw the graph of y = -x
t.pencolor("gray")
t.penup()
t.goto(-10, 10)
t.pendown()
for x1 in range(-10, 11):
    y1 = -x1
    t.goto(x1, y1)
t.penup()
# Drawing Polygon given by user
t.goto(x[0],y[0])
t.pencolor("red")
t.color("red")
t.begin_fill()
t.pendown()
for i in range(1,num):
    t.goto(x[i],y[i])
t.end_fill()
t.goto(x[0],y[0])
t.penup()
# Drawing Reflected Polygon
t.goto(result1[0][0][0],result1[0][1][0])
t.pencolor("orange")
t.color("orange")
t.begin_fill()
t.pendown()
for i in range(1,num):
    t.goto(result1[i][0][0],result1[i][1][0])
t.end_fill()
t.goto(result1[0][0][0],result1[0][1][0])

# Hide the turtle cursor
t.hideturtle()

# Update the turtle screen
turtle.done()