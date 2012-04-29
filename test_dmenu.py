import dmenu

def test_build_commandline():
    cli = dmenu.build_commandline()
    assert cli == ["dmenu"]

def test_build_commandline_bottom():
    cli = dmenu.build_commandline(bottom=True)
    assert cli == ["dmenu","-b"]

def test_build_commandline_advanced():
    cli = dmenu.build_commandline(bottom=True,lines=10,prompt="select")
    assert cli == ["dmenu","-b","-l", "10", "-p", "select"]
