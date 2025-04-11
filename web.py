import streamlit as st
import function


todos = function.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    function.write_todos(todos)


st.title("My todo App")
st.write("This app is to increase your productivity")


for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo......", key="new_todo", on_change=add_todo)
print("hello")
