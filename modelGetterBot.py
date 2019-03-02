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
        Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
    json: To help with json parsing
    pprint: To help with printing things prettily
    os: To help with directory and file navigation
    urllib2: To interact with URLs
LOCAL FILES
    ./config (dir)
    ./data (dir)


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
def loadJson (jsonPath):
    with open(jsonPath, 'r') as readjson:
        try:
            jsonText = json.load(readjson)
        except:
            return False
        return jsonText



"""
--PRIVATE FUNCTION--
The function that will run for each config type of postURL
"""
def postUrl (configJSON):
    '''Wrap this in a loop in case there are multiple urls to check'''
    thisReturn = []
    for url in configJSON['baseUrls']:
        parentElement = configJSON['parentElement']
        pElement = parentElement['element']
        pPropertyType = parentElement['propertyType']
        pPropertyLabel = parentElement['propertyLabel']
        target = configJSON['target']
        tElement = target['element']
        tPropertyType = target['propertyType']
        tPropertyLabel = target['propertyLabel']

        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, features='html.parser', from_encoding=page.info().get_param('charset'))

        '''This returns all full <a> tags. Need to just return the href part'''
        thisReturn.append(soup.select('#' + pPropertyLabel + ' ' + tElement))

    return thisReturn



"""
--PRIVATE FUNCTION--
This function gets an indivudual model info. Split up so getModels function can loop through this if needed
DO NOT RUN THIS FUNCTION - it shoud only be called from getModels
"""
def getModel (configName, config):
    if config['configType'] == 'postUrl':
        return postUrl (config)
    elif config['configType'] == '???':
        return 'The ??? config type has not been set up yet'
    else:
        return config['configType'] + ' has not been set up yet'


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
def getModels (modelName):

    allConfigs = loadJson(configFile)
    if allConfigs == False:
        pp.pprint('Config File is not valid json.')
        return False

    if modelName == '':
        thisReturn = []
        for config in allConfigs:
            thisConfigName = config
            thisConfig = allConfigs[config]
            thisReturn.append(getModel(thisConfigName, thisConfig))

    else:
        thisConfigName = modelName
        thisConfig = allConfigs[thisConfigName]
        thisReturn = getModel(thisConfigName, thisConfig)

    return thisReturn



"""
This function writes all the models into the data file
"""
def writeModels (models):

    """Validate the json file"""
    if isValidJson(dataFile) == False:
        pp.pprint('Data File is not valid json.')
        return False

    allData = loadjson(dataFile)
    return models


print(getModels(''))
