#!/usr/bin/env python3
# lib/debug.py
import ipdb

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.post import Post


p1 = Post("1", "Hello")

ipdb.set_trace()
