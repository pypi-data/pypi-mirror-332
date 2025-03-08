# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 06:32:02 2025

@author: Dr. REBEL-ious
"""
from setuptools import setup, find_packages
setup(name = 'influential_points', #Name of your package
      version = '1.0', #Package version
      packages=find_packages(), #Finds and includes all Python packages
      install_requires=['pandas','scipy'], #Required Dependancies
      author = 'Dr. REBEL-ious',
      description='A python script for detecting influential points',
      url="https://github.com/REBELABS/Regression-Influential-Points-Identification-Python",)
