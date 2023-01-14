import csv
from io import TextIOWrapper
from zipfile import BadZipfile

from apps.todos.serializers import TaskSerializer


def import_tasks(request) -> dict:
    """Import tasks from csv file."""
    if request.data['file'].name.split('.')[-1] != 'csv':
        return {
            'message': 'Файл должен иметь расширение .csv',
        }
    try:
        file = TextIOWrapper(request.FILES['file'].file, encoding=request.encoding)
    except BadZipfile:
        return {
            'message': 'Файл является битым',
        }
    csv_reader = csv.reader(file, delimiter=";")
    append_tasks = []
    for row in csv_reader:
        tasks_data = {
            "name": row[0],
            "description": row[1],
            "is_done": (row[2] == "True"),
        }
        task_serializer = TaskSerializer(data=tasks_data)
        task_serializer.is_valid(raise_exception=True)
        task_serializer.save(user=request.user)
        append_tasks.append(task_serializer.data)
    data = {
        'tasks': append_tasks,
    }
    return data


def export_operation(queryset, filename) -> None:
    """Export tasks from csv file."""
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerows(
            [
                [task.name, task.description, str(task.is_done)]
                for task in queryset
            ]
        )
