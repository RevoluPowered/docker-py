import os
import unittest

import paramiko.ssh_exception
import pytest

import docker

from .base import TEST_API_VERSION


class SSHConnectionTest(unittest.TestCase):
    @pytest.mark.skipif('UNKNOWN_DOCKER_SSH_HOST' not in os.environ,
                        reason='Unknown Docker SSH host not configured')
    def test_ssh_unknown_host(self):
        pass
