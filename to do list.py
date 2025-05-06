print("welcome to our to do list")
print("\nmenu for to do list")
l=[]
c=0
print("\n1.add\n2.delete\n3.show\n4.task completed\n5.exit")
while True:
    ch=int(input("\nenter your choice:"))
    if ch==1:
        task=input('enter task to add:')
        if task  not in l and task+"✅"  not in l and task+"❎" not in l:
               c+=1
               l.append(task)
               print('task is added successfully')
        else:
            print("task is already in list")
    elif ch==2:
        if c==0:
            print('to do list is empty')
        else:
            task=input('enter task to delete:')
            if task in l:
               c-=1
               l.remove(task)
               print('task is deleted successfully')
            elif task+"✅" or task+"❎" in l:
                c-=1
                if task+"❎" in l:
                    l.remove(task+"❎")
                else:
                    l.remove(task+"✅")
                print('task is deleted successfully')
            else:
                print('task not found in list')
    elif ch==3:
        if c==0:
            print('list is empty')
        else:
            for i in range(0,c):
                print(i+1,")",l[i])
    elif ch==4:
        if c==0:
            print("list is empty")
        else:
            task=input('enter task which is completed:')
            if task in l or task+"✅" in l or task+"❎" in l:
                if task+"✅" in l:
                    print("task already completed")
                elif task in l:
                    l.remove(task)
                    l.append(task+"✅")
                elif task+"❎" in l:
                    l.remove(task+"❎")
                    l.append(task+"✅")
            else:
                    print('task not found in list')
            for i in range(0,c):
                    if not l[i].endswith("✅"):
                        if not l[i].endswith("❎"):
                              l[i]=l[i]+"❎"
    elif ch==5:
        print('thank you')
        break
    else:
        print('wrong choice')


 '''print("Welcome to our To-Do List")
print("\nMenu:\n1. Add Task\n2. Delete Task\n3. Show Tasks\n4. Mark Completed\n5. Exit")

tasks = set()  # Using a set for quick lookups

while True:
    ch = int(input("\nEnter your choice: "))
    
    if ch == 1:
        task = input("Enter task to add: ")
        if task not in tasks:
            tasks.add(task)
            print("Task added successfully!")
        else:
            print("Task already in list.")
    
    elif ch == 2:
        if not tasks:
            print("To-Do List is empty.")
        else:
            task = input("Enter task to delete: ")
            if task in tasks or task+"✅" in tasks or task+"❎" in tasks:
                tasks.discard(task)
                tasks.discard(task+"✅")
                tasks.discard(task+"❎")
                print("Task deleted successfully.")
            else:
                print("Task not found.")
    
    elif ch == 3:
        if not tasks:
            print("To-Do List is empty.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}) {task}")
    
    elif ch == 4:
        if not tasks:
            print("List is empty.")
        else:
            task = input("Enter task completed: ")
            if task in tasks or task+"❎" in tasks:
                tasks.discard(task)
                tasks.discard(task+"❎")
                tasks.add(task+"✅")
                print("Task marked as completed.")
            else:
                print("Task not found.")
    
    elif ch == 5:
        print("Thank you!")
        break
    
    else:
        print("Wrong choice.")
'''       
