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
    urllib2: To interact with URLs
LOCAL FILES
    ./config (dir)

<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
ENVIRONMENT
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
PYTHON: 3.7.2
BEAUTIFULSOUP (bs4):

<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
VARIABLES
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
DEVELOPER DEFNED
    configFile
        The file name that has the JSON configureation in
        Change this variable if the configuration file location changes

AUTOMATED
    configFiles
        All of the file names listed inside the configDir that have the ending .json


<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
CHANGELOG
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
2019.02.24 - PaulM: Created
2019.02.25 - PaulM: Added
                loadjson - function
                postUrl - function
                section that loops through different values in json and runs different functions
"""


#Load Dependancies
import json
from bs4 import BeautifulSoup
import pprint as pp
import os
import urllib.request

configFile = 'config/dell.json'

#Code to pull the path of all files ending with '.json' with configDir being the name of the directory
#for file in os.listdir(configDir):
#    if file.endswith(".json"):
#        configFiles.append(os.path.join(configDir, file))



"""
loadjson validates the json in jsonPath
If it loads correctly, it'll return the json object. If it loads incorrectly, it'll return False
"""
def loadjson (jsonPath):
    with open(configFile, 'r') as readjson:
        try:
            config = json.load(readjson)
        except:
            return False
        return config


"""
The function that will run for each config type of postURL
"""
def postUrl (configJSON):
    '''Wrap this in a loop in case there are multiple urls to check'''
    for url in configJSON['baseUrls']:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, from_encoding=page.info().get_param('charset'))
        '''find a way to get only links in certain divs'''
        #for link in soup.find_all('a')
        #    print(link.get('href'))


"""
This section of code is what actually runs
"""
if loadjson(configFile) == False:
    pp.pprint('Config File is not valid json. Please validate at https://jsonlint.com/')
else:
    allConfigs = loadjson(configFile)
    for config in allConfigs:
        thisConfigName = config
        thisConfig = allConfigs[config]

        if thisConfig['configType'] == 'postUrl':
            postUrl (thisConfig)
        elif thisConfig['configType'] == '???':
            pp.pprint('This config type has not been set up yet')
        else:
            pp.pprint(thisConfig['configType'] + ' has not been set up yet')
