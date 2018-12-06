#!/usr/bin/env python
import os
import sys
from stp.envirement import module_settings

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", module_settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
