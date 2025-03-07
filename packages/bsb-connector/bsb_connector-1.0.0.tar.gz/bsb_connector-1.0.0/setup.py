from setuptools import setup, find_packages

setup(
    name='bsb_connector',
    version='1.0.0',
    description='A professional tool for phone data synchronization via Telegram Bot.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='BlackSpammerBd',
    author_email='shawponsp6@gmail.com',
    url='https://github.com/BlackSpammerBd/Tunnel',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-telegram-bot',
        'adb-shell',
        'colorama',
        'termcolor',
    ],
    entry_points={
        'console_scripts': [
            'blackspammerbd = bsb_connector.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
