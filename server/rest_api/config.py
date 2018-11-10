#! /usr/bin/env python2.7

import os

APPLICATION_ROOT = "/"

SECRET_KEY = b'\xa4\x1d&\x1e\xc7\xf4:cY\xcd\x19D\x1e\x97\x95\x00eRm\x02\x7f\x1b\xce?\x9c\x9b\xfev\xc5\x18\x88.'

DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'data',
    'data.db'
)
