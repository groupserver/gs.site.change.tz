# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.site.change.tz',
    version=version,
    description="Change the timezone on a GroupServer site",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: Other/Proprietary License",
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='site groupserver time timezone date',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://groupserver.org/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.site', 'gs.site.change', ],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'setuptools',
        'zope.formlib',
        'zope.interface',
        'zope.schema',
        'zope.viewlet',
        'Zope2',
        'gs.content.form',
        'gs.help',
        'gs.site.change.base',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
