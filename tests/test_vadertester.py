import subprocess
import sys
from vadertester.__main__ import main
def test_vadertester(capsys):
    sys.argv = ['314Project\\vadertester\\__main__.py', '-i', '20', '-f', 'Amazon_githubdata.json.gz']
    main()
    captured = capsys.readouterr()
    assert "Vader tester started" in captured.out
    assert "Vader tester finished" in captured.out
    sys.argv = ['314Project\\vadertester\\__main__.py', '-i', '30']
    main()
    captured = capsys.readouterr()
    assert "Vader tester started" in captured.out
    assert "Vader tester finished" in captured.out
    sys.argv = ['314Project\\vadertester\\__main__.py']
    main()
    captured = capsys.readouterr()
    assert "Vader tester started" in captured.out
    assert "Vader tester finished" in captured.out

    output1 = str(subprocess.check_output("python -m vadertester", stderr = subprocess.STDOUT, shell = True))
    assert "Vader tester started" in output1
    assert "Vader tester finished" in output1
    output2 = str(subprocess.check_output("python -m vadertester -i 25", stderr = subprocess.STDOUT, shell = True))
    assert "Vader tester started" in output2
    assert "Vader tester finished" in output2
    output3 = str(subprocess.check_output("python -m vadertester -i 20 -f Amazon_githubdata.json.gz", stderr=subprocess.STDOUT, shell=True))
    assert "Vader tester started" in output3
    assert "Vader tester finished" in output3