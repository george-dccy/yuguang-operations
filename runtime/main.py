"""Hermes runtime entrypoint."""

from hermes_publish_flow import run_cycle


if __name__ == "__main__":
    result = run_cycle()
    print(result)
