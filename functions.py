def get_todos():
    with open('c:/Users/james.green/Documents/PythonScripts/To-Do App/ToDo_List.txt', 'r+') as file:
        todo_list = file.readlines()
    return todo_list


def write_todos(todos):
    with open('c:/Users/james.green/Documents/PythonScripts/To-Do App/ToDo_List.txt', 'w') as file:
        file.writelines(todos)





