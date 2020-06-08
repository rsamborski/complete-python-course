"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""

n = 0

with open("questions.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        (question, answer) = line.strip().split("=")
        user_answer = input("{}=".format(question))
        if user_answer.lower() == answer.lower():
            n = n+1
        # print(f"{question} -> {answer}")

with open("result.txt", "w") as f:
    f.write("Your final score is {}/{}".format(n, len(lines)))
