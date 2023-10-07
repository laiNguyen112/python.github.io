import tkinter as tk
from tkinter import StringVar
import random

root = tk.Tk()
root.title('Trắc Nghiệm')
root.geometry('700x500')

file_path = "test.txt"

frame = tk.Frame(root, padx=10, pady=10,bg='#fff')
question_label = tk.Label(frame,height=5, width=40,bg='grey',fg="#fff", 
                          font=('Verdana', 20),wraplength=700)

correct_answer_label = tk.Label(frame, text='', font=('Verdana', 16))
correct_answer_label.grid(row=5, column=0)

v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, font=('Verdana', 20),
                         command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option4))

button_next = tk.Button(frame, text='Next',bg='Orange', font=('Verdana', 20), 
                        command = lambda : displayNextQuestion())

frame.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky= 'W', row=1, column=0)
option2.grid(sticky= 'W', row=2, column=0)
option3.grid(sticky= 'W', row=3, column=0)
option4.grid(sticky= 'W', row=4, column=0)

button_next.grid(row=6, column=0)


index = 0
correct = 0
questions = [] 
options = []

def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state

def read_questions_from_file(file_path):
    global questions, options
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            questions.append(lines[i].strip())
            options.append(lines[i + 1].strip().split(','))

def random_questions(num_questions=50):
    global questions, options
    combined = list(zip(questions, options))
    random.shuffle(combined)
    selected_questions = combined[:num_questions]
    questions, options = zip(*selected_questions)

def checkAnswer(radio):
    global correct, index
    
    selected_answer = radio['text']
    correct_answer = options[index][4]  
    
    if selected_answer == correct_answer:
        correct += 1
        correct_answer_label.config(text=f'Correct Answer: {correct_answer}', fg='green')
    else:
        correct_answer_label.config(text=f'Correct Answer: {correct_answer}', fg='red')
    
    index +=1
    disableButtons('disable')

def displayNextQuestion():
    global index, correct

    correct_answer_label.config(text='')


    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'

    if index == len(options):
       question_label['text'] = str(correct) + " / " + str(len(options))
       button_next['text'] = 'Restart The Quiz'
       if correct >= len(options)/2:
            question_label['bg'] = 'green'
       else:
            question_label['bg'] = 'red'


    else:
        question_label['text'] = questions[index]
        
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Check the Results'

read_questions_from_file(file_path)
random_questions(num_questions=50)
displayNextQuestion()

root.mainloop()