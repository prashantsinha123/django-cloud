from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album,song,video,document
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserCreateForm


'''def index(request):
	all_albums=Album.objects.all()
	context={'all_albums':all_albums}
	return render(request,'music/index.html',context)


def detail(request,album_id):
	album=get_object_or_404(Album,pk=album_id)
	return render(request,'music/detail.html',{'album':album})
'''
class Index(ListView):
	template_name='music/index.html'
	context_object_name='all_albums'
	def get_queryset(self):
		return Album.objects.all()

class Detail(DetailView):
	model=Album
	template_name='music/detail.html'

class Create(CreateView):
	model=Album
	template_name='music/create.html'
	fields=['artist','album_title','album_logo']

class Update(UpdateView):
	model=Album
	template_name='music/create.html'
	fields=['artist','album_title','album_logo']

class Delete(DeleteView):
	model=Album
	success_url=reverse_lazy('music:index')

class AddSong(CreateView):
	model=song
	template_name='music/songs.html'
	fields=['album','song_title','file_type']
	success_url='/music/'

def song_delete(request, album_id, song_id):
	album = get_object_or_404(Album, pk=album_id)
	song1 = song.objects.get(pk=song_id)
	song1.delete()
	return render(request, 'music/detail.html', {'album': album})

class SongList(ListView):
	model=Album
	context_object_name='all_albums'
	template_name='music/songlist.html'
	

class Video(CreateView,ListView):
	model=video
	context_object_name='all_video'
	template_name='music/vcreate.html'
	fields=['artist','video_title','video_logo']
	success_url=reverse_lazy('music:create')

class VideoList(ListView):
	model=video
	context_object_name='all_video'
	template_name='music/videolist.html'

class Doc(CreateView,ListView):
	model=document
	context_object_name='all_doc'
	template_name='music/document.html'
	fields=['document_title','doc_url']
	success_url=reverse_lazy('music:docs')

def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

def logout_user(request):
	logout(request)
	form = UserForm(request.POST or None)
	context = {
		"form": form,
    		}
	return render(request, 'music/login.html', context)
 
class Deletev(DeleteView):
	model=video
	success_url=reverse_lazy('music:create')

class DeleteDoc(DeleteView):
	model=document
	success_url=reverse_lazy('music:docs')
	




