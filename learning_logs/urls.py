"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from . import views

app_name = 'learning_logs'

urlpatterns = [
  # Home page
  url(r'^$', views.index, name='index'),

  # Show All Topics
  url(r'^topics/$', views.topics, name='topics'),
  # Detail page for a single topic
  url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
  # New topic
  url(r'^new_topic/$', views.new_topic, name='new_topic'),
  # New entry
  url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
  # Edit entry
  url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
