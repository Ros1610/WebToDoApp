import streamlit as st
import functions

todos = functions.read_file("todos.txt")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo.strip().capitalize())
    functions.write_file(todos)


st.title("My TO-DO App")
st.subheader("Manage your TO-DOs easily!")

checkboxes = dict()
for index, todo in enumerate(todos):
    checkbox = (st.checkbox(todo, key=todo))
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input("", placeholder="Enter a to-do", key="new_todo")

st.button("Add", on_click=add_todo)

st.session_state