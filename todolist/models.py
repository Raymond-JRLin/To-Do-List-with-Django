from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True) # detailed description
    completed = models.BooleanField(default=False) # flag of status, default is incompleted, i.e. False
    created_at = models.DateTimeField(auto_now_add=True) # the timestamp when created
    updated_at = models.DateTimeField(auto_now=True) # every timestamp when we update

    class Meta:
        ordering = ('completed', '-updated_at',) # order data as if they are completed, then order them as updating time
