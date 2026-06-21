from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Temporary list to store student records
students = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    students.append(data)
    return jsonify({"message": "Student added successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)