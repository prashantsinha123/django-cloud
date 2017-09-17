from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
app_name='music'
urlpatterns=[
	url(r'^$',views.Index.as_view(),name='index'),
	url(r'^login/$',login,{'template_name':'music/signup.html'}),
	url(r'^register/$',views.save,name='save'),
	url(r'^(?P<pk>[0-9]+)/$',views.Detail.as_view(),name='detail'),
	url(r'album/create/$',views.Create.as_view(),name='album-create'),
	url(r'album/(?P<pk>[0-9]+)/update/$',views.Update.as_view(),name='album-update'),
	url(r'album/(?P<pk>[0-9]+)/delete/$',views.Delete.as_view(),name='album-delete'),
	url(r'album/(?P<pk>[0-9]+)/$',views.AddSong.as_view(),name='song-add'),
	url(r'album/(?P<album_id>[0-9]+)/song/(?P<song_id>[0-9]+)/$',views.song_delete,name='song-delete'),
	url(r'^songs/', views.SongList.as_view(), name='songs'),
	url(r'^album/videos/(?P<pk>[0-9]+)/delete/$',views.Deletev.as_view(),name='video-delete'),
	url(r'^album/documents/$', views.Doc.as_view(), name='docs'),
	url(r'^album/videos/$', views.Video.as_view(), name='create'),
	url(r'^album/documents/(?P<pk>[0-9]+)/delete/$',views.DeleteDoc.as_view(),name='doc-delete'),
	
]
