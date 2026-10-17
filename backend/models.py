from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False , unique=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    roles = db.Column(db.String, nullable=False) #admin or student or company

    placement_drives = db.relationship("PlacementDrive", back_populates="company")
    applications = db.relationship("Application", back_populates="student")

class PlacementDrive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    job_title = db.Column(db.String, nullable=False)
    drive_name = db.Column(db.String, nullable=False)
    job_description = db.Column(db.String , nullable=False)
    eligibility_criteria= db.Column(db.Integer, nullable=False)
    application_deadline = db.Column(db.Date, nullable=False)

    company = db.relationship("User", back_populates="placement_drives")
    applications = db.relationship("Application", back_populates="placement_drive")

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    drive_id = db.Column(db.Integer, db.ForeignKey("placement_drive.id"))
    application_date = db.Column(db.String , nullable=False)##date
    status= db.Column(db.String, nullable=False)

    student = db.relationship("User", back_populates="applications")
    placement_drive = db.relationship("PlacementDrive", back_populates="applications")

class ApprovedDrive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, nullable=False)
    drive_name = db.Column(db.String(100), nullable=False)
    job_title = db.Column(db.String, nullable=False)
    job_description = db.Column(db.String , nullable=False)
    eligibility_criteria= db.Column(db.Integer, nullable=False)
    application_deadline = db.Column(db.Date, nullable=False)

class StudentApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False)
    drive_id = db.Column(db.Integer, nullable=False)
    resume = db.Column(db.String, nullable=False)

class ApplicationHistory(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    student_id = db.Column(db.Integer, nullable=False)
    drive_id = db.Column(db.Integer, nullable=False)
    job_title = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)