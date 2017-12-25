#!/usr/bin/python3

from sys        import version_info
from platform   import linux_distribution
from subprocess import check_output

class MissingPackageError(Exception):
    def __init__(self, packages):
        self.packages = packages

def installed_packages():
    if not (version_info.major >= 3 and 
            linux_distribution()[0].lower() in ['debian', 'ubuntu']):
        raise RuntimeError('ONLY PYTHON3 ON DEBIAN/UBUNTU IS SUPPORTED !!')

    output = check_output(['dpkg-query', '--show', '-f', '${Package}\n'])
    return output.decode('utf-8').strip().split('\n')

def verify_packages(*package_list):
    missing = [pkg for pkg in package_list if pkg not in installed_packages()]
    if missing:
        raise MissingPackageError(missing)