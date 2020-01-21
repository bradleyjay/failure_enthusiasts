#!/usr/bin/env python
from backend import make_connection, parse_current

data = make_connection()
parse_current(data)
