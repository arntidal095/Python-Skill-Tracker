import os


skills = {}
if not os.path.exists("devv.txt"):
    with open("devv.txt","w") as f:
        f.write("")
if not os.path.exists("dev_tracker.txt"):
    with open("dev_tracker.txt","w") as f:
        f.write("")


with open("devv.txt", "r") as file:
    for line in file:
        skill, progress = line.strip().split(":", 1)  # split only at the first colon
        skills[skill] = int(progress)

def new_skil():
    new_skill = input("Enter new skill: ")
    value = int(input("Enter skill point level: "))

    with open("dev_tracker.txt", "a",encoding="utf-8") as dev:
        if new_skill not in skills:
           dev.write(f"your skill : {new_skill} is at this level: {value}\n")
           with open("devv.txt", "a", encoding="utf-8") as devv:
              devv.write(f"{new_skill}:{value}\n")
           skills[new_skill] = value
        else:
            print("you already have this skill")
def update_skills():
    update_skil = input("Enter skill u will like to update: ")
    value = int(input("Enter new skill point level: "))

    if update_skil not in skills:
        print("you do not have this skill")
    else:
        dev=  open("dev_tracker.txt", "w", encoding="utf-8")
        devv =  open("devv.txt", "w", encoding="utf-8")
        skills[update_skil] = value
        for k,v in skills.items():
            dev.write(f"your new skill : {k} is at this level: {v}\n")
            devv.write(f"{k}:{v}\n")
        dev.close()
        devv.close()

def view_skills():
    with open("dev_tracker.txt", "r", encoding="utf-8") as dev:
        for row in dev:
            print(row.strip())

def most_improved():
    high = max(skills.values())
    for skill, progress in skills.items():
        if high == progress:
            print(f"{skill} is at level {progress}")

def bye():
    print("nice doing business with u")

while True:
    try:
       beg = int(input("1 ➝ Add a new skill,\n 2 ➝ Update progress on an existing skill,\n 3 ➝ View all skills and progress,\n 4 ➝ Find which skill you have improved the most,\n 5 ➝ Exit\n   :"))
    except ValueError:
        print("please enter a valid number")
        continue
    if beg < 1 or beg > 5:
        print("Please enter a number between 1 and 5.")
        continue
    if beg == 1:
       new_skil()
    elif beg == 2:
       update_skills()
    elif beg == 3:
       view_skills()
    elif beg == 4:
       most_improved()
    else:
       bye()
       break








