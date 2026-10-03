def sort_todos(todos, result=None):
    result = list(todos) if result is None else result
    result.sort(key=lambda todo: (todo["priority"], todo["id"]))
    return result


def filter_todos(todos, status):
    if status == "done":
        return [todo for todo in todos if todo["done"] == 1]
    if status == "pending":
        return [todo for todo in todos if todo["done"] == 0]
    return list(todos)


def format_title(title):
    if title:
        return title.strip().title()
    return title
