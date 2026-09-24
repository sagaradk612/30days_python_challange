task=[]
while True:
    print("=== TO DO LIST ===")
    print("""1. Add task
2. View tasks
3. Remove task
4. Exit""")
    choice=input("enter your choices (ex:1) : ")
    if choice == "1":
        input_task=input("enter task : ")
        task.append(input_task)
    
    elif choice == "2":
        print("==== TASK ====")
        print(task)
    elif choice == "3":
        print(task)
        task_remove = input("enter task for remove : ")
        task.remove(task_remove)
    elif choice == "4":
        break
    else:
        print("bye")
        print("unknown error")