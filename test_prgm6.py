from employee import employee_details

def test_employee_details():
    result = employee_details("Rahul", "101", "IT", "30000")
    expected = "Name: Rahul\nEmployee ID: 101\nDepartment: IT\nSalary: 30000"
    assert result == expected