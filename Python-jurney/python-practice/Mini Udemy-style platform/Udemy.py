import json


class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.creating_account()

    def creating_account(self):
        data = {
            "name": self.name,
            "email": self.email,
        }
        with open("data.json", "r") as json_file:
            data = json.load(json_file)

        if self.email not in data.values():
            with open("data.json", "w") as json_file:
                json.dump(data, json_file, indent=4)


class Instructor(User):
    """
    let's use inheritance , inherit from the User so instructor also can create account in
	• Instructors can create courses.
	• They can add multiple lessons to each course.
	  Each course stores its creator (instructor) and a list of lessons.
    """

    def __init__(self, name, email):
        super().__init__("", name, email)
        self.courses_created = []  # List to store created courses

    def create_course(self, course_name):
        course = {
            "course_name": course_name,
            "students": []
        }
        self.courses_created.append(course)
        print(f"{course_name} course added successfully ")
        return self.courses_created

    def view_students(self, course_name):
        for course in self.courses_created:
            if course_name == course['course_name']:
                print(f"course name : {course['course_name']} and associate student {course['students']}")
                return
        print(f"No course found with the name of {course_name}")


class student(User):
    def __init__(self, name, email):
        super().__init__("", name, email)

    def view_course(self, course_list):
        print("Below courses are listed in udemy Mini : ")
        for i in course_list:
            print(f"{i['course_name']}")

    def enroll(self, course, all_courses):
        ctr = 0
        for i in all_courses:
            if course in i['course_name']:
                print(f"{self.name} successfully enroll for the {course} course")
                all_courses[ctr]['students'].append(self.name)
                return (all_courses)
            ctr += 1
        print(f"{course}  is not present in the udemy")
        return 0


class Lesson:
    def __init__(self, lesson_id, title, content, duration):
        self.lesson_id = lesson_id
        self.title = title
        self.content = content
        self.duration = duration

    def play_lesson(self):
        print(f"\n📘 Playing Lesson: {self.title}")
        print(f"⏱️ Duration: {self.duration} mins")
        print(f"📝 Content: {self.content}")


class Course:
    def __init__(self, course_id, title, description, instructor):
        self.course_id = course_id
        self.description = description
        self.instructor = instructor
        self.title = title
        self.lessons = []

    def add_lesson(self, lession):
        self.lessons.append(lession)
        print(f"✅ Lesson '{lession.title}' added to course '{self.title}'.")

    def view_course_content(self):
        print(f"\n📚 Course: {self.title} by {self.instructor.name}")
        for i in self.lessons:
            print(f" - Lesson: {i.title} ({i.duration} mins)")


class Platform:
    def __init__(self):
        self.courses = []
        self.users = []

    def register_user(self, user):
        self.users.append(user)
        print(f"✅ Registered user: {user.name} ({user.__class__.__name__})")

    def add_course(self, course):
        self.courses.append(course)
        print(f"✅ Added course: {course.title} by {course.instructor.name}")

    def list_course(self):
        for i in self.courses:
            print(f" - {i.title} (Instructor: {i.instructor.name})")
    def find_course_by_title(self,title):
        for i in self.courses:
            if i.title.lower() == title.lower():
                print(f"✅ Found: {course.title} by {course.instructor.name}")
                return course
        print("❌ Course not found.")
        return None


user_1 = User("", "mayur", "joshi.mayu1234@gmail.com")

instructor1 = Instructor("venky", "venky.millionaire@gmail.com")
all_courses = instructor1.create_course("Python")
all_courses = instructor1.create_course("SQL")
instructor1.view_students("Python")

std_1 = student("mayur", "joshi.mayur4121@gmail.com")
std_1.view_course(all_courses)
all_courses = std_1.enroll("Python", all_courses)

all_courses = std_1.enroll("SQL", all_courses)

instructor1.view_students("Python")
instructor1.view_students("SQL")

course = Course(course_id=1, title="Python Basics", description="Learn Python from scratch", instructor=instructor1)

# Create lessons
lesson1 = Lesson(lesson_id=101, title="Intro to Python", content="Variables, Data Types", duration=10)
lesson2 = Lesson(lesson_id=102, title="Control Flow", content="if, for, while", duration=15)

course.add_lesson(lesson1)
course.add_lesson(lesson2)

lesson1.play_lesson()

# Create platform
udemy_clone = Platform()
udemy_clone.register_user(instructor1)
udemy_clone.register_user(std_1)
udemy_clone.add_course(course)
udemy_clone.find_course_by_title("Python Basics")