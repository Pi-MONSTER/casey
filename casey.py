#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# swap case of commandline string
# v0.3

import sys

if len(sys.argv) > 1:
	lower_c_text = sys.argv[1]
else:
	lower_c_text = input("text to convert to UPPER CASE : ")
print(lower_c_text.swapcase())
