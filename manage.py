#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

from django.conf import settings
from dotenv import load_dotenv


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

    base_dir = Path(__file__).resolve().parent

    if settings.DEBUG:
        dotenv_path = base_dir / '.env.development'
    else:
        dotenv_path = base_dir / '.env'
    load_dotenv(dotenv_path=dotenv_path)

    try:
        from django.core.management import execute_from_command_line  # noqa PLC0415
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
