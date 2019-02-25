"""
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
DESCRIPTION
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
This Bot is meant to scrape various computer manufacter's web sites and return a list of all modules of computers that that manufacterer has


<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
DEPENDANCIES
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
LIBRARIES
    BeautifulSoup: To help with web scraping
    json: To help with json parsing
    pprint: To help with printing things prettily
    os: To help with directory and file navigation
LOCAL FILES
    ./config (dir)

<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
VARIABLES
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
DEVELOPER DEFNED
    configDir
        The directory name that all of the configuration files are in.
        Change this variable if the configuration directory changes

AUTOMATED
    configFiles
        All of the file names listed inside the configDir that have the ending .json


<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
CHANGELOG
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
2019.02.24 - PaulM - Created
"""


#Load Dependancies
import json
import bs4 #BeautifulSoup
import pprint as pp
import os

#Grab All .json files in configFile
configDir = 'config'
configFiles = []

for file in os.listdir(configDir):
    if file.endswith(".json"):
        configFiles.append(os.path.join(configDir, file))
