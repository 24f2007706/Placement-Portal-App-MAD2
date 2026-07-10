from celery_worker import celery_app
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
from datetime import date
from flask import render_template
from models import User, ApplicationHistory, ApprovedDrive

SERVER_SMTP_HOST = os.environ.get("MAIL_SERVER", "localhost")
SERVER_SMTP_PORT = int(os.environ.get("MAIL_PORT", 1025))
SENDER_ADDRESS = "placementcell@gmail.com"

def send_email(to_address, subject, message, content="text"):
    msg = MIMEMultipart()
    msg["From"] = SENDER_ADDRESS
    msg["To"] = to_address
    msg["Subject"] = subject
    if content == "html":
        msg.attach(MIMEText(message, "html"))
    else:
        msg.attach(MIMEText(message, "plain"))
    try:
        print(f"Connecting to SMTP server at {SERVER_SMTP_HOST}:{SERVER_SMTP_PORT}...")
        smtp = smtplib.SMTP(SERVER_SMTP_HOST, SERVER_SMTP_PORT)
        smtp.send_message(msg)
        smtp.quit()
        print(f"SUCCESS: Email sent to {to_address}")
    except Exception as e:
        print(f"CRITICAL SMTP ERROR: Failed to send email to {to_address}. Reason: {e}")

@celery_app.task
def send_monthly_report():
    admin = User.query.filter_by(roles="admin").first()

    if not admin:
        print("No admin found")
        return
    
    history = ApplicationHistory.query.all()
    details = []

    for student in history:
        details.append({"student_id": student.student_id, "job_title": student.job_title, "status": student.status})

    html = render_template("monthly_report.html",details=details)

    send_email(admin.email, "Monthly Placement Activity Report", html, content="html")
    print("Monthly report sent")


@celery_app.task
def send_daily_reminder():
    today = date.today()
    students = User.query.filter_by(roles="student").all()
    drives = ApprovedDrive.query.all()

    for drive in drives:
        days_left = (drive.application_deadline - today).days
        if 0 <= days_left <= 2:
            for student in students:
                html = render_template("daily_reminder.html",student=student,drive=drive)
                send_email(student.email, "Placement Drive Reminder", html, content="html")
    print("Daily reminder completed")