import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package_installed(host):
    pkg = host.package("nginx")

    assert pkg.is_installed


def test_config_valid(host):
    cmd = host.run("nginx -t")

    assert cmd.rc == 0


def test_service_running(host):
    svc = host.service("nginx.service")

    assert svc.is_enabled
    assert svc.is_running
