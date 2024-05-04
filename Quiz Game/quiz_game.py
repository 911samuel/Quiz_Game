print("Welcome to my computer quiz")
playing = input("Do you want to play? ")
score = 0
total_questions = 0

if playing.lower() == "yes":
    print("Okay let's play 😊 ")

    # Question 1
    total_questions += 1
    answer = input("What is the CPU in full? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Question 2
    total_questions += 1
    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Question 3
    total_questions += 1
    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphics processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Question 4
    total_questions += 1
    answer = input("What is the main function of an operating system? ")
    if answer.lower() == "manage computer hardware and software resources":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Calculate percentage
    percentage = (score / total_questions) * 100
    print("You scored", score, "out of", total_questions, "questions correct.")
    print("Your percentage: {:.2f}%".format(percentage))
else:
    quit()
