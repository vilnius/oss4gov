#!/usr/bin/env python3

import argparse
import getpass
import json
import os
import os.path
import subprocess
import sys


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', default='')
    parser.add_argument('--admin', help="Active Directory admin user name")
    args = parser.parse_args(argv)

    if os.getuid() != 0:
        print('You must run this command with sudo.')
        sys.exit(1)

    # Install system dependencies
    subprocess.check_call(
        ['apt-get', 'install', '-y', 'ansible'],
        env=dict(os.environ, DEBIAN_FRONTEND='noninteractive'),
    )

    path = args.path or '/tmp/oss4gov'

    # Get playbook
    if not os.path.exists(path):
        os.mkdir(path)
        dlurl = 'https://github.com/vilnius/oss4gov/archive/master.tar.gz'
        subprocess.check_call(['wget', dlurl], cwd=path)
        subprocess.check_call(['tar', '-xvzpf', 'master.tar.gz'], cwd=path)
        path = os.path.join(path, 'oss4gov-master')

    # Run playbook
    env = dict(os.environ, ANSIBLE_NOCOWS='1')
    extra = None

    if args.admin:
        extra = json.dumps({'domadm': args.admin}, sort_keys=True)
        env['DOMADM_PASSWORD'] = getpass.getpass('%s password:' % args.admin)

    ansible_command = list(filter(None, [
        'ansible-playbook',
        '--connection=local',
        '--inventory=localhost,',
        (('--extra-vars=%s' % extra) if extra else None),
        'vmsa.yml',
    ]))

    subprocess.check_call(ansible_command, cwd=path, env=env)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
    except KeyboardInterrupt:
        sys.exit(1)
