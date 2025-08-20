from multiplequestion import Question

question_prompts = [
    "what color are pineapple?\n(a) Red/Green\n(b) Purple\n(c) Yellow\n\n",
    "what color are bananas?\n(a) Teal \n(b) Magenta\n(c)  Yellow\n\n",
    "what color are strawberries?\n (a) Yellow\n(b) Red\n(c) Blue\n\n"
]
questions = [
    Question(question_prompts[0],"c"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower().strip() == question.answer:
            score += 1
    print("You got "+ str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)