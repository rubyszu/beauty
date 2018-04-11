# -*- coding: utf-8 -*-

import sys

print 'Number of arguments:', len(sys.argv)

print 'They are:', str(sys.argv)

print type(sys.argv)

branch = sys.argv[-1]
print branch