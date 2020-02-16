import turtle

wN = turtle.Screen()      #create turtle window
wN.title("Pong by  @rawle_assano")    #creater
wN.bgcolor("black")               #set window color
wN.setup(width=800, height=600)
wN.tracer(0)

##
##choice = input('Enter Rock, Paper Or Scissors?')
##
##if choice == 'Rock':
##    print(choice, end=' ')
##    
##elif choice == 'Paper':
##    print(choice, end=' ')
##
##elif choice == 'Scissors':
##    print(choice, end=' ')

paddle_a = turtle.Turle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("White")
paddle_a.penup()
paddle_a.goto(-350, 0)
