import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.write_todos(todos)

def remove_todo():
    todo_to_remove = st.session_state["todo"]
    todos.remove(todo_to_remove)
    functions.write_todos(todos)


st.title("My To-Do App")
st.header("List of To-Do items")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a new todo", on_change=add_todo, key="new_todo")
