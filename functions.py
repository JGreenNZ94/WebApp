def get_todos():
    with open('ToDo_List.txt', 'r+') as file:
        todo_list = file.readlines()
    return todo_list


def write_todos(todos):
    with open('ToDo_List.txt', 'w') as file:
        file.writelines(todos)





