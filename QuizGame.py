from tkinter import *
from tkinter import messagebox
import json

font_style = ("times", 20, "bold")

guiWindow = Tk()
guiWindow.title("Quiz Game")
guiWindow.geometry("800x500")
guiWindow.resizable(0, 0)
with open('quiz.json') as file:
    obj = json.load(file)
ques = (obj['questions'])
options = (obj['options'])
ans = (obj['answers'])
# print(ques)
# print(options)
# print(ans)


class QuizGame:
    def __init__(self):

        self.question_number = 0
        self.opt_selected = IntVar()
        self.questions_label = self.question(self.question_number)
        self.opts = self.radiobuttons()
        self.display_options(self.question_number)
        self.buttons()
        self.correct = 0

    def question(self, question_number):
        heading_label = Label(guiWindow, text="Quiz in Python Programming",
                              width=50, bg="blue", fg="white", font=font_style)
        heading_label.pack(padx=0, pady=2)

        question_label = Label(guiWindow, text=ques[question_number], width=60, font=(
            "times", 16, "bold"), anchor=W)
        question_label.pack(padx=70, pady=70)
        return question_label

    def radiobuttons(self):
        val = 0
        option_btn = []
        yp = 150
        while val < 4:
            button = Radiobutton(
                guiWindow, text="", variable=self.opt_selected, value=val+1, font=("times", 14))
            option_btn.append(button)
            button.place(x=100, y=yp)
            val += 1
            yp += 40
        return option_btn

    def display_options(self, question_number):
        val = 0
        self.opt_selected.set(0)
        self.questions_label.config(text=ques[question_number])
        for op in options[question_number]:
            self.opts[val]['text'] = op
            val += 1

    def buttons(self):
        next_btn = Button(guiWindow, text="Next", width=10, bg="green",
                          foreground="white", font=("times", 16, "bold"), command=self.next_button)
        next_btn.place(x=200, y=380)

        quit_btn = Button(guiWindow, text="Quit", width=10, bg="red",
                          foreground="white", font=("times", 16, "bold"), command=guiWindow.destroy)
        quit_btn.place(x=380, y=380)

    def checkans(self, question_number):
        if self.opt_selected.get() == ans[question_number]:
            return True
        else:
            return False

    def next_button(self):
        if self.checkans(self.question_number):
            self.correct += 1
        self.question_number += 1
        if self.question_number == len(ques):
            self.display_result()
        else:
            self.display_options(self.question_number)

    def display_result(self):
        score = int(self.correct/len(ques)*100)
        result = f"Score:{str(score)}%"
        wrong_count = len(ques)-self.correct
        correct_ans = f"No.of correct answers:{str(self.correct)}"
        wrong_ans = f"No.of wrong answers:{str(wrong_count)}"
        messagebox.showinfo("Result", "\n".join(
            [result, correct_ans, wrong_ans]))
        self.play_again()

    def play_again(self):
        choice = messagebox.askyesno(
            "Play again", "Do you want to play again?")
        if choice:
            self.question_number = 0
            self.opt_selected.set(0)
            self.correct = 0
            self.display_options(self.question_number)
        else:
            guiWindow.destroy()


game = QuizGame()
guiWindow.mainloop()
