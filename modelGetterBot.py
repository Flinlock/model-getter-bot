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
    ./??? (dir)


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
    dataFile
        The file name that has the JSON data in
        Change this variable if the configuration file location changes

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

#Local Files
configFile = 'config/dell.json'
dataFile = 'data/db.json'



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
        parentElement = configJSON['parentElement']
        pElement = parentElement['element']
        pPropertyType = parentElement['propertyType']
        pPropertyLabel = parentElement['propertyLabel']
        target = configJSON['target']
        tElement = target['element']
        tProperty = target['property']

        #page = urllib.request.urlopen(url)
        #soup = BeautifulSoup(page, from_encoding=page.info().get_param('charset'))
        '''find a way to get only links in certain divs'''
        #for link in soup.find_all('a'):
        #    print(link.get('href'))
        print (parentElement['element'])


"""
This is the function you should run to get models. If model is blank, will return all models in config file

RETURN FORMAT:
{
    "Dell": {
        "adamo": {
            "title": "Adamo 13",
            "baseURL": "url"
            }
        }
    }
}
"""
def getModels (model):

    """Validate the json file"""
    if loadjson(configFile) == False:
        pp.pprint('Config File is not valid json. Please validate at https://jsonlint.com/')
        return False

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


"""
This function writes all the models into the data file
"""
def writeModels (models):

    """Validate the json file"""
    if loadjson(dataFile) == False:
        pp.pprint('Data File is not valid json. Please validate at https://jsonlint.com/')
        return False

    allData = loadjson(dataFile)
    return models
