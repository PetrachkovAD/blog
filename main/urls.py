from django.conf.urls import url, include
from . import views as v

urlpatterns = [
    url(r'^$', v.articale_list, name='articale_list'),
    url(r'^articale/', include([
        url(r'^(?P<pk>[0-9+])/$', v.articale_detail, name='articale_detail'),
        url(r'^new/$', v.articale_new, name='articale_new'),
        url(r'^(?P<pk>[0-9+])/edit/$', v.articale_edit, name='articale_edit'),
        url(r'^search/$', v.articale_search, name='articale_search'),
    ])),
]
