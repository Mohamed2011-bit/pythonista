from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Todo

@receiver(post_save, sender=User)
def create_user_todos(sender, instance, created, **kwargs):
    if created:
        Todo.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_todos(sender, instance, **kwargs):
    instance.todo.save()
