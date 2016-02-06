"""

Running tests
=============

First install dependencies::

    $ pip install mock pytest pytest-mock

Then run::

    $ py.test -vv tests.py

"""

import mock
import os.path
import tempfile

import oss4gov


def test_main(mocker):
    mocker.patch('os.environ', {})
    mocker.patch('os.getuid', return_value=0)
    check_call = mocker.patch('subprocess.check_call')

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'oss4gov')

        # First time run
        oss4gov.main(['-p', path])

        # Second time run
        oss4gov.main(['-p', path])

    call = mock.call

    assert check_call.mock_calls == [
        # First time run
        call(['apt-get', 'install', '-y', 'ansible'], env={'DEBIAN_FRONTEND': 'noninteractive'}),
        call(['wget', 'https://github.com/vilnius/oss4gov/archive/master.tar.gz'], cwd=path),
        call(['tar', '-xvzpf', 'master.tar.gz'], cwd=path),
        call(
            ['ansible-playbook', '--connection=local', '--inventory=localhost,', 'vmsa.yml'],
            cwd=os.path.join(path, 'oss4gov-master'), env={'ANSIBLE_NOCOWS': '1'},
        ),

        # Second time run
        call(['apt-get', 'install', '-y', 'ansible'], env={'DEBIAN_FRONTEND': 'noninteractive'}),
        call(
            ['ansible-playbook', '--connection=local', '--inventory=localhost,', 'vmsa.yml'],
            cwd=os.path.join(path, 'oss4gov-master'), env={'ANSIBLE_NOCOWS': '1'},
        ),
    ]
