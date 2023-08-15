#           Python Begineer Boost

#           Daily Journal App

import datetime

#Creating todays date
todaydate = datetime.date.today()

#Opening a file in write mode 
file = open(f"Files/{todaydate}.txt",'w')
file.close()

#Variables to store questions
question1 = "How was your day?"
question2 = "What goals or tasks did you accomplish today?"
question3 = "Did you face any obstacles or challenges today? How did you overcome them?"
question4 = "What is something you learned today?"
question5 = "What's one thing you would like to improve or work on tomorrow?"

#Taking user input for answers 
answer1 = input("How was your day?\n")
answer2 = input("What goals or tasks did you accomplish today?\n")
answer3 = input("Did you face any obstacles or challenges today? How did you overcome them?\n")
answer4 = input("What is something you learned today?\n")
answer5 = input("What's one thing you would like to improve or work on tomorrow?")

#Opening the file in write mode for storing questions and answers 
file = open(f"Files/{todaydate}.txt",'w')
file.write(f"{question1}\n")
file.write(f"{answer1}\n\n")
file.write(f"{question2}\n")
file.write(f"{answer2}\n\n")
file.write(f"{question3}\n")
file.write(f"{answer3}\n\n")
file.write(f"{question4}\n")
file.write(f"{answer4}\n\n")
file.write(f"{question5}\n")
file.write(f"{answer5}\n")
file.close()