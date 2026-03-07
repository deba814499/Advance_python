#freelancer marketing system

class Freelancer:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def show_profile(self):
        print("Freelancer:", self.name)
        print("Skill:", self.skill)


class Client:
    def __init__(self, name, company):
        self.name = name
        self.company = company


class Project:
    def __init__(self, title, budget):
        self.title = title
        self.budget = budget
        self.status = "Pending"

    def update_status(self, status):
        self.status = status


freelancer = Freelancer("Debasis", "Python Developer")

client1 = Client("Rahul", "TechSoft")

project1 = Project("Website Development", 20000)

freelancer.show_profile()

print("\nClient:", client1.name)
print("Company:", client1.company)

print("\nProject:", project1.title)
print("Budget:", project1.budget)

project1.update_status("Completed")

print("Project Status:", project1.status)