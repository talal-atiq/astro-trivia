# Source Code for Astro Trivia:
#A project designed to help kids learn more about Astronomy via short and small multiple choice based quiz :)

# import modules:
import time
import turtle

#Setting a picture as the background of the window:
x= turtle.Turtle()
back = turtle.Screen()
back.bgpic("1.gif")


# Setting up the main window:
window = turtle.Screen()
window.setup(1000, 600)
window.colormode(255)
window.title("Astro Trivia")



# Making the text boxes for choices, scores and questions:
# box A
turtle.speed(0)
turtle.penup()
turtle.goto(-442, -75)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.color("#2072CB")
for sides in range(2):
    turtle.fd(300)
    turtle.left(90)
    turtle.fd(90)
    turtle.left(90)
turtle.end_fill()

# box B
turtle.speed(0)
turtle.penup()
turtle.goto(25, -75)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(300)
    turtle.left(90)
    turtle.fd(90)
    turtle.left(90)
turtle.end_fill()

# Box C:
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-442, -250)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.color("#2072CB")
for sides in range(2):
    turtle.fd(300)
    turtle.left(90)
    turtle.fd(90)
    turtle.left(90)
turtle.end_fill()

# box D
turtle.penup()
turtle.goto(25, -250)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(300)
    turtle.left(90)
    turtle.fd(90)
    turtle.left(90)
turtle.end_fill()


# Question box
turtle.penup()
turtle.goto(-450, 100)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(625)
    turtle.left(90)
    turtle.fd(140)
    turtle.left(90)
turtle.end_fill()

# Score box
turtle.penup()
turtle.goto(275, 170)
turtle.pendown()
turtle.dot(150)

# Creating Question turtle:
quest = turtle.Turtle()
quest.speed(0)
quest.hideturtle()
quest.penup()
quest.goto(-425, 150)

# Creating Score turtle:
score1 = turtle.Turtle()
score1.speed(0)
score1.hideturtle()
score1.penup()
score1.goto(260, 145)
score1.setheading(0)
for sides in range(2):
    score1.fd(300)
    score1.left(90)
    score1.fd(90)
    score1.left(90)
score1.end_fill()

# Creating Answer turtles:
# A
A = turtle.Turtle()
A.speed(0)
A.hideturtle()
A.penup()
A.goto(-425, -50)

# B
B = turtle.Turtle()
B.speed(0)
B.hideturtle()
B.penup()
B.goto(50, -50)

# C
C = turtle.Turtle()
C.speed(0)
C.hideturtle()
C.penup()
C.goto(-425, -225)

# D
D = turtle.Turtle()
D.speed(0)
D.hideturtle()
D.penup()
D.goto(50, -225)


#Exit Functionality:
def exit_game():
    window.bye()


# Opening Credits
fontcolor=quest.color('white')
quest.write("Welcome to Astro Trivia", font=("Arial Narrow", 40, "bold"))
time.sleep(2)
quest.clear()

quest.write("Press A, B, C, or D to answer!", font=("Arial Narrow", 30, "bold"))
time.sleep(2)
quest.clear()

quest.write("Good Luck :)", font=("Arial Narrow", 30, "bold"))
time.sleep(2)
quest.clear()

# NUMBER OF CORRECT ANSWERS HERE
correctNow = 0
fontcolor=score1.color('#F9B300')
score1.write("{}".format(correctNow), font=("Times New Roman", 45, "bold"))

# Variables
CurrentQ = 1

# Key Functions:
def chooseAnswerA():
    global select
    select = 'A'
    evaluate()

def chooseAnswerB():
    global select
    select = 'B'
    evaluate()

def chooseAnswerC():
    global select
    select = 'C'
    evaluate()

def chooseAnswerD():
    global select
    select = 'D'
    evaluate()

def evaluate():
    global correctNow
    global CurrentQ
    if correct == select:
        quest.clear()
        fontcolor=quest.color('#FFF413')
        quest.write("CORRECT!!!", font=("Arial Narrow", 32, "bold"))
        time.sleep(1.2)
        score1.clear()
        correctNow += 1
        score1.write("{}".format(correctNow), font=("Arial Narrow", 45, "bold"))
    else:
        quest.clear()
        fontcolor=quest.color('#FFF413')
        quest.write("WRONG! The answer was {}".format(correct), font=("Arial Narrow", 32, "bold"))
        time.sleep(1.2)
        quest.clear()
    CurrentQ += 1
    clearBoard() #calling the clearBoard function
    GetQuestionNum() #calling the GetQuestionNum function


#Adding Questions to the GUI:
def GetQuestionNum():
    if CurrentQ == 2:
        question2()
    if CurrentQ == 3:
        question3()
    if CurrentQ == 4:
        question4()
    if CurrentQ == 5:
        question5()
    if CurrentQ == 6:
        question6()
    if CurrentQ == 7:
        question7()
    if CurrentQ == 8:
        question8()
    if CurrentQ == 9:
        question9()
    if CurrentQ == 10:
        question10()
    if CurrentQ == 11:
        question11()
    if CurrentQ == 12:
        question12()
    if CurrentQ == 13:
        question13()
    if CurrentQ == 14:
        scorecard()

def clearBoard():
    quest.clear()
    A.clear()
    B.clear()
    C.clear()
    D.clear()

def question1():
    #To change the color of the provided choices:
    A.color("white")
    B.color("white")
    C.color("white")
    D.color("white")
    quest.write("The largest circular storm in our solar\n system is on the surface of?", font=("Arial Narrow", 23, "bold"))
    A.write("A. Jupiter", font=("Arial Narrow", 23, "bold"))
    B.write("B. Venus", font=("Arial Narrow", 23, "bold"))
    C.write("C. Uranus", font=("Arial Narrow", 23, "bold"))
    D.write("D. Earth", font=("Arial Narrow", 23, "bold"))

    global correct
    correct = 'A'

def question2():
    quest.write("The biggest asteroid known is:?", font=("Arial Narrow", 23, "bold"))
    A.write("A. Vesta", font=("Arial Narrow", 23, "bold"))
    B.write("B. Icarus", font=("Arial Narrow", 23, "bold"))
    C.write("C. Ceres", font=("Arial Narrow", 23, "bold"))
    D.write("D. Eros", font=("Arial Narrow", 23, "bold"))
    global correct
    correct = 'C'

def question3():
    quest.write("Rounded to the nearest day, the\n Mercurian year is equal to?", font=("Arial Narrow", 23, "bold"))
    A.write("A. 111 days", font=("Arial Narrow", 23, "bold"))
    B.write("B. 88 days", font=("Arial Narrow", 23, "bold"))
    C.write("C. 50 days", font=("Arial Narrow", 23, "bold"))
    D.write("D. 25 days", font=("Arial Narrow", 23, "bold"))
    global correct
    correct = 'B'

def question4():
    quest.write("One of the largest volcanos in\n our solar system is located on?", font=("Arial Narrow", 23, "bold"))
    A.write("A. Jupiter's Callisto", font=("Arial Narrow", 23, "bold"))
    B.write("B. Venus", font=("Arial Narrow", 23, "bold"))
    C.write("C. Titan(Saturn)", font=("Arial Narrow", 23, "bold"))
    D.write("D. Mars", font=("Arial Narrow", 23, "bold"))
    global correct
    correct = 'D'

def question5():
    quest.write("One Jupiter day is equal to what?", font=("Arial Narrow", 23, "bold"))
    A.write("A. 30 hrs 40 min", font=("Arial Narrow", 23, "bold"))
    B.write("B. 9 hrs 50 min", font=("Arial Narrow", 23, "bold"))
    C.write("C. 3 hrs 20 min", font=("Arial Narrow", 23, "bold"))
    D.write("D. 52 hrs 10 min", font=("Arial Narrow", 23, "bold"))
    global correct
    correct = 'B'

def question6():
    quest.write("The sunspot cycle is?", font=("Arial Narrow", 23, "bold"))
    A.write("A. 3 years", font=("Arial Narrow", 23, "bold"))
    B.write("B. 11 years", font=("Arial Narrow", 23, "bold"))
    C.write("C. 26 years", font=("Arial Narrow", 23, "bold"))
    D.write("D. 49 years", font=("Arial Narrow", 23, "bold"))
    global correct
    correct = 'B'

def question7():
    quest.write("The andromeda Galaxy is which\n of the following types of galaxies?", font=("Arial Narrow", 23, "bold"))
    A.write("A. elliptical", font=("Arial Narrow", 23, "bold"))
    B.write("B. spiral", font=("Arial Narrow", 23, "bold"))
    C.write("C. barred-spiral", font=("Arial Narrow", 23, "bold"))
    D.write("D. irregular", font=("Arial Narrow", 23, "bold"))
    global correct
    correct = 'B'

def question8():
    quest.write("About how many light years\n across is the Milky Way?", font=("Arial Narrow", 23, "bold"))
    A.write("A. 1000", font=("Arial Narrow", 23, "bold"))
    B.write("B. 10000", font=("Arial Narrow", 23, "bold"))
    C.write("C. 100000", font=("Arial Narrow", 23, "bold"))
    D.write("D. 1000000", font=("Arial Narrow", 23, "bold"))
    global correct
    correct = 'C'

def question9():
    quest.write("Smallest planet in our solar system?", font=("Arial Narrow", 23, "bold"))
    A.write("A. Pluto", font=("Arial Narrow", 23, "bold"))
    B.write("B. Jupiter", font=("Arial Narrow", 23, "bold"))
    C.write("C. Mars", font=("Arial Narrow", 23, "bold"))
    D.write("D. Saturn", font=("Arial Narrow", 23, "bold"))
    global correct
    correct = 'A'

def question10():
    quest.write("The first man to classify\n stars based on their brightness?", font=("Arial Narrow", 23, "bold"))
    A.write("A. Aristarchus", font=("Arial Narrow", 23, "bold"))
    B.write("B. Pythagorus", font=("Arial Narrow", 23, "bold"))
    C.write("C. Copernicus", font=("Arial Narrow", 23, "bold"))
    D.write("D. Hipparchus", font=("Arial Narrow", 23, "bold"))
    global correct
    correct = 'D'

def question11():
    quest.write("How many stars are there in Milky Way?", font=("Arial Narrow", 23, "bold"))
    A.write("A. 10 billion", font=("Arial Narrow", 23, "bold"))
    B.write("B. 40 billion", font=("Arial Narrow", 23, "bold"))
    C.write("C. 200 billion", font=("Arial Narrow", 23, "bold"))
    D.write("D. 800 billion", font=("Arial Narrow", 23, "bold"))
    global correct
    correct = 'A'

def question12():
    quest.write("A comet's tail points in which direction?", font=("Arial Narrow", 23, "bold"))
    A.write("A. toward the sun", font=("Arial Narrow", 23, "bold"))
    B.write("B. toward the earth", font=("Arial Narrow", 23, "bold"))
    C.write("C. behind the comet", font=("Arial Narrow", 23, "bold"))
    D.write("D. away from the sun", font=("Arial Narrow", 23, "bold"))
    global correct
    correct = 'D'



def question13():
    quest.write("Scientists can see stars in which region:", font=("Arial Narrow", 23, "bold"))
    A.write("A. visual", font=("Arial Narrow", 23, "bold"))
    B.write("B. radio", font=("Arial Narrow", 23, "bold"))
    C.write("C. ultraviolet", font=("Arial Narrow", 23, "bold"))
    D.write("D. x-ray", font=("Arial Narrow", 23, "bold"))
    global correct
    correct = 'A'
def scorecard():
    quest.color("#3BDF27")
    quest.write("Progress Recorded.\nPress 'E' to exit. BYE!", font=("Arial Narrow", 23, "bold"))
    A.write(" ¯\_(ツ)_/¯ ", font=("Arial Narrow", 23, "bold"))
    B.write(" ಠ_ಠ ", font=("Arial Narrow", 23, "bold"))
    C.write(" ( ͡ᵔ ͜ʖ ͡ᵔ ) ", font=("Arial Narrow", 23, "bold"))
    D.write(" (づ｡◕‿‿◕｡)づ ", font=("Arial Narrow", 23, "bold"))
    global correct
    correct = 'A'
# Key Bindings
window.listen()
window.onkeypress(chooseAnswerA, "a")
window.onkeypress(chooseAnswerB, "b")
window.onkeypress(chooseAnswerC, "c")
window.onkeypress(chooseAnswerD, "d")
window.onkey(exit_game, "e")


# Start Game
question1()
input()
