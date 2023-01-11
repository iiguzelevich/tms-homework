from config import celery
from config.celery import ErrorLoggingTask
from .models import Post


@celery.app.task(base=ErrorLoggingTask, name='show_test_task')
def show_test_task():
    posts = Post.objects.all()
    for post in posts:
        post.information = post.information + 'INFO'
        post.save()
