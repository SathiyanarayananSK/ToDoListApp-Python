import functions


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    todos = functions.get_todos()

    if user_action.startswith("add"):
        todo = user_action[4:] +"\n"
        todos.append(todo)
        functions.write_todos(todos)


    elif user_action.startswith("show"):
        for index, item in enumerate(todos, start = 1):
            item = item.strip("\n")
            item = item.title()
            print(f"{index}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            new_todo = input("Enter new todo:") + "\n"
            todos[number-1] = new_todo
            functions.write_todos(todos)
        except ValueError or IndexError:
            print("This command is invalid! Type the index of the todo!")
            continue

    elif user_action.startswith("complete"):
       try:
           number = int(user_action[9:])
           todo_to_remove = todos[number-1].strip("\n")
           todos.pop(number - 1)
           print(f"Todo: {todo_to_remove} was removed from the list!")
           functions.write_todos(todos)
       except IndexError:
           print("This command is invalid! Type the index of the todo!")
           continue

    elif user_action.startswith("exit"):
        print("Bye")
        break

    else:
        print("Command is invalid! Please Retry!")


