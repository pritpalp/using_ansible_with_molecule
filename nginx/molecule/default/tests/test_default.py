import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_nginx(host):
    # is the nginx package installed
    assert host.package('nginx').is_installed
    # is it running
    assert host.service('nginx').is_running


def test_nginx_index(host):
    f = host.file('/usr/share/nginx/html/index.html')
    # Does the index.html file exist in the correct folder
    assert f.exists


def test_index_content(host):
    f = host.file('/usr/share/nginx/html/index.html')
    # Is it the file we put there?
    assert f.contains('Hello World!')
