from app.commands.operations import Addition, Subtraction, Multiplication, Division, Power, Modulus  # Adjust the import path

def test_addition_command(capfd):
    command = Addition(a=5, b=3)
    command.execute()
    out, _ = capfd.readouterr()
    assert out.strip() == "The sum of 5 and 3 is 8", "Addition command failed"

def test_subtraction_command(capfd):
    command = Subtraction(a=5, b=3)
    command.execute()
    out, _ = capfd.readouterr()
    assert out.strip() == "The difference between 5 and 3 is 2", "Subtraction command failed"

def test_multiplication_command(capfd):
    command = Multiplication(a=5, b=3)
    command.execute()
    out, _ = capfd.readouterr()
    assert out.strip() == "The product of 5 and 3 is 15", "Multiplication command failed"

def test_division_command(capfd):
    command = Division(a=6, b=3)
    command.execute()
    out, _ = capfd.readouterr()
    assert out.strip() == "The quotient of 6 divided by 3 is 2.0", "Division command failed"

def test_division_by_zero_command(capfd):
    command = Division(a=6, b=0)
    command.execute()
    out, _ = capfd.readouterr()
    assert "Error: Division by zero is not allowed" in out, "Division by zero error handling failed"

def test_power_command(capfd):
    command = Power(a=2, b=3)
    command.execute()
    out, _ = capfd.readouterr()
    assert out.strip() == "2 raised to the power of 3 is 8", "Power command failed"

def test_modulus_command(capfd):
    command = Modulus(a=5, b=3)
    command.execute()
    out, _ = capfd.readouterr()
    assert out.strip() == "The remainder of 5 divided by 3 is 2", "Modulus command failed"
