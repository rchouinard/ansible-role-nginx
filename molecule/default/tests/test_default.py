import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package_installed(host):
    pkg = host.package("nginx")

    assert pkg.is_installed


def test_service_running(host):
    srvc = host.service("nginx.service")

    assert srvc.is_enabled
    assert srvc.is_running
