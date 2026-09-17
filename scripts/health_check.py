"""Basic health checks for yuguang-operations."""

import os


def check_env():
    required = []
    missing = [x for x in required if not os.getenv(x)]
    return missing


if __name__ == '__main__':
    missing = check_env()
    if missing:
        print('Missing configuration:', missing)
    else:
        print('Environment looks ready')
