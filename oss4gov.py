#!/usr/bin/env python3

import argparse
import os
import os.path
import subprocess
import sys


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', default='/tmp/oss4gov')
    args = parser.parse_args(argv)

    if os.getuid() != 0:
        print('You must run this command with sudo.')
        sys.exit(1)

    # Install system dependencies
    subprocess.check_call(
        ['apt-get', 'install', '-y', 'ansible'],
        env=dict(os.environ, DEBIAN_FRONTEND='noninteractive'),
    )

    # Get playbook
    if not os.path.exists(args.path):
        os.mkdir(args.path)
        dlurl = 'https://github.com/vilnius/oss4gov/archive/master.tar.gz'
        subprocess.check_call(['wget', dlurl], cwd=args.path)
        subprocess.check_call(['tar', '-xvzpf', 'master.tar.gz'], cwd=args.path)

    # Run playbook
    ansible_command = [
        'ansible-playbook',
        '--connection=local',
        '--inventory=localhost,',
        'vmsa.yml',
    ]
    subprocess.check_call(
        ansible_command,
        cwd=os.path.join(args.path, 'oss4gov-master'),
        env=dict(os.environ, ANSIBLE_NOCOWS='1'),
    )


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
    except KeyboardInterrupt:
        sys.exit(1)
