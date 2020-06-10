import os
import sys
from vadertester.__main__ import main
from pkg_resources import resource_filename

def test_vadertester1(tmpdir, capsys):
    os.chdir(tmpdir)
    sys.argv = ['__main__.py', '-i', '20', '-f', resource_filename("vadertester", "json/Amazon_githubdata.json.gz")]
    main()
    captured = capsys.readouterr()
    assert "Vader tester started" in captured.out
    assert "Vader tester finished" in captured.out
    assert os.path.exists(os.path.join(tmpdir, "output.txt"))

def test_vadertester2(tmpdir, capsys):
    os.chdir(tmpdir)
    sys.argv = ['__main__.py', '-i', '30']
    main()
    captured = capsys.readouterr()
    assert "Vader tester started" in captured.out
    assert "Vader tester finished" in captured.out
    assert os.path.exists(os.path.join(tmpdir, "output.txt"))

def test_vadertester3(tmpdir, capsys):
    os.chdir(tmpdir)
    sys.argv = ['__main__.py']
    main()
    captured = capsys.readouterr()
    assert "Vader tester started" in captured.out
    assert "Vader tester finished" in captured.out
    assert os.path.exists(os.path.join(tmpdir, "output.txt"))
