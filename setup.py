from DistUtilsExtra.auto import setup
from distutils.command.install import install
import os

PACKAGE="vacmonitor"
VERSION="1.0"

# In case we need hooks
class post_install(install):
    def run(self):
        install.run(self)

setup(
    name              = PACKAGE,
    author            = "Gary Oliver",
    author_email      = "go@robosity.com",
    url               = "http://robosity.com",
    version           = VERSION,
    packages          = [ "vacmonitor" ],
    scripts           = [ "vacmonitor/vacmonitor" ],
    # package_data      = { "vacmonitor": [ "bitmaps/vacmonitor-logo.png" ] },
    license           = "Copyright 2020, Robosity Codeworks.",
    description       = "Vacuum monitor and control",
    long_description  = open("README.md").read(),
    data_files        = [
        ("share/vacmonitor",     [ "LICENSE", ]),
    ],
    cmdclass = { 'install': post_install },
)
