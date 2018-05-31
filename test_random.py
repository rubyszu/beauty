# -*- coding: utf-8 -*-
import random

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
sa = []
for i in range(8):
    sa.append(random.choice(seed))
salt = ''.join(sa)
print salt