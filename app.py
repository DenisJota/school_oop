from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from aluno import Student

class App:
    def __init__(self):
        self.window = Tk()
        self.students = []
        self.window.title("Student Registration")

        self.label_studentID = Label(self.window, text="Student ID: ", font="tahoma 14 bold",
                                     fg="black", bg="grey")
        self.label_studentID.grid(row=0, column=0)
        self.txt_studentID = Entry(self.window, font="Tahoma 14 ", width=27, state=DISABLED)
        self.txt_studentID.grid(row=0, column=1)

        self.label_name = Label(self.window, text="Name: ", font="tahoma 14 bold",
                                     fg="black", bg="grey")
        self.label_name.grid(row=1, column=0)
        self.txt_name = Entry(self.window, font="Tahoma 14 ", width=27)
        self.txt_name.grid(row=1, column=1)

        self.label_age = Label(self.window, text="Age: ", font="tahoma 14 bold",
                                     fg="black", bg="grey")
        self.label_age.grid(row=2, column=0)
        self.txt_age = Entry(self.window, font="Tahoma 14 ", width=27)
        self.txt_age.grid(row=2, column=1)

        self.label_course = Label(self.window, text="Course: ", font="tahoma 14 bold",
                               fg="black", bg="grey")
        self.label_course.grid(row=3, column=0)
        self.courses = ['Python', 'Javascript', 'HTML&CSS', 'React']
        self.combo_course = ttk.Combobox(self.window, values=self.courses, width=25, font="Tahoma 14")
        self.combo_course.grid(row=3, column=1)

        self.label_grade = Label(self.window, text="Grade: ", font="tahoma 14 bold",
                                     fg="black", bg="grey")
        self.label_grade.grid(row=4, column=0)
        self.txt_grade = Entry(self.window, font="Tahoma 14 ", width=27)
        self.txt_grade.grid(row=4, column=1)

        self.button_submit = Button(self.window, text="Submit",
                                       font="Tahoma 12 bold", width=7, fg="black", command=self.submitStudent)
        self.button_submit.grid(row=5, column=0)

        self.button_edit = Button(self.window, text="Edit",
                                    font="Tahoma 12 bold", width=7, fg="black", command=self.editStudent)
        self.button_edit.grid(row=5, column=1)

        self.button_delete = Button(self.window, text="Delete",
                                     font="Tahoma 12 bold", width=7, fg="red", command=self.deleteStudent)
        self.button_delete.grid(row=5, column=2)

        self.frame = Frame(self.window)
        self.frame.grid(row=6, column=0, columnspan=3)
        self.columns = ['Student ID', 'Name', 'Age', 'Course', 'Grade']
        self.table = ttk.Treeview(self.frame, columns=self.columns, show="headings")
        for column in self.columns:
            self.table.heading(column, text=column)
        self.table.bind('<ButtonRelease-1>',self.selectRow)
        self.table.pack()

        self.window.mainloop()

    def deleteStudent(self):
        studentID = self.txt_studentID.get()
        for student in self.students:
            if str(student.studentID) == studentID:
                self.students.remove(student)
        self.listStudents()
        self.clearFields()
        messagebox.showinfo('Success!', 'Student removed successfully!')

    def editStudent(self):
        studentID = self.txt_studentID.get()
        for student in self.students:
            if str(student.studentID) == studentID:
                student.name = self.txt_name.get()
                student.age = int(self.txt_age.get())
                student.course = self.combo_course.get()
                student.grade = float(self.txt_grade.get())
        self.clearFields()
        self.listStudents()
        messagebox.showinfo('Success!', 'Data changed successfully!')


    def createStudent(self):
        name = self.txt_name.get()
        age = int(self.txt_age.get())
        course = self.combo_course.get()
        grade = float(self.txt_grade.get())
        student = Student(name, age, course, grade)
        return student

    def submitStudent(self):
        student = self.createStudent()
        self.students.append(student)
        messagebox.showinfo('Success', 'Student added successfully!')
        self.clearFields()
        self.listStudents()

    def clearFields(self):
        self.txt_studentID.config(state=NORMAL)
        self.txt_studentID.delete(0, END)
        self.txt_studentID.config(state=DISABLED)
        self.txt_name.delete(0, END)
        self.txt_age.delete(0, END)
        self.combo_course.set("")
        self.txt_grade.delete(0, END)

    def selectRow(self, event):
        self.clearFields()
        selected_row = self.table.selection()[0]
        student = self.table.item(selected_row)['values']
        self.txt_studentID.config(state=NORMAL)
        self.txt_studentID.delete(0, END)
        self.txt_studentID.insert(0, str(student[0]))
        self.txt_studentID.config(state=DISABLED)
        self.txt_name.delete(0, END)
        self.txt_name.insert(0, student[1])
        self.txt_age.delete(0, END)
        self.txt_age.insert(0, student[2])
        self.combo_course.set(student[3])
        self.txt_grade.delete(0, END)
        self.txt_grade.insert(0, str(student[4]))

    def listStudents(self):
        # Clear the table rows
        for row in self.table.get_children():
            self.table.delete(row)

        for student in self.students:
            self.table.insert("", END, values=(student.studentID,
                                               student.name,
                                               student.age,
                                               student.course,
                                               student.grade))


if __name__ == "__main__":
    App()
