#!/usr/bin/env python
import os
import sys

MANAGE_ROOT = os.path.dirname(os.path.realpath(__file__))
THIRD_PARTY_ROOT = os.path.join(MANAGE_ROOT, 'third_party')

sys.path.extend([THIRD_PARTY_ROOT,])

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
