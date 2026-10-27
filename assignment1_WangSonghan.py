from turtle import *

def draw_square():
  speed(3)
  bgcolor("White")
  pensize(10)
  penup()
  goto(-200, -200)
  pendown()
  goto(-200, -140)
  goto(-140, -140)
  goto(-140, -200)
  goto(-200, -200)
  

def draw_sunflower():
  speed(20)
  bgcolor("White")
  pensize(3)
  color("#E67E22", "#FFA726")
  for angle in range (0, 360, 30):
    penup()
    goto(0,50)
    seth(angle)
    forward(45)
    seth(angle - 45)
    pendown()
    begin_fill()
    circle(35, 90)
    left(90)
    circle(35, 90)
    end_fill()
  
  penup()
  goto(0, 0)
  seth(0)
  color("#D35400", "#FFEB3B")
  pendown()
  begin_fill()
  circle(50)
  end_fill()
  
def bot():
  keyword = ["Hello", "HKU", "robot", "jetson", "ai", "human", "name"]
  print("Question Answering Bot")
  while(1):
	  question = input("Ask me something: ")
	  if keyword[0].lower() in question.lower():
	    print("Bot: Hello! Nice to meet you.")
	  elif keyword[1].lower() in question.lower():
	    print("Bot: HKU means The University of Hong Kong, a research university located in Hong Kong.")
	  elif keyword[2].lower() in question.lower():
	    print("Bot: Robot is an automatic machine device designed to perform tasks.")
	  elif keyword[3].lower() in question.lower():
	    print("Bot: Jetson Nano is an AI computer.")
	  elif keyword[4].lower() in question.lower():
	    print("Bot: AI means artificial intelligence.")
	  elif keyword[5].lower() in question.lower():
	    print("Bot: Human is a species with intelligence.")
	  elif keyword[6].lower() in question.lower():
	    print("Bot: My name is python bot.")
	  else:
	    print("Bot: Sorry, I don't understand.")



draw_square()
draw_sunflower()
bot()
done()
