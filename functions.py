def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local