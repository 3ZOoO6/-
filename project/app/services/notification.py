from app.extensions import celery
import smtplib
from email.mime.text import MIMEText

@celery.task
def send_email_notification(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'noreply@yourdomain.com'
    msg['To'] = to
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
        server.send_message(msg)
