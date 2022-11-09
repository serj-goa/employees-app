from app import app, db
from models import Employees

from flask import render_template, request, redirect


@app.route('/')
def index():
    employees = Employees.query.all()

    return render_template('index.html', title='Employees manager', employees=employees)


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == "POST":
        data = request.form.to_dict()
        employee = Employees(name=data['name'], email=data['email'], phone=data['phone'])

        db.session.add(employee)
        db.session.commit()

        return redirect('/')


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        data = request.form.to_dict()
        employee = Employees.query.get(data['id'])

        employee.name = data['name']
        employee.email = data['email']
        employee.phone = data['phone']

        db.session.add(employee)
        db.session.commit()

        return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    employee = Employees.query.get(id)

    db.session.delete(employee)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
