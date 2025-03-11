from django.db import models


# Create your models here.
class Task(models.Model):
    class StatusChoices(models.TextChoices):
        TO_DO = "To Do", "To Do"
        IN_PROGRESS = "In Progress", "In Progress"
        DONE = "Done", "Done"
        CANCELED = "Canceled", "Canceled"
        OVERDUE = "Overdue", "Overdue"
        PAUSED = "Paused", "Paused"

    class PriorityChoices(models.TextChoices):
        LOW = "Low", "Low"
        MEDIUM = "Medium", "Medium"
        HIGH = "High", "High"

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=StatusChoices.choices, default="To Do")
    priority = models.CharField(max_length=30, choices=PriorityChoices.choices, default="Low")
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned = models.ForeignKey(
        "users.CustomUser", on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned"
    )
    owner = models.ForeignKey("users.CustomUser", on_delete=models.SET_NULL, null=True, related_name="owner")

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
    user = models.ForeignKey("users.CustomUser", on_delete=models.SET_NULL, null=True, related_name="comment_author")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.task.title}"


class Attachment(models.Model):
    fileUrl = models.URLField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="attachments")
    user = models.ForeignKey("users.CustomUser", on_delete=models.SET_NULL, null=True, related_name="attachment_owner")
    created_at = models.DateTimeField(auto_now_add=True)
    fileName = models.CharField(max_length=200)

    def __str__(self):
        return f"Attachment for {self.task.title}"
