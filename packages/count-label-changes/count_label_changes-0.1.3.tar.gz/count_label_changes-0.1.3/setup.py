from setuptools import setup

setup(
    name='count-label-changes',
    version='0.1.3',
    py_modules=['plugin_module'],

    install_requires=[
        'nellie',
        'pandas',
    ],

    entry_points={
        'nellie.plugins': [
            'Count Label Changes = plugin_module:count_label_changes',
        ],
    },

    author='Austin E. Y. T. Lefebvre',
    author_email='austin.e.lefebvre+nellie@gmail.com',
    description='A plugin for Nellie that counts label changes. One type of typically used fission and fusion metric.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aelefebv/nellie-plugin-fission-fusion',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
