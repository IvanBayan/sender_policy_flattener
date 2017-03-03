# coding=utf-8
from distutils.core import setup

setup(
    name='sender_policy_flattener',
    version='1',
    packages=['sender_policy_flattener'],
    url='https://github.com/cetanu/sender_policy_flattener',
    license='MIT',
    author='vsyrakis',
    author_email='cetanu@gmail.com',
    description='Flatten SPF records to IPs to avoid DNS record constraints',
    entry_points={
        'console_scripts': [
            'sender_policy_flattener=sender_policy_flattener'
        ]
    },
)