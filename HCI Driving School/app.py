from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
students = [
    {'name': 'John Doe', 'lesson_type': 'Introductory', 'instructor': 'Jane Instructor'},
    {'name': 'Alice Smith', 'lesson_type': 'Standard', 'instructor': 'Bob Instructor'},
    # Add more sample data as needed
]

instructors = [
    {'id': 1, 'name': 'Jane Instructor', 'contact': '123-456-7890'},
    {'id': 2, 'name': 'Bob Instructor', 'contact': '987-654-3210'},
    {'id': 3, 'name': 'Eva Thompson', 'contact': '555-123-4567'},
    # Add more sample data as needed
]

@app.route('/')
def index():
    return render_template('index.html', students=students, instructors=instructors)

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Handle form submission (booking functionality)
        student_name = request.form.get('student_name')
        lesson_type = request.form.get('lesson_type')
        instructor_id = int(request.form.get('instructor_id'))

        # Sample: Add the new booking to the students list
        new_student = {'name': student_name, 'lesson_type': lesson_type, 'instructor': get_instructor_name(instructor_id)}
        students.append(new_student)

        return redirect(url_for('index'))

    return render_template('booking.html', instructors=instructors)

def get_instructor_name(instructor_id):
    for instructor in instructors:
        if instructor['id'] == instructor_id:
            return instructor['name']
    return 'Unknown Instructor'

if __name__ == '__main__':
    app.run(debug=True)
