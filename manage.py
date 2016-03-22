#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sdp_curricula.settings")
    sys.path.append('../lib/python/2.7/site-packages')
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
