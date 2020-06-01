import subprocess

def test_vadertester():
    output = str(subprocess.check_output("python -m vadertester -i 25", stderr = subprocess.STDOUT, shell = True))
    assert "Vader tester started" in output
    assert "Vader tester finished" in output