#last modify Officially

import tkinter as tk

class Chatbot:
    def __init__(self, master):
        self.master = master
        self.master.title("Zooba Machine")
        self.current_frame = None
        self.create_welcome_page()

    def create_welcome_page(self):
        self.current_frame = tk.Frame(self.master)
        self.label1 = tk.Label(self.current_frame, text="  Welcome to Zooba Machine  ", font=("Arial", 16))
        self.label1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.start_button = tk.Button(self.current_frame, text="Start", command=self.create_question1_page, bg="#4CAF50", fg="white", font=("Arial", 14), height=2, width=10)
        self.start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.current_frame.place(relwidth=1, relheight=1)

    def create_question1_page(self):
        self.current_frame.destroy()
        self.current_frame = tk.Frame(self.master)
        self.label2 = tk.Label(self.current_frame, text=" Do you have headache or body aches ?  ", font=("Arial", 16))
        self.label2.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.yes_button1 = tk.Button(self.current_frame, text="Yes", command=self.show_answer1, bg="#008CBA", fg="white", font=("Arial", 12), height=2, width=10)
        self.yes_button1.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
        self.no_button1 = tk.Button(self.current_frame, text="No", command=self.show_answer2, bg="#f44336", fg="white", font=("Arial", 12), height=2, width=10)
        self.no_button1.place(relx=0.7, rely=0.5, anchor=tk.CENTER)
        self.next_button1 = tk.Button(self.current_frame, text="Next", state=tk.DISABLED, command=self.create_question2_page, bg="#4CAF50", fg="white", font=("Arial", 14), height=2, width=10)
        self.next_button1.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        self.answer1 = tk.Label(self.current_frame, text="")
        self.answer1.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        self.current_frame.place(relwidth=1, relheight=1)

    def create_question2_page(self):
        self.current_frame.destroy()
        self.current_frame = tk.Frame(self.master)
        self.label3 = tk.Label(self.current_frame, text=" Do you have diarrhea and gastroenteritis ?  ", font=("Arial", 16))
        self.label3.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.yes_button2 = tk.Button(self.current_frame, text="Yes", command=self.show_answer3, bg="#008CBA", fg="white", font=("Arial", 12), height=2, width=10)
        self.yes_button2.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
        self.no_button2 = tk.Button(self.current_frame, text="No", command=self.show_answer4, bg="#f44336", fg="white", font=("Arial", 12), height=2, width=10)
        self.no_button2.place(relx=0.7, rely=0.5, anchor=tk.CENTER)
        self.next_button2 = tk.Button(self.current_frame, text="Next", state=tk.DISABLED, command=self.create_question3_page, bg="#4CAF50", fg="white", font=("Arial", 14), height=2, width=10)
        self.next_button2.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        self.answer2 = tk.Label(self.current_frame, text="")
        self.answer2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        self.current_frame.place(relwidth=1, relheight=1)

    def create_question3_page(self):
        self.current_frame.destroy()
        self.current_frame = tk.Frame(self.master)
        self.label4 = tk.Label(self.current_frame, text=" Do you have cough ?  ", font=("Arial", 16))
        self.label4.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.yes_button3 = tk.Button(self.current_frame, text="Yes", command=self.show_answer5, bg="#008CBA", fg="white", font=("Arial", 12), height=2, width=10)
        self.yes_button3.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
        self.no_button3 = tk.Button(self.current_frame, text="No", command=self.show_answer6, bg="#f44336", fg="white", font=("Arial", 12), height=2, width=10)
        self.no_button3.place(relx=0.7, rely=0.5, anchor=tk.CENTER)
        self.finish_button = tk.Button(self.current_frame, text="Finish", command=self.master.destroy, bg="#4CAF50", fg="white", font=("Arial", 14), height=2, width=10)
        self.finish_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        self.answer3 = tk.Label(self.current_frame, text="")
        self.answer3.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        self.current_frame.place(relwidth=1, relheight=1)

    def show_answer1(self):
        self.answer1.config(text="You Should Take Panadol. ",font=("Arial", 14),fg="white",bg="black")
        self.next_button1.config(state=tk.NORMAL)

    def show_answer2(self):
        self.answer1.config(text=" You Are Good Don't Worry. ",font=("Arial", 14),fg="white",bg="black")
        self.next_button1.config(state=tk.NORMAL)

    def show_answer3(self):
        self.answer2.config(text=" You Should Take Antinal. ",font=("Arial", 14),fg="white",bg="black")
        self.next_button2.config(state=tk.NORMAL)

    def show_answer4(self):
        self.answer2.config(text=" You Are Good Don't Worry. ",font=("Arial", 14),fg="white",bg="black")
        self.next_button2.config(state=tk.NORMAL)

    def show_answer5(self):
        self.answer3.config(text=" You Should Take Profien. ",font=("Arial", 14),fg="white",bg="black")

    def show_answer6(self):
        self.answer3.config(text=" You Are Good Don't Worry. ",font=("Arial", 14),fg="white",bg="black")

if __name__ == "__main__":
    root = tk.Toplevel()
    #chatbot = Chatbot(root)
    root.attributes('-fullscreen', True)
    root.mainloop()
    
