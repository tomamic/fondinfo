#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

@link    https://www.brython.info/static_doc/en/intro.html
@link    https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
'''

import os, sys, urllib.request, webbrowser, http.server, socketserver, zipfile

swig_ver = 'swigwin-3.0.12'
swig_zip = swig_ver + '.zip'
if not os.path.isfile(swig_zip):
    url = 'https://kent.dl.sourceforge.net/project/swig/swigwin/' + swig_ver + '/' + swig_zip
    with urllib.request.urlopen(url) as response:
        content = response.read()
        with open(swig_zip, 'wb') as local_file:
            local_file.write(content)

    with zipfile.ZipFile(swig_zip, 'r') as zip_ref:
        zip_ref.extractall('.')
