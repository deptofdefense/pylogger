# -*- coding: utf-8 -*-

# =================================================================
#
# Work of the U.S. Department of Defense, Defense Digital Service.
# Released as open source under the MIT License.  See LICENSE file.
#
# =================================================================

from distutils.core import setup
import json

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
    try:
        from pip._internal.download import PipSession
        pip_session = PipSession()
    except ImportError:  # for pip >= 20
        from pip._internal.network.session import PipSession
        pip_session = PipSession()
except ImportError:  # for pip <= 9.0.3
    try:
        from pip.req import parse_requirements
        from pip.download import PipSession
        pip_session = PipSession()
    except ImportError:  # backup in case of further pip changes
        pip_session = 'hack'

install_requires = None
try:
    # attempt to parse the requirements.txt file
    requirements = list(parse_requirements('requirements.txt', session=pip_session))
    try:
        install_requires = [str(ir.req) for ir in requirements]
    except Exception:
        install_requires = [str(ir.requirement) for ir in requirements]
except Exception:
    # attempt to parse the Pipfile.lock used by pipenv
    with open('Pipfile.lock') as fd:
        data = json.load(fd)
        install_requires = [
            ("git+{}@{}#egg={}".format(v['git'], v.get('ref'), k) if v.get("git") is not None else k + v['version'])
            for k, v in data['default'].items()
        ]

install_requires = [
    ("{} @ {}".format(ir[ir.index("#egg=")+5:], ir) if ir.startswith("git+") else ir)
    for ir in install_requires
]

setup(name='pylogger',
      version="0.0.1",
      description="A simple library for logging in Python.",
      long_description=open('README.md').read(),
      classifiers=[
        "Development Status :: 5 - Production/Stable"
      ],
      download_url="https://github.com/deptofdefense/pylogger/zipball/main",
      python_requires='>=3.9',
      keywords='python data',
      author='DDS Developers',
      author_email='code@dds.mil',
      url='https://github.com/deptofdefense/pylogger',
      packages=[
        'pylogger',
      ],
      package_data={
          '': ['requirements.txt'], # noqa
          '': ['*.*'], # noqa
          '': ['static/*.*'], # noqa
          'static': ['*.*'],
      },
      include_package_data=True,
      install_requires=install_requires,
      zip_safe=False
)
