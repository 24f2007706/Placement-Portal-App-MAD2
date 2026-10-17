import os
from flask import Flask , request ,jsonify
from datetime import date
from flask_cors import CORS
from flask import send_from_directory
from models import db,User,PlacementDrive,ApprovedDrive,StudentApplication,ApplicationHistory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///" + os.path.join(BASE_DIR, "placement.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['JWT_SECRET_KEY']= 'secret-jwt-key'


#for esume 
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "uploads"
)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


CORS(app)
db.init_app(app)

# jwt setup 
jwt = JWTManager(app)

with app.app_context():
    db.create_all()
    if not User.query.filter_by(username = 'admin').first():
        admin = User(username = 'admin', password = generate_password_hash('admin'), email = 'admin@gmail.com', roles = 'admin')
        db.session.add(admin)
        db.session.commit()

#search functionality
@app.route('/api/search/<string:name>')
@jwt_required() 
def search_user(name):
    users = User.query.filter(
        User.username.ilike(f"%{name}%")
    ).all()

    data = []
    for user in users:
        data.append({"id": user.id, "username": user.username, "email": user.email, "role": user.roles})
    return jsonify(data)

@app.route('/api/register', methods=["POST"])
def register():
    data = request.get_json()
    if User.query.filter_by(username = data['username']).first():
        return jsonify({'message' : 'username is already registered'}), 200
    
    user = User(
        username = data['username'],
        password = generate_password_hash(data['password']),
        email = data['email'],
        roles = 'student',
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({'message' : 'student registered successfully'}), 200

#company registration
@app.route('/api/company/register', methods=["POST"])
def company_register():
    data = request.get_json()

    if User.query.filter_by(username = data['username']).first():
        return jsonify({'message' : 'username is already registered'}), 200
    
    user = User(
        username = data['username'],
        password = generate_password_hash(data['password']),
        email = data['email'],
        roles = 'company',
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({'message' : 'company registered successfully'}), 200

#student login
@app.route('/api/login', methods=['POST'])
def student_login():
    data = request.get_json()
    user = User.query.filter_by(username = data['username']).first()

    if user and check_password_hash(user.password, data['password']) and user.roles=='student':

        access_token = create_access_token(identity = str(user.id),additional_claims={'roles':user.roles})
        return jsonify({'message' : 'Student Login successfull', 'data' : {'username' : user.username, 'email' : user.email, 'roles' : user.roles , 'access_token' : access_token}}), 200 
    
    return jsonify({'message' : 'Student Login failed'}), 401
    
#company login
@app.route('/api/company/login',methods=['POST'])
def company_login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.password, data['password']) and user.roles=='company':
        access_token = create_access_token(identity = str(user.id), additional_claims={'roles':user.roles})
        return jsonify({'message' : 'company login successfull', 'data' : {'username' : user.username, 'email' : user.email, 'roles' : user.roles , 'access_token' : access_token}}), 200 

    return jsonify({'message' : 'invalid company credentials'}), 401

#admin login
@app.route('/api/admin/login',methods=['POST'])
def admin_login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.password,data['password']) and user.roles=='admin':
        access_token = create_access_token(identity = str(user.id), additional_claims={'roles':user.roles})
        return jsonify({'message' : 'admin login successfull', 'data' : {'username' : user.username, 'email' : user.email, 'roles' : user.roles , 'access_token' : access_token}}), 200 
    

    return jsonify({'message' : 'invalid admin credentials'})

#admin dashboard
@app.route('/api/admindashboard',methods=['GET'])
@jwt_required()
def admin_dashboard():
    return {
        "message": "Welcome Admin"
    }

#student dashboard
@app.route('/api/studentdashboard', methods=['GET'])
@jwt_required()
def student_dashboard():

    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }

#company dashboard
@app.route('/api/companydashboard', methods=['GET'])
@jwt_required()
def company_dashboard():
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }


#student edit profile
@app.route('/api/editprofile', methods=['PUT'])
@jwt_required()
def edit_profile():

    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username:
        return {"message": "Username required"}, 400

    existing_user = User.query.filter_by(username=username).first()

    if existing_user and existing_user.id != user.id:
        return {"message": "Username already exists"}, 400

    user.username = username
    user.password = generate_password_hash(password)

    db.session.commit()

    return {"message": "Profile Updated"}

#student history
@app.route('/api/studenthistory', methods=['GET'])
@jwt_required()
def student_history():
    student_id = int(get_jwt_identity())

    history = ApplicationHistory.query.filter_by(student_id=student_id).all()

    data = []
    for item in history:
        data.append({"job_title": item.job_title, "status": item.status})

    return jsonify(data)

# company createdrives
@app.route("/api/createdrives", methods=["POST"])
@jwt_required() 
def create_drive():

    data = request.get_json()
    print(data)

    drive = PlacementDrive(
        company_id=int(get_jwt_identity()),
        drive_name=data["drive_name"],
        job_title=data["job_title"],
        job_description=data["job_description"],
        eligibility_criteria=float(data["eligibility_criteria"]),
        application_deadline=date.fromisoformat(
            data["application_deadline"]
        ),
    )
    db.session.add(drive)
    db.session.commit()

    return jsonify({
        "message": "Drive created successfully"
    })

#display all students who applied for that specific drive 
# Flask API

@app.route('/api/appliedstudents/<int:id>')
@jwt_required()
def applied_students(id):
    applications = StudentApplication.query.filter_by(drive_id=id).all()

    students = []
    for application in applications:
        student = User.query.get(application.student_id)
        if student is None:
            continue

        if student.roles == "student":
            students.append({
                "id": student.id,
                "application_id": application.id,
                "username": student.username,
                "email": student.email
            })
    return jsonify(students)

#reject application
@app.route('/api/reject/<int:id>', methods=['POST'])
@jwt_required()
def reject_student(id):
    application = StudentApplication.query.get(id)

    if not application:
        return jsonify({"message": "Application not found"}), 404
    
    drive = ApprovedDrive.query.get(application.drive_id)
    history = ApplicationHistory(
        student_id=application.student_id,
        drive_id=application.drive_id,
        job_title=drive.job_title,
        status="Rejected"
    )
    db.session.add(history)
    db.session.delete(application)
    db.session.commit()

    return jsonify({
        "message": "Student Rejected"
    })


#accept application
@app.route('/api/accept/<int:id>', methods=['POST'])
@jwt_required()
def accept_student(id):
    application = StudentApplication.query.get(id)

    if not application:
        return jsonify({"message": "Application not found"}), 404
    
    drive = ApprovedDrive.query.get(application.drive_id)
    history = ApplicationHistory(
        student_id=application.student_id,
        drive_id=application.drive_id,
        job_title=drive.job_title,
        status="Accepted"
    )

    db.session.add(history)
    db.session.delete(application)
    db.session.commit()

    return jsonify({
        "message": "Student Accepted"
    })

#viewing resume
@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"],filename)

@app.route('/api/resume/<int:id>')
@jwt_required() 
def get_resume(id):
    application = StudentApplication.query.get(id)

    if application is None:
        return jsonify({"message": "Application not found"}), 404
    
    return jsonify({"resume": application.resume})

#display all registered companies admin
@app.route('/api/registeredcompanies')
@jwt_required()
def registered_companies():
    users = User.query.filter_by(roles="company").all()

    data = []
    for user in users:
        data.append({"id": user.id, "username": user.username, "email": user.email})
    return jsonify(data)

#ongoing drives
@app.route('/api/ongoingdrives')
@jwt_required()
def ongoing_drives():
    drives = ApprovedDrive.query.all()

    data = []
    for drive in drives:
        data.append({
            "id": drive.id,
            "drive_name": drive.drive_name,
            "job_title": drive.job_title,
            "eligibility_criteria": drive.eligibility_criteria,
            "application_deadline": drive.application_deadline})

    return jsonify(data)

#remove user
@app.route('/api/removeuser/<int:id>', methods=['DELETE'])
@jwt_required()
def remove_user(id):
    user = User.query.get(id)

    if user is None:
        return jsonify({"message": "User not found"}), 404

    if user.roles == "student":
        StudentApplication.query.filter_by(student_id=id).delete()
        ApplicationHistory.query.filter_by(student_id=id).delete()
    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User Removed Successfully"}), 200

#stuents applications
@app.route('/api/studentapplications')
@jwt_required()
def student_applications():
    applications = StudentApplication.query.all()

    data = []
    for application in applications:
        student = User.query.get(application.student_id)
        drive = ApprovedDrive.query.get(application.drive_id)

        if student is None:
            continue

        if drive is None:
            continue

        data.append({
            "id": application.id,
            "student_name": student.username,
            "job_title": drive.job_title,
            "resume": application.resume})

    return jsonify(data)

#close drive
@app.route('/api/closedrive/<int:id>', methods=['DELETE'])
@jwt_required() 
def close_drive(id):
    drive = ApprovedDrive.query.get(id)

    if drive is None:
        return jsonify({"message": "Drive not found"}), 404

    db.session.delete(drive)
    db.session.commit()

    return jsonify({"message": "Drive Closed Successfully"}), 200

#companydata of all available drives for students to apply
@app.route('/api/companydata/<int:company_id>', methods=['GET'])
@jwt_required() 
def company_data(company_id):
    company = User.query.get(company_id)
    drives = ApprovedDrive.query.filter_by(company_id=company_id).all()

    drive_list = []
    for drive in drives:
        drive_list.append({
            "id": drive.id,
            "drive_name": drive.drive_name,
            "application_deadline": str(drive.application_deadline)
        })
    return jsonify({"company_name": company.username,"drives": drive_list})

# get all registered students  admin page
@app.route('/api/registeredstudents')
@jwt_required() 
def registered_students():
    users = User.query.filter_by(roles="student").all()
    data = []
    for user in users:
        data.append({"id": user.id,"username": user.username,"email": user.email})
    return jsonify(data)

#all approved companies in student dashboard companies button
@app.route('/api/companies', methods=['GET'])
@jwt_required() 
def companies():
    approved_drives = ApprovedDrive.query.all()

    companies = []
    seen_companies = set()
    for drive in approved_drives:
        if drive.company_id not in seen_companies:
            user = User.query.get(drive.company_id)
            if user:
                companies.append({"id": user.id,"company_name": user.username})
                seen_companies.add(drive.company_id)
    return jsonify(companies)

#upcommingDrives
@app.route('/api/upcommingdrives/<int:company_id>', methods=['GET'])
@jwt_required() 
def upcoming_drives(company_id):
    drives = ApprovedDrive.query.filter_by(company_id=company_id).all()

    drive_list = []
    for drive in drives:
        drive_list.append({
            "id": drive.id,
            "drive_name": drive.drive_name,
            "application_deadline": str(drive.application_deadline)})
    return jsonify(drive_list)

#appliedStudents company


#company applications admin
@app.route('/api/companyapplications', methods=['GET'])
@jwt_required() 
def company_applications():
    drives = PlacementDrive.query.all()

    drive_list = []
    for drive in drives:
        drive_list.append({
            "id": drive.id,
            "company_id": drive.company_id,
            "drive_name": drive.drive_name,
            "job_title": drive.job_title,
            "application_deadline": drive.application_deadline,})
    return jsonify(drive_list)

#apply for a job ... apply drive student dashboard 
@app.route('/api/viewdrivedetails/<int:drive_id>', methods=['GET'])
@jwt_required() 
def view_drive_details(drive_id):
    drive = ApprovedDrive.query.get(drive_id)

    return jsonify({
        "id": drive.id,
        "drive_name": drive.drive_name,
        "job_title": drive.job_title,
        "job_description": drive.job_description,
        "eligibility_criteria":drive.eligibility_criteria,
        "application_deadline":str(drive.application_deadline)
    })

#approve drive admin
@app.route('/api/approvedrive/<int:id>', methods=['PUT'])
@jwt_required() 
def approve_drive(id):
    drive = PlacementDrive.query.get(id)

    if not drive:
        return jsonify({"message": "Drive not found"}), 404
    
    approved = ApprovedDrive(
        company_id=drive.company_id,
        drive_name=drive.drive_name,
        job_title=drive.job_title,
        job_description=drive.job_description,
        eligibility_criteria=drive.eligibility_criteria,
        application_deadline=drive.application_deadline
    )

    db.session.add(approved)
    db.session.delete(drive)
    db.session.commit()
    return jsonify({"message": "Drive approved"})

#reject drive admin
@app.route('/api/rejectdrive/<int:id>', methods=['DELETE'])
@jwt_required()
def reject_drive(id):
    drive = PlacementDrive.query.get(id)

    if not drive:
        return jsonify({"message": "Drive not found"}), 404
    
    db.session.delete(drive)
    db.session.commit()

    return jsonify({"message": "Drive deleted successfully"})


# this end point is created in jan2026 project session for testing..
@app.route('/',methods=['GET'])
def get_data():
    data = {
        'message' : 'hello from the backend!',
        'items' : [1,2,3,4,5]
    }
    return jsonify(data)

@app.route('/api/applydrive', methods=['POST'])
@jwt_required()
def apply_drive():
    student_id = get_jwt_identity()
    user = User.query.get(student_id)

    drive_id = request.form.get('drive_id')
    resume = request.files.get('resume')

    if user.roles != "student":
        return jsonify({"message":"Only students can apply"}),403

    if not drive_id or not resume:
        return jsonify({"message": "Drive ID and Resume are required"}), 400

    already_applied = StudentApplication.query.filter_by(student_id=student_id, drive_id=drive_id).first()

    if already_applied:
        return jsonify({"message": "Already Applied"}), 400

    resume.save(os.path.join(app.config["UPLOAD_FOLDER"],resume.filename))

    application = StudentApplication(student_id=student_id, drive_id=drive_id, resume=resume.filename)

    db.session.add(application)
    db.session.commit()
    return jsonify({"message": "Applied Successfully"}), 200

if __name__=="__main__":
    app.run(debug=True)