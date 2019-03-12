import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_installed(host):
    pkg = host.package('nginx')

    assert pkg.is_installed


def test_nginx_config_valid(host):
    cmd = host.run('nginx -t -c /etc/nginx/nginx.conf')

    assert cmd.rc == 0


def test_nginx_running(host):
    svc = host.service('nginx')

    assert svc.is_enabled and svc.is_running
