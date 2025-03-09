#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from localecmd import parsing
from localecmd.parsing import parse_line, extend_word


def test_parsing():
    assert parsing.convert_word("") == ""
    assert parsing.convert_word("8") == 8
    assert parsing.convert_word("-8") == -8
    assert parsing.convert_word("-8.5") == -8.5
    assert parsing.convert_word("+8") == 8.0
    assert parsing.convert_word("asd") == "asd"
    assert parsing.convert_word("'-8'") == "-8"
    assert parsing.convert_word("' h iosgh'") == " h iosgh"


def test_tokenising():
    assert parsing.object_to_token(8) == "8"
    assert parsing.object_to_token(8.9) == "8.9"
    assert parsing.object_to_token(-8.9) == "-8.9"
    assert parsing.object_to_token(-1) == "-1"
    assert parsing.object_to_token("b") == "'b'"
    assert parsing.object_to_token("a b c") == "'a b c'"


def test_word_kwarg():
    assert parsing.word_is_kwarg('-kwarg')
    assert parsing.word_is_kwarg('-k4')
    assert parsing.word_is_kwarg('-引数')  # Parameter? in Japanese
    assert parsing.word_is_kwarg('-پارامتر')  # Parameter? in Persian
    assert not parsing.word_is_kwarg('-5')
    assert not parsing.word_is_kwarg('-3.1415926')
    assert not parsing.word_is_kwarg('-3,1415926')
    assert not parsing.word_is_kwarg('-4g')


def test_parsing_args():
    assert parsing.line_to_args("") == ("", [], {}, "")
    assert parsing.line_to_args("bla") == ("bla", [], {}, "bla")
    line = "hello, world"
    assert parsing.line_to_args(line) == ("hello,", ["world"], {}, line)

    line = "edit stop 62850 Meyenburg -arr 08:15"
    args = ["stop", 62850, "Meyenburg"]
    kwargs = {"arr": "08:15"}
    assert parsing.line_to_args(line) == ("edit", args, kwargs, line)

    line = "edit stop 62850 'Frankfurt am Main Hbf' -arr 08:15 -dep 08:16"
    args = ["stop", 62850, "Frankfurt am Main Hbf"]
    kwargs = {"arr": "08:15", "dep": "08:16"}
    assert parsing.line_to_args(line) == ("edit", args, kwargs, line)

    # Test negative numbers
    line = "bla -8 -a -9"
    assert parsing.line_to_args(line) == ("bla", [-8], {'a': -9}, line)


def test_line_generation():
    assert (
        parsing.args_to_line("cmd", *["arg"], **{"key": "value"})
        == "cmd 'arg' -key 'value'"
    )


def test_back_and_forth():
    line = "edit_stop 62850 'Meyenburg' '08:14' '08:15' '|'"
    cmd, args, kwargs, line = parsing.line_to_args(line)
    assert parsing.args_to_line(cmd, *args, **kwargs) == line

    line = "edit_stop 62850 'Meyenburg' -arr '08:14' -dep '08:15' -stop '|'"
    cmd, args, kwargs, line = parsing.line_to_args(line)
    assert parsing.args_to_line(cmd, *args, **kwargs) == line


def test_complete_command(capsys):
    flist = "help quit list_all list_args list_cmds love_your_next".split()
    dist = set("list love".split())

    assert extend_word("help", flist, dist) == "help"
    assert extend_word("q", flist, dist) == "quit"
    assert extend_word("list_ar", flist, dist) == "list_args"
    assert extend_word("lo", flist, dist) == "love"
    assert extend_word("lo", flist, set(["list"])) == "love_your_next"

    assert extend_word("list", flist, dist) == "list"
    assert extend_word("list_a", flist, dist) == ""
    assert "ambigous" in capsys.readouterr().out.strip()

    assert extend_word("k", flist, dist) == ""
    assert "does not exist" in capsys.readouterr().out.strip()


def test_parse_line(capsys):
    help_str = "help"
    quit_str = "Print that program is exited"

    functions = {
        "help": lambda *x: print(help_str, *x),
        "help_program": lambda: print('help_program'),
        "quit": lambda: print(quit_str),
        "list_cmds": print,
        "list_args": print,
        "list_all": print,
    }

    ret = parse_line("help", functions, set())
    assert ret[0] == functions["help"]
    assert not ret[1]
    assert not ret[2]

    ret = parse_line("quit", functions, set())
    assert ret[0] == functions["quit"]
    assert not ret[1]
    assert not ret[2]

    # Test completion
    ret = parse_line("q", functions, set())
    assert ret[0] == functions["quit"]
    assert not ret[1]
    assert not ret[2]

    ret = parse_line("help_", functions, set())
    assert ret[0] == functions["help_program"]
    assert not ret[1]
    assert not ret[2]

    # Test that name conflict between function and distributor goes in favour of function
    ret = parse_line("h", functions, set(["help"]))
    assert ret[0] == functions["help"]
    assert not ret[1]
    assert not ret[2]

    ret = parse_line("h p", functions, set(["help"]))
    assert ret[0] == functions["help"]
    assert ret[1] == ["p"]
    assert not ret[2]

    # Test incomplete command
    # Shouldnt this raise an exception?
    parse_line("list", functions, set(["list"]))
    assert "incomplete" in capsys.readouterr().out.strip()

    # Test ambiguous commands
    # Shouldnt these raise an exception too?
    parse_line("list", functions, set())
    assert "ambigous" in capsys.readouterr().out.strip()

    parse_line("list a", functions, set(["list"]))
    assert "ambigous" in capsys.readouterr().out.strip()

    ret = parse_line("list all functions", functions, set(["list"]))
    assert ret[0] == functions["list_all"]
    assert ret[1] == ["functions"]
    assert not ret[2]

    # Test alias
    ret = parse_line(
        "list all functions", functions, set(["list"]), {"list_all": "help"}
    )
    assert ret[0] == functions["help"]
    assert ret[1] == ["functions"]
    assert not ret[2]

    # Test empty line
    ret = parse_line("", functions, set())
    assert ret is None
