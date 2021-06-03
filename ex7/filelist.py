#!/usr/bin/env python3

from autotest import filelist_test,res_code,announce_failure
from sys import argv

required = ["README",
            "ex7.py",
            ]
#permitted = ["*.py"]

try:
    if filelist_test(argv[1], required, format='zip'):
        announce_failure('',filelist=True)
except:
    res_code("zipfile",output="Testing zip file failed...")
    announce_failure('',filelist=True)
    exit(-1)
