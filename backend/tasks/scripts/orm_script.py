from django.utils import timezone

from models import Task


def run():
    task = Task()
    task.title = "Test 1"
    task.description = "test 1"
    task.status = task.status_choices[0]
    task.priority = "Low"
    task.start_date = timezone.now()
    task.due_date = timezone.now() + timezone.timedelta(days=21)
    task.owner = 
