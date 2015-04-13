from django.db import models
from django.forms import ModelForm
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

#use the requests library to import data from link for the assignment (https://github.com/kennethreitz/requests)
import requests 

# MedicalData model here: for now just have all fields to be strings
class MedicalData(models.Model):
    author = models.CharField(max_length=1000, blank=True)
    author_email = models.CharField(max_length=1000, blank=True) #none
    ckan_url = models.CharField(max_length=1000, blank=True)
    extras = models.CharField(max_length=1000, blank=True) #dicts
    groups = models.CharField(max_length=1000, blank=True) #list
    id = models.CharField(max_length= 1000, primary_key = True)
    isopen = models.CharField(max_length= 1000, blank=True) #boolean
    license = models.CharField(max_length= 1000, blank=True)
    license_id = models.CharField(max_length= 1000, blank=True)
    license_title = models.CharField(max_length=1000, blank=True)
    maintainer = models.CharField(max_length=1000, blank=True) #none
    maintainer_email = models.CharField(max_length=1000, blank=True) #none
    metadata_created = models.CharField(max_length=1000, blank=True)
    metadata_modified = models.CharField(max_length=1000, blank=True)
    name = models.CharField(max_length=1000, blank=True)
    notes = models.CharField(max_length= 1000, blank=True)
    notes_rendered = models.CharField(max_length= 1000, blank=True)
    num_resources = models.CharField(max_length=1000, blank=True) #models.IntegerField(default=0)
    num_tags = models.CharField(max_length=1000, blank=True) #models.IntegerField(default=0)
    organization = models.CharField(max_length=1000, blank=True) #none
    owner_org = models.CharField(max_length=1000, blank=True) #none
    private = models.CharField(max_length= 1000, blank=True) #boolean
    ratings_average = models.CharField(max_length=1000, blank=True) #none
    ratings_count = models.CharField(max_length=1000, blank=True) #models.IntegerField(default=0)
    relationships = models.CharField(max_length=1000, blank=True) #list
    resources = models.CharField(max_length=1000, blank=True) #list/dict
    revision_id = models.CharField(max_length=1000, blank=True)
    state = models.CharField(max_length=1000, blank=True)
    tags = models.CharField(max_length=1000, blank=True) #list
    title = models.CharField(max_length=1000, blank=True)
    tracking_summary = models.CharField(max_length=1000, blank=True) #dict
    type = models.CharField(max_length=1000, blank=True)
    url = models.CharField(max_length=1000, blank=True)
    version = models.CharField(max_length=1000, blank=True) #None/null

#import data from link and write to database
def importdata():
    r = requests.get("http://hub.healthdata.gov/api/2/rest/dataset/c447002d-51df-46d9-a105-dda94dfd6083")
    jsonDict = r.json()
    
    #remove the unicode from the keys
    for key in jsonDict.keys():
        jsonDict[key.encode('ascii','ignore')]=jsonDict.pop(key)
    
    q = MedicalData()
    
    #set the fields of the MedicalData model
    for key in jsonDict:
        setattr(q, key, str(jsonDict[key])) 

    q.save()

#call the function to import data from the link given from the assignment
importdata()

    
