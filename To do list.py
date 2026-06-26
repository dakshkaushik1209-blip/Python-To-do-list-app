task=[]
def Add():
    number=1
    while True:
        add=input(f"{number}.Type your task(and \'Exit\' to exit):- ")
        number+=1
        if add.upper()=="EXIT":
            break
        print("Task added sucessfully")
        task.append({"task":add,"done":False})
    
def View():
    number = 1
    for i in task:
        status="❌"
        if i["done"]:
            status="✅"
        print(number,". ",i["task"],status)
        number+=1

def Mark():
    if len(task)==0:
        print("No task available")
        return
    View()
    while True:
        try:
            done=int(input("Enter your task number which you completed:- "))
        except Exception as ex:
            print("Please give the already exists task number")
            continue
        if done<=0 or done>len(task):
            print("Task not found")
            continue

        if task[done-1]["done"]:
            print("Already Done")
            continue
        else:
            task[done-1]["done"]=True
            print("Task mark as completed")  
        
        View()
        break

def Delete():
    View()
    if len(task)==0:
        print("No task available")
        return
    while True:
        try:
            delete=int(input("Enter the number of task which you want to delete:- "))
        except Exception as ex:
            print("Please give the alreasy exists task number")
            continue
        if delete<=0 or delete>len(task):
                print("Task not found")
                continue
        else:
            print("Task deleted sucessfully")
        task.pop(delete-1)
        View()
        break



while True:
    print("Welcome to To-do list")
    print("Add task     Click 1")
    print("View task    Click 2")
    print("Mark Task Completed      Click 3")
    print("Delete Task          Click 4")
    print("Exit             Click 5")
    try:
        choice=int(input("Enter your choice:- "))
    except Exception as ex:
        print("Please select 1,2,3,4 or 5 only")
        continue
    if choice==1:
        Add()
    elif choice == 2:
        View()
    elif choice== 3 :
        Mark()
    elif choice == 4:
        Delete()
    elif choice==5:
        break
    else:
        print("Invalid Input")