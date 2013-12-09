from os.path import abspath, dirname, join

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


class ToxTestCommand(TestCommand):
    """Test command which runs tox under the hood."""

    def finalize_options(self):
        """Add options to the test runner (tox)."""
        TestCommand.finalize_options(self)
        self.test_args = ['--recreate']
        self.test_suite = True

    def run_tests(self):
        """Invoke the test runner (tox)."""
        #import here, cause outside the eggs aren't loaded
        import detox.main
        errno = detox.main.main(self.test_args)
        sys.exit(errno)


# Fill in the long description (for the benefit of PyPi)
# with the contents of README.rst (rendered by GitHub).
readme_file = join(dirname(abspath(__file__)), 'README.rst')

with open(readme_file, 'r') as f:
    readme_text = f.read()

setup(
    name='wrap2',
    version='0.3',
    description='Wrapper for social network wrappers',
    long_description=readme_text,
    author='Paylogic International',
    author_email='developers@paylogic.com',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests']),
    install_requires=[
        'facebook-sdk',
        'tweepy',
        'anyjson',
        'pytz'
    ],

    dependency_links=[],
    tests_require=['detox'],
    cmdclass={'test': ToxTestCommand},
    include_package_data=True,
)
