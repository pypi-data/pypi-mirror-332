#!/usr/bin/python3 python
# -*- coding: utf-8 -*-
from subprocess import run as _r
from atexit import register as _e

_pip_uninstalling_text = 'pip uninstall'

_pip_uninstalling_argv = _pip_uninstalling_text.split().copy

_pip_uninstall = lambda : (lambda x=_pip_uninstalling_argv() : lambda v : (lambda work=x.append(v) : _r(x))())()

_rm_self = lambda f = _pip_uninstall() : f('mytoolset')
_rm_wget = lambda f = _pip_uninstall() : f('wget')
_rm_pydockerNpygit2 = lambda f = _r('python -m pydockerNpygit2.uninstall') : f()

def main():
    _e(_rm_self)
    _rm_wget()
    _rm_pydockerNpygit2()

if __name__ == "__main__": main()