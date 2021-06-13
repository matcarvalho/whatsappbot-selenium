# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 13:12:48 2021

@author: mateuscarvalho
"""

from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='whatsappbot-selenium',
    version='0.0.1',
    url='https://github.com/matcarvalho/whatsappbot-selenium',
    license='MIT License',
    author='Mateus Carvalho',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='mateuscarvalho@outlook.com',
    keywords='Bot for Whatsapp with Selenium',
    description=u'It is a module that has the function of sending and deleting whatsapp messages using Selenium',
    packages=['whatsappbot-selenium'],
    install_requires=['webdriver-manager', 'selenium'],
)
