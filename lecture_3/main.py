def addStudent(list):
    name = input("Enter student name:")
    for student in list:
        if student["name"].lower() == name.lower():
            print("This student already exist.")
            return
    newStudent = {"name": name, "grades": []}

    list.append(newStudent)

def gradeStudent(list):
    name = input("Enter student name:")

    foundStudent = None

    for student in list:
        if student["name"].lower() == name.lower():
            foundStudent = student
            break

    if foundStudent == None:
        print("Student not found.")
        return
    else:
        while(True):
            grade = (input("Enter a grade (or 'done' to finish): "))

            if(grade == "done"):
                break

            try:
                grade = int(grade)
                if(grade >= 0 and grade <= 100):
                    foundStudent["grades"].append(grade)
                else:
                    print("Num must be beetween 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

def desplay(list):
    if not list:
        print("List is empty.")
        return

    allAverages = []

    for student in list:
        name = student["name"]
        grades = student["grades"]

        try:
            average = sum(grades) / len(grades)
            print(f"{name}'s average grade is {average:.2f}")

            allAverages.append(average)
        except ZeroDivisionError:
            print(f"{name}'s average grade is N/A.")

    if allAverages:
        maxA = max(allAverages)
        minA = min(allAverages)
        overallA = sum(allAverages) / len(allAverages)

        print(f"Max Average: {maxA:.2f}")
        print(f"Min Average: {minA:.2f}")
        print(f"Overall Average: {overallA:.2f}")
    else:
        print("No grades available")

def findTop(list):
    if not list:
        print("No students available.")
        return
    students_with_grades = []

    for s in list:
        if len(s["grades"]) > 0:
            students_with_grades.append(s)

    if not students_with_grades:
        print("No grades recorded yet.")
        return

    topStudent = max(students_with_grades, key=lambda s: sum(s["grades"]) / len(s["grades"]))

    highestAvg = sum(topStudent["grades"]) / len(topStudent["grades"])

    print(f"The student with the highest average is {topStudent['name']} with a grade if {highestAvg:.2f}.")




def main():
    listOfStudent = []

    while(True):
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")

        try:
            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    addStudent(listOfStudent)
                case 2:
                    gradeStudent(listOfStudent)
                case 3:
                    desplay(listOfStudent)
                case 4:
                    findTop(listOfStudent)
                case 5:
                    print("Exiting program.")
                    break
        except ValueError:
            print("Invalid input. Please enter a number.")




if __name__ == "__main__":
    main()