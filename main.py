grade_points= {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}
courses= {}
def add_course():
    name= input("Enter Course Name:")
    grade= input("Enter Letter Grade A-F: ").upper()
    credit= int(input("How many credits is the class?: "))
    courses[name]={"grade":grade, "credits":credit}
def calc_gpa():
    total_points=0
    total_credits=0
    for lebron in courses.values():
        grade= lebron["grade"]
        credit=lebron["credits"]
        total_points += grade_points[grade] * credit
        total_credits += credit
    if total_credits==0:
        return 0
    return total_points / total_credits
while True:
    add_course()
    more = input("Add another course? (y/n): ").lower()
    if more != "y":
        break
gpa=calc_gpa()
print(f"Your gpa is: {gpa:.2f}")