from celery import shared_task
from time import sleep


@shared_task
def sendemail():
    sleep(3)
    print("email sent to dispatch!")
