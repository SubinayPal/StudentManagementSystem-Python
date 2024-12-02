# Student Management System in Python (Core)
import pickle

# Class to represent a Student
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Class to manage the Student records
class StudentManagementSystem:
    def __init__(self):
        self.students = self.load_students()

    # Load students from a file
    def load_students(self):
        try:
            with open("students.pkl", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    # Save students to a file
    def save_students(self):
        with open("students.pkl", "wb") as file:
            pickle.dump(self.students, file)

    # Add a new student
    def add_student(self, student):
        self.students.append(student)
        self.save_students()

    # View all students
    def view_students(self):
        if len(self.students) == 0:
            print("No students found.")
        else:
            for student in self.students:
                print(student)

    # Edit a student's details
    def edit_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(f"Editing student: {student}")
                student.name = input("Enter new name: ")
                student.age = int(input("Enter new age: "))
                student.grade = input("Enter new grade: ")
                self.save_students()
                print("Student details updated.")
                return
        print("Student not found.")

    # Delete a student
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()
                print("Student deleted.")
                return
        print("Student not found.")

    # Search for a student
    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(f"Student found: {student}")
                return
        print("Student not found.")

# Main menu to interact with the system
def main_menu():
    system = StudentManagementSystem()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            student = Student(student_id, name, age, grade)
            system.add_student(student)
            print("Student added successfully.")
        
        elif choice == "2":
            system.view_students()
        
        elif choice == "3":
            student_id = input("Enter student ID to edit: ")
            system.edit_student(student_id)
        
        elif choice == "4":
            student_id = input("Enter student ID to delete: ")
            system.delete_student(student_id)
        
        elif choice == "5":
            student_id = input("Enter student ID to search: ")
            system.search_student(student_id)
        
        elif choice == "6":
            print("Exiting the system...")
            break
        
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
