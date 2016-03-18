# -*- coding: utf-8 -*-
from copy import copy
import logging


def basicConfig(**kwargs):
    options = {'level': logging.INFO,
            'format': "%(name)s %(levelname)s %(asctime)s - %(message)s"
    }
    options.update(kwargs)
    logging.basicConfig(**options)

