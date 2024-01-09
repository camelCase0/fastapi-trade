from email.message import EmailMessage
import smtplib
from celery import Celery
from config import REDIS_HOST, REDIS_PORT, SMTP_PASS, SMTP_USER

SMTP_HOST="smtp.gmail.com"
SMTP_PORT="465"

celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')

def get_email_template(username:str):
    email = EmailMessage()
    email['subject'] = "Test"
    email['from'] = SMTP_USER
    email['to'] = SMTP_USER

    email.set_content(
        '<div>'
        f'<h1>Hello dear {username}</h1>'
        '</div>',
        subtype='html'
    )
    return email

@celery.task
def send_email_report(username:str):
    email = get_email_template(username)
    with smtplib.SMTP_SSL(SMTP_HOST,SMTP_PORT) as server:
        server.login(SMTP_USER,SMTP_PASS)
        server.send_message(email)