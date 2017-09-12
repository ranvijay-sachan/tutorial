#!/usr/bin/env python

import paramiko


def get_remote_user_info(host, user, password):
    shell = {}
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password)
    sftp_client = ssh.open_sftp()
    remote_file = sftp_client.open('/etc/passwd')

    try:
        for line in remote_file:
            if len(line.rstrip("\n").split(":")) >= 6 and \
                            line.rstrip("\n").split(":")[6] in ["/bin/sh", "/bin/bash"]:
                fields = line.rstrip().split(":")
                shell[fields[0]] = fields[-1]
    finally:
        remote_file.close()
    print shell
    return shell
    # for user in shell.keys():
    #     print user


if __name__ == '__main__':
    get_remote_user_info('20.20.4.197', 'zymr', 'zymr')
