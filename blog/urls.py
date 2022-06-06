from django.urls import path
from . views import *

app_name = 'blog'

urlpatterns = [
    path('api/blogs', BlogView.as_view(), name='blogs'),
    path('api/opportunities', OpportunityView.as_view(), name='opportunities'),
]
