# -*- coding: utf-8 -*-
from setuptools import setup,find_packages
import os,sys
import logging

developMode = False
if len(sys.argv) >= 2:
    if sys.argv[1] == "develop": developMode = True
if developMode:
    logging.warning("You have sleected a developer model ( local install)")


VERSION ="0.0.1"

# def parse_requirements(requirements):
#     with open(requirements) as f:
#         return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]

# reqs = parse_requirements("requirements.txt")


#------------------------- INSTALL--------------------------------------------
setup(name = 'pyCGM2-wheelchair',
    version = VERSION,
    author = 'Fabien Leboeuf',
    author_email = 'fabien.leboeuf@gmail.com',
    description = "pyCGM2 extension for processing wheelchair",
    long_description= "",
    url = '',
    keywords = 'Wheelchair',
    packages=find_packages(),
	include_package_data=True,
    license='CC-BY-SA',
	install_requires = reqs,
    classifiers=['Programming Language :: Python',
                 'Programming Language :: Python :: 3.7',
                 'Operating System :: Microsoft :: Windows',
                 'Natural Language :: English'],
    # entry_points={
    #       'console_scripts': [
    #             # NEXUS
    #             'pyCGM2f-init  =  pyCGM2f.commands.commands:initiatingCommand',
    #             'pyCGM2f-edit  =  pyCGM2f.commands.commands:editingCommand',
    #             'pyCGM2f-process  =  pyCGM2f.commands.commands:processingCommand',
    #             'pyCGM2f-report  =  pyCGM2f.commands.commands:reportingCommand',
    #             'pyCGM2f-check  =  pyCGM2f.commands.commands:checkingCommand',
    #             'pyCGM2f-pushMongoDB  =  pyCGM2f.commands.commands:pushMongoDbCommand',
    #             'pyCGM2f-push  =  pyCGM2f.commands.commands:pushingCommand',
    #             'pyCGM2f-interpret  =  pyCGM2f.commands.commands:interpretingCommand',
    #             'pyCGM2f-nantes-convertExam  =  pyCGM2f.commands.commands:convertOldExam'
    #       ]
    #   },
    )
