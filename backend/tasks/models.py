from django.db import models


# Create your models here.
class Task(models.Model):
    status_choices = [
        ("To Do", "To Do"),
        ("In Progress", "In Progress"),
        ("Done", "Done"),
        ("Canceled", "Canceled"),
        ("Overdue", "Overdue"),
        ("Paused", "Paused"),
    ]

    priority_choices = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=status_choices, default="To Do")
    priority = models.CharField(max_length=30, choices=priority_choices, default="Low")
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_user = models.ForeignKey("users.CustomUser", on_delete=models.SET_NULL, null=True, related_name="tasks")
    author_user = models.ForeignKey(
        "users.CustomUser", on_delete=models.SET_NULL, null=True, related_name="created_tasks"
    )

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200)
    tasks = models.ManyToManyField(Task, related_name="tags")

    def __str__(self):
        return self.name


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    user = models.ForeignKey("users.CustomUser", on_delete=models.SET_NULL, null=True, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.task.title}"


class Attachment(models.Model):
    fileUrl = models.URLField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="attachments")
    user = models.ForeignKey("users.CustomUser", on_delete=models.SET_NULL, null=True, related_name="attachments")
    created_at = models.DateTimeField(auto_now_add=True)
    fileName = models.CharField(max_length=200)

    def __str__(self):
        return f"Attachment for {self.task.title}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tasks = models.ManyToManyField(Task, related_name="projects")
    users = models.ManyToManyField("users.CustomUser", related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField("users.CustomUser", related_name="teams")
    projects = models.ManyToManyField(Project, related_name="teams")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
