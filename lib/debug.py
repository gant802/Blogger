#!/usr/bin/env python3
# lib/debug.py
import ipdb

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.post import Post

Post.drop_table()
Post.create_table()
p1 = Post("Big whale", "a", "sports", "Whales", "Grant")

ipdb.set_trace()
