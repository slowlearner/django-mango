from django.conf.urls import patterns, include, url


urlpatterns = patterns('proposal.views',
    url(r'^$', 'proposal_list', name='proposal_list'),
    url(r'^create/$', 'proposal_create', name='proposal_create'),
    url(r'^(?P<slug>[-\w]+)$', 'proposal_detail', name='proposal_detail'),
    url(r'^(?P<slug>[-\w]+)/(?P<status>approved|declined)/$',
        'proposal_update_status', name='proposal_update_status'),
)
