#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def accepts(*types):
    def check_accepts(f):
        if sys.version_info > (3, ):
            assert len(types) == f.__code__.co_argcount
        else:
            assert len(types) == f.func_code.co_argcount

        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), "arg %r does not match %s" % (a, t)
            return f(*args, **kwds)

        if sys.version_info > (3, ):
            new_f.func_name = f.__name__
        else:
            new_f.func_name = f.func_name

        return new_f

    return check_accepts
