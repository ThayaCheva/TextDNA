from flask import Flask, request, jsonify
from flask_cors import CORS
#import pyodbc
from scripts.sql import run_sql_query
from scripts.SQL_queries_dynamic.sql_queries import students_in_subject_query, subject_page_query, submissions_for_assignment, submissions_for_student , teacher_page_query
import bcrypt
from scripts.run_ps_script import uploading_assignment
import os


app = Flask(__name__)
CORS(app)

#get student info from DB 
@app.route('/student', methods=['GET'])
def get_student():
    student_id = request.args.get('studentID')
    q = "SELECT * FROM [dbo].[student] WHERE Id = ?"
    query = q.replace("?", str(student_id))
    res =  run_sql_query(query)
    
    formatted_rows = []
    for row in res:
        formatted_row = {
            'Id': row.Id,
            'Name': row.Name
        }
        formatted_rows.append(formatted_row)
    return formatted_rows

#get Assignment Info from DB 
@app.route('/assignment', methods=['GET'])
def get_assignment():
    query = "SELECT * FROM [dbo].[assignment]"
    res =  run_sql_query(query)
    
    formatted_rows = []
    for row in res:
        formatted_row = {
            'Id': row.Id,
            'SubjectId': row.SubjectId
        }
        formatted_rows.append(formatted_row)
    return formatted_rows


@app.route('/login', methods=['GET'])
def get_login():
    login_username = request.args.get('username')
    login_password = request.args.get('password')

    password_q = "SELECT * FROM [dbo].[login] WHERE Username = ?"
    password_query = password_q.replace("?", "'" + str(login_username) + "'", 1) 
    res_pass = run_sql_query(password_query)
    hashed_password = None
    if (len(res_pass) > 0) :
        hashed_password = res_pass[0][1]
        
    q = "SELECT * FROM [dbo].[login] WHERE Username = ? AND Password = ?"
    query = q.replace("?", "'" + str(login_username) + "'", 1) 
    query = query.replace("?", "'" + str(login_password) + "'", 1)

    if hashed_password is not None:
        # Use bcrypt.checkpw to verify the entered password
        if bcrypt.checkpw(login_password.encode('utf-8'), hashed_password.encode('utf-8')):
            q = "SELECT * FROM [dbo].[login] WHERE Username = ? AND Password = ?"
            query = q.replace("?", "'" + str(login_username) + "'", 1) 
            query = query.replace("?", "'" + str(hashed_password) + "'", 1)

    res = run_sql_query(query)


    formatted_rows = []
    for row in res:
        formatted_row = {
            'Id': row.Id,
            'Username': row.Username
        }
        formatted_rows.append(formatted_row)
    return formatted_rows

@app.route('/comp_login', methods=['GET'])
def compare_login():
    login_username = request.args.get('username')
    q = "SELECT * FROM [dbo].[login] WHERE Username = ?"
    query = q.replace("?", "'" + str(login_username) + "'", 1) 
    res = run_sql_query(query)

    formatted_rows = []
    for row in res:
        formatted_row = {
            'Id': row.Id,
            'Username': row.Username
        }
        formatted_rows.append(formatted_row)

    if (len(formatted_rows) == 0) :
        return 'new'
    return 'old'


#get teacher info from DB 
@app.route('/teacher', methods=['GET'])
def get_teacher():
    teacher_id = request.args.get('teacherID')
    q = "SELECT * FROM [dbo].[academic] WHERE Id = ?"
    query = q.replace("?", str(teacher_id))
    res =  run_sql_query(query)
    
    formatted_row = []
    if res:
        formatted_row = {
            'Id': res[0].Id,
            'Name': res[0].Name
        }
        
    return formatted_row


# Routes for SQL Insertion 
#get teacher info 
@app.route('/teacher1', methods=['GET'])
def get_teacher_all():
    query = "SELECT * FROM [dbo].[academic]"
    res =  run_sql_query(query)
    
    formatted_rows = []
    for row in res:
        formatted_row = {
            'Id': row.Id,
            'Name': row.Name
        }
        formatted_rows.append(formatted_row)
    return formatted_rows


@app.route('/signup', methods=['POST'])
def create_account():
    account_data = request.get_json()
    hashed_password = bcrypt.hashpw(account_data['password'].encode('utf-8'), bcrypt.gensalt())

    #call create student entry query 
    query = "INSERT INTO [dbo].[login] (Username, Password, Id) VALUES (?, ?, ?)"
    params = (account_data['username'], hashed_password, account_data['aId'])
    run_sql_query(query, params)
    print(hashed_password)
    response = {
        "message": "New Account created successfully:",
        "account_data": account_data
    }

    return jsonify(response), 201

@app.route('/new_academic', methods=['POST'])
def create_academic():
    academic_data = request.get_json()
    academic_name = academic_data['firstName'] + " " + academic_data['lastName']
    print(academic_name)
    query = "INSERT INTO [dbo].[academic] (Name, Id) VALUES (?, ?)"
    params = (academic_name, academic_data['aId'])
    run_sql_query(query, params)

    response = {
        "message": "Student Profile created successfully:",
        "student_data": academic_data
    }

    return jsonify(response), 201

# Receives student_data from the frontend and Inserts that into the DB 
@app.route('/student', methods=['POST'])
def create_student():
    student_data = request.get_json()
    #call create student folder script

    #call create student entry query 
    query = "INSERT INTO [dbo].[student] (Name, Id) VALUES (?, ?)"
    params = (student_data['name'], student_data['id'])
    run_sql_query(query, params)

    response = {
        "message": "Student Profile created successfully:",
        "student_data": student_data
    }

    return jsonify(response), 201

# Receives assignment_data from the frontend and Inserts that into the DB 
@app.route('/assignment', methods=['POST'])
def create_assignment():
    assignment_data = request.get_json()

    #call create assignment entry query 
    query = "INSERT INTO [dbo].[Assignment] (SubjectId, Name) VALUES (?, ?)"
    params = (assignment_data['id'], assignment_data['name'])
    run_sql_query(query, params)

    response = {
        "message": "Assignment Profile created successfully:",
        "assignment_data": assignment_data
    }

    return jsonify(response), 201

# Receives classroom_data from the frontend and Inserts that into the DB 
@app.route('/classroom', methods=['POST'])
def create_classroom():
    classroom_data = request.get_json()
    academicID = request.args.get('academicID')

    #call create classroom entry query 
    query = "INSERT INTO [dbo].[Subject] (Name, Id) VALUES (?, ?)"
    params = (classroom_data['name'], classroom_data['id'])
    run_sql_query(query, params)

    query1 = "INSERT INTO [dbo].[AcademicsCohort] (SubjectId, AcademicId) VALUES (?, ?)"
    params1 = (classroom_data['id'], academicID)
    run_sql_query(query1, params1)



    response = {
        "message": "Classroom Profile created successfully:",
        "classroom_data": classroom_data
    }

    return jsonify(response), 201

#Routes for Deleting Entries in SQL

#Delete Student Entry by ID
@app.route('/student/<int:id>', methods=['DELETE'])
def delete_student(id):

    query = "DELETE FROM [dbo].[student] WHERE Id = ?"
    params = (id,)
    run_sql_query(query, params)

    response = {
        "message": f"Student with ID {id} deleted successfully"
    }

    return jsonify(response), 204 

#Delete Assignment Entry by ID
@app.route('/assignment/<int:id>', methods=['DELETE'])
def delete_assignment(id):

    query = "DELETE FROM [dbo].[Assignment] WHERE Id = ?"
    params = (id,)
    run_sql_query(query, params)

    response = {
        "message": f"Assignment with ID {id} deleted successfully"
    }

    return jsonify(response), 204  

#Delete Classroom entry By ID
@app.route('/classroom/<int:id>', methods=['DELETE'])
def delete_classroom(id):

    query = "DELETE FROM [dbo].[Subject] WHERE Id = ?"
    params = (id,)
    run_sql_query(query, params)

    response = {
        "message": f"Classroom with ID {id} deleted successfully"
    }

    return jsonify(response), 204  


#Routes to connect to the File Storage 

#Uploads a file to the File Storage 
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 401

    file = request.files['file']
    if 'subject_name' not in request.form:
        return "No Subject Data", 414

    if 'studentID' not in request.form:
        return "No Student Data", 415

    if file.filename == '':
        return "No selected file", 400

    if file:
        # call script here
        file_content = file.read()

        with open('temp.txt', 'wb') as f:
            f.write(file_content)
 
        assignmentID = request.form['assignmentID']
        subject_name = request.form['subject_name']
        studentID = request.form['studentID']

        uploading_assignment('temp.txt', subject_name, studentID, assignmentID)
        
        os.remove("temp.txt")


        return file_content

    return "Something went wrong", 500


#get teacher page info based on academicID 
@app.route('/teacher-info', methods=['GET'])
def get_teacher_info():
    academic_id = request.args.get('teacherID')
    params = (academic_id)
    query = teacher_page_query.replace("?", str(params))
    res =  run_sql_query(query)
    
    formatted_rows = []
    for row in res:
        formatted_row = {
            'Subject': row.Subject,
            'SubjectID': row.ID,
            'Assignments': row.AssignmentCount,
            'Students': row.StudentCount
        }
        formatted_rows.append(formatted_row)
    return formatted_rows

#get teacher page info based on academicID 
@app.route('/subject-info', methods=['GET'])
def get_subject_info():
    academic_id = request.args.get('subjectID')
    params = (academic_id)
    query = subject_page_query.replace("?", str(params))
    res =  run_sql_query(query)
    
    formatted_rows = []
    for row in res:
        formatted_row = {
            'ID': row.Id,
            'SubjectId': row.SubjectId,
            'Name': row.Name,
            }
        formatted_rows.append(formatted_row)
    return formatted_rows

#get teacher page info based on academicID 
@app.route('/assignment-info', methods=['GET'])
def get_assignment_info():
    academic_id = request.args.get('studentID')
    params = (academic_id)
    query = submissions_for_student.replace("?", str(params))
    res =  run_sql_query(query)
    
    formatted_rows = []
    for row in res:
        formatted_row = {
            'ID': row.AssignmentId,
            'subjectName': row.Subject_Name,
            'similarityScore': row.Similarity_Score,
            'Date': row.Date
            }
        formatted_rows.append(formatted_row)
    return formatted_rows


#get student info from DB 
@app.route('/students', methods=['GET'])
def get_students_in_subject():
    subject_id = request.args.get('subjectID')
    query = students_in_subject_query.replace("?", str(subject_id))
    res =  run_sql_query(query)
    
    formatted_rows = []
    for row in res:
        formatted_row = {
            'Id': row.Id,
            'Name': row.Name
        }
        formatted_rows.append(formatted_row)
    return formatted_rows

if __name__ == "__main__":
    app.run(debug=True, port=5000)  