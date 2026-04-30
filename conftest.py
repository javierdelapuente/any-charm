# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.


def pytest_addoption(parser):
    parser.addoption("--charm-file", action="append", default=[])
