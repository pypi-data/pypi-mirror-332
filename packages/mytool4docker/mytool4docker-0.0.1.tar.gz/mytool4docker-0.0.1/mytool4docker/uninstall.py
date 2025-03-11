#!/usr/bin/python3 python
# -*- coding: utf-8 -*-
from subprocess import run as _r
from atexit import register as _e

_pip_uninstalling_text = 'pip uninstall'

_pip_uninstalling_argv = _pip_uninstalling_text.split().copy

_pip_uninstall = lambda : (lambda x=_pip_uninstalling_argv() : lambda v : (lambda work=x.append(v) : _r(x))())()

_rm_self = lambda f = _pip_uninstall() : f('mytool4docker')
_rm_akatool = lambda f = _pip_uninstall() : f('akatool')
_rm_mytoolset = lambda f = _r('python -m mytoolset.uninstall') : f()

def main():
    _e(_rm_self)
    _rm_akatool()
    _rm_mytoolset()

if __name__ == "__main__": main()