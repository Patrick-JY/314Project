import subprocess

def test_vadertester():
    output1 = str(subprocess.check_output("python -m vadertester", stderr = subprocess.STDOUT, shell = True))
    assert "Vader tester started" in output1
    assert "Vader tester finished" in output1
    output2 = str(subprocess.check_output("python -m vadertester -i 25", stderr = subprocess.STDOUT, shell = True))
    assert "Vader tester started" in output2
    assert "Vader tester finished" in output2
    output3 = str(subprocess.check_output("python -m vadertester -i 20 -f Amazon_githubdata.json.gz", stderr=subprocess.STDOUT, shell=True))
    assert "Vader tester started" in output3
    assert "Vader tester finished" in output3