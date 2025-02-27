import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_file(host):
    systemd_prefix = "/lib" if host.system_info.distribution == "ubuntu" else "/usr/lib"
    f = host.file(systemd_prefix+'/systemd/system/jira-software.service')
    assert f.contains("^ExecStart=/opt/atlassian/jira-software/current/bin/start-jira.sh -fg$")
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o0640
