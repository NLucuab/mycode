#!/usr/bin/env python3
"""Parsing log files"""
loginfail = 0 # fail counter

keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")

keystone_file_lines = keystone_file.readlines()

for line in keystone_file_lines:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1

print("The # of failed login attempts is", loginfail)

keystone_file.close()
