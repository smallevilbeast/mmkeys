#!/usr/bin/env python

"""Setup script for the CDDB module distribution."""

__revision__ = "$Id: setup.py,v 1.4 2001/03/10 22:34:03 che_fox Exp $"

import os
from distutils.core import setup, Extension

def capture(cmd):
    return os.popen(cmd).read().strip()

setup (# Distribution meta-data
       name = "mmkeys",
       version = "1.6.3",
       description = "Multimedia Key support as a PyGTK object",
       author = "Lee Willis",
       author_email = "lee@leewillis.co.uk",
       url = "http://csl.cse.ucsc.edu/~ben/python/",

       # Description of the modules and packages in the distribution
       py_modules = ['mmkeys'],
       ext_modules=[Extension(
            "mmkeys", ["mmkeyspy.c", "mmkeys.c", "mmkeysmodule.c"], 
            extra_compile_args=capture("pkg-config --cflags gtk+-2.0 pygtk-2.0").split(),
            extra_link_args=capture("pkg-config --libs gtk+-2.0 pygtk-2.0").split()),]
       )
       
       
