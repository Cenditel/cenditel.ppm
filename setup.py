# -*- coding: utf-8 -*-
"""
This module contains the tool of cenditel.ppm
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

long_description = (
    read('README.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('cenditel', 'ppm', 'README.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Download\n'
    '********\n')

tests_require = ['zope.testing']

setup(name='cenditel.ppm',
      version=version,
      description="A framework for managing projects within a project porfolio using wikis, blogs, and issue tracker.",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Plone',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='cenditel project portfolio management framework plone plonegov',
      author='Oswaldo Lopez',
      author_email='oswaldolo@hotmail.com',
      maintainer='Leonardo J. Caballero G.',
      maintainer_email='leonardocaballero@gmail.com',
      url='http://svn.plone.org/svn/collective/cenditel.ppm',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cenditel', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        "Products.AddRemoveWidget==1.3",
                        "Products.DataGridField==1.6.2",
                        "Products.Quills==1.7.0",
                        "Products.Ploneboard==2.0",
                        #"Products.Poi==1.2.9",
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='cenditel.ppm.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
