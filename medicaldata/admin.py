from django.contrib import admin
from medicaldata.models import MedicalData


class MedicalDataAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Author information', {'fields': ['author', 'author_email']}),
        ('Extras' , {'fields': ['extras']}),
        ('Groups' , {'fields': ['groups']}),
        ('Identification', {'fields': ['id', 'revision_id']}),
        ('Is open' , {'fields': ['isopen']}),     
        ('License information', {'fields': ['license', 'license_id', 'license_title']}),
        ('Maintainer information', {'fields': ['maintainer', 'maintainer_email']}),
        ('Metadata', {'fields': ['metadata_created', 'metadata_modified']}),
        ('Name', {'fields': ['name']}),
        ('Notes information', {'fields': ['notes', 'notes_rendered']}),
        ('Organization information', {'fields': ['organization', 'owner_org']}),
        ('Is private' , {'fields': ['private']}),
        ('Ratings information', {'fields': ['ratings_average', 'ratings_count']}),
        ('Relationships', {'fields': ['relationships']}),
        ('Resources', {'fields': ['resources','num_resources']}),
        ('State', {'fields': ['state']}),
        ('Tag Information', {'fields': ['tags', 'num_tags']}),
        ('Title', {'fields': ['title']}),
        ('Tracking Summary', {'fields': ['tracking_summary']}),
        ('Type', {'fields': ['type']}),
        ('Url Information', {'fields': ['url', 'ckan_url']}),
        ('Version', {'fields': ['version']}),

    ]
    list_display = ('name', 'author', 'id')
    
    #filter added
    list_filter = ['author','title']
    
    #search ability
    search_fields = ['author', 'title', 'id']
    


#makes the MedicalData app available
admin.site.register(MedicalData, MedicalDataAdmin)