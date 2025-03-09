#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shlex
import logging
from typing import List, Union, Iterable

from localecmd.localisation import _
from localecmd.func import Function

module_logger = logging.getLogger("parsing")


def convert_word(word: str) -> Union[str, int, float]:
    """
    Interpret string.

    Converts the string to what type is looks like. There are several possibles:
    1. Empty string is kept as a string.
    2. a sequence of decimals without decimal comma (or point) is an integer.
    It may contain a minus "-" in the front.
    3. Something in quotes is a string. Quotes are removed.
    4. Whatever python regards as a float is a float.

    :param list[str] word: word to convert.
    :return: Converted word.
    :rtype: str | int | float

    """
    # Convert decimals to int
    if len(word) == 0:
        return word
    if word.lstrip("-").isdecimal():
        return int(word)
    # Convert quoted strings to non-quoted strings
    if word[0] == word[-1] and word[0] in ['"', "'"]:
        return word[1:-1]
    # Try to recognise floats
    # Maybe better algorithms https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python
    # But remember to localise
    try:
        f = float(word)
        return f
    except ValueError:
        return word


def object_to_token(o: Union[int, float, str]) -> str:
    """
    Converts the object into a string that can again be parsed by convert_tokens.

    This calls the Python str method for everything but strings. Here `repr(o)`
    is called to insert quotation marks.

    :param Union[int, float, str] o: The object to convert.
    :return str: The object as a string.

    """
    if isinstance(o, str):
        # Keep quotes around strings:
        return repr(o)
    return str(o)


def word_is_kwarg(word: str) -> bool:
    """
    Checks if the given word starts a keyword argument.

    A keyword argument starts with a dash '-' and the following characters are a valid Python variable name.
    However, the function checks only for the dash and that the first character afterwards is alphabetical.

    :param word: Word to check
    :type word: str
    :return: If the word starts a keyword argument
    :rtype: bool

    """
    return len(word) > 1 and word.startswith('-') and word[1].isalpha()


def line_to_args(line: str) -> tuple[str, list, dict, str]:
    """Parse the line into a command name and a string containing
    the arguments. Returns a tuple containing (`command`, `args`, `kwargs`, `line`).
    'command' and 'args' may be empty if the line couldn't be parsed.

    """
    line = line.strip()

    # Split up at space, but keep quoted strings as such and also keep the quotes.
    tokens = shlex.split(line, posix=False)

    if len(tokens) == 0:
        # Nothing in the line
        cmd = ""
        words: List = []
    elif len(tokens) == 1:
        # Only command
        cmd, words = tokens[0], []
    else:
        # Should tokens be empty list anyway, this line will fail with
        # "IndexError: list index out of range".
        cmd, words = tokens[0], tokens[1:]

    # Sort out keyword arguments
    # Indices of keyword arguments
    kwi = [i for i, e in enumerate(words) if word_is_kwarg(e)]
    kwargs = {words[i][1:]: convert_word(words[i + 1]) for i in kwi}

    if len(kwargs) > 0:
        args = [convert_word(word) for word in words[0 : kwi[0]]]
    else:
        args = [convert_word(word) for word in words]

    return cmd, args, kwargs, line


def args_to_line(cmd: str, *args, **kwargs) -> str:
    """
    Convert the calling of a command to a string that produces this command.

    The arguments are converted directly. Keyword arguments get a minus "-" in
    front of the key and the argument comes afterward.
    Note that the interpreter does not convert keyword arguments yet.

    :param str cmd: Command name.
    :param list:args: Arguments to the command.
    :param dict kwargs: Keyword arguments to the command.
    :return str: The line to insert into command line prompt.

    :::{rubric} Example
    :::
    >>> args_to_line("bla", 80, "bla", hello="world")
    "bla 80 'bla' -hello 'world'"

    """
    tokens = [str(cmd)]
    for arg in args:
        tokens.append(object_to_token(arg))

    for key, value in kwargs.items():
        tokens.append("-" + str(key))
        tokens.append(object_to_token(value))

    return " ".join(tokens)


def extend_word(cmd: str, cmdlist: Iterable[str], distributors: set[str]) -> str:
    """
    Extent word

    The function will try to extend the word `cmd` to a command in `cmdlist`
    or a word in the `distributors` set.

    The following will be the output:
    1. Given string is a valid command -> return it
    2. It can be completed to one word in the `distributors` set -> extend to that.
    3. It can be completed to one valid command -> extend to that.
    4. It can't be extended to any command, return empty string.
    Command doesn't exist.
    5. It can be extended to more than one command,
    but zero or at least two distributors -> return empty string.
    Command is ambigous.

    :param str cmd: Command to complete
    :param Iterable[str] cmdlist: List of known commands
    :param set[str] distributors: List of names to extend to.
    :return: Completed command, or empty string if not able to complete
    :rtype: str

    """
    # Remember to updating docstring of CLI when doing changes here
    if cmd not in cmdlist:
        func_completes = [n for n in cmdlist if n.startswith(cmd)]
        dist_completes = [n for n in distributors if n.startswith(cmd)]

        if len(dist_completes) == 1:
            cmd = dist_completes[0]
        elif len(func_completes) == 1:
            cmd = func_completes[0]
        elif not func_completes:
            print(_("Command {0} does not exist!").format(cmd))
            return ""
        else:
            msg = _("Command {0} is ambigous! it could be {1}")
            print(msg.format(cmd, str(func_completes)))
            return ""
    return cmd


def parse_line(
    line: str,
    function_dict: dict[str, Function],
    distributors: set[str],
    aliases: dict[str, str] = {},
) -> Union[tuple[Function, Iterable, dict], None]:
    """
    Interpret line as if it came from prompt.

    What function does is
    1. Parse line to get command name, positional args and keyword args.
    See {py:func}`parsing.line_to_args`
    2. Complete command
    3. If command is now in distributor set, use first argument to extend it.
    4. Apply aliases


    :param line: Line as typed in
    :type line: str
    :param function_dict: Dictionary of name – executable pairs.
    :type function_dict: dict[str, Function]
    :param distributors: Set of short names of functions to use for command completion
    and for being able to concatenate commands such that user can use space instead of underscore.
    :type distributors: set[str]
    :param aliases: Command aliases to apply *after* command completion,
    defaults to {}
    :type aliases: dict[str, str], optional
    :return: Function, positional args and dict of keyword args. None if command could not be parsed
    :rtype: tuple[Function, Iterable, dict]

    """

    module_logger.debug("Got line " + line)

    cmd, args, kwargs, line = line_to_args(line)

    if not cmd:
        print()
        return None

    funcs = list(function_dict.keys()) + list(aliases.keys())

    # Autocomplete_command
    # Remember to updating docstring of CLI when doing changes here
    cmd = extend_word(cmd, funcs, distributors)
    module_logger.debug("Extended first word to command " + cmd)
    # Handle distributor functions, like edit, print, etc.
    if cmd in distributors and cmd not in funcs:
        if len(args) > 0 and isinstance(args[0], str):
            cmd += "_" + args[0]
            # Autocomplete again. Now for the whole command
            cmd = extend_word(cmd, funcs, distributors)
            args = args[1:]
        else:
            # Called f.e. edit and did not say what to edit.
            # or specified what to edit as an integer
            # This should be handled somehow
            print(_("Command incomplete: {0}").format(cmd))
            return None
            # Now just edit is called, which is no function
    if not cmd:  # If problems with the command, cmd is now empty
        return None

    # Handle aliases
    if cmd in aliases.keys():
        cmd = aliases[cmd]

    func = function_dict[cmd]
    return func, args, kwargs
