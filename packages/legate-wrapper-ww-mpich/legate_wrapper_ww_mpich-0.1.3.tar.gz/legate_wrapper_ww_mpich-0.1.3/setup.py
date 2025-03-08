import os
import subprocess
import sys
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        super().__init__(name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(build_ext):
    def run(self):
        try:
            subprocess.check_call(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.join(os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name))), 'legate_wrapper')
        cmake_args = [
            '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
            '-DPYTHON_EXECUTABLE=' + sys.executable,
            '-DCMAKE_INSTALL_PREFIX=' + extdir
        ]

        build_args = ['--config', 'Release']

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        # Run CMake to configure the project
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp)
        # Build the project
        subprocess.check_call(['cmake', '--build', '.', '--target', 'install'] + build_args, cwd=self.build_temp)

class InstallWithCMake(install):
    def run(self):
        self.run_command('build_ext')
        install.run(self)

setup(
    name='legate_wrapper_ww_mpich',
    version='0.1.3',
    author='Your Name',
    author_email='your.email@example.com',
    description='A description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/legate_wrapper',
    packages=['legate_wrapper'],
    ext_modules=[CMakeExtension('legate_wrapper', sourcedir='.')],
    cmdclass={
        'build_ext': CMakeBuild,
        'install': InstallWithCMake,
    },
    zip_safe=False,
    python_requires=">=3.8",
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
