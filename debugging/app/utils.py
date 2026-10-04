def sort_assignments(assignments: list) -> list:
    return sorted(assignments, key=lambda a: (a["difficulty"], a["id"]))


def filter_assignments(assignments: list, status: str) -> list:
    if status == "submitted":
        return [a for a in assignments if a["submitted"] == int(1)]
    if status == "pending":
        return [a for a in assignments if a["submitted"] == int(0)]
    return list(assignments)


def format_title(title: str) -> str:
    if title:
        return title.strip().title()
    return title
