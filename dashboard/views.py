from os import link
from django.shortcuts import redirect, render
from django.contrib import messages
from . forms import *
from . models import *
from django.views import generic
from youtubesearchpython import VideosSearch
import requests 
import wikipedia
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'], description=request.POST['description'], file=request.FILES['file'])
            notes.save()
        messages.success(request, f"Notes Added by {request.user.username} successfully!")
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes, 'form':form}
    return render(request, 'dashboard/notes.html',context)

@login_required
def delete_note(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")

class NotesDetailView(generic.DetailView):
    model = Notes

def youtube(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit=10)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime'],
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            result_list.append(result_dict)
            context = {
                'form':form,
                'results':result_list
            }
        return render(request, 'dashboard/youtube.html', context)    
    else:
        form = DashboardForm()
    context = {'form':form}
    return render(request, "dashboard/youtube.html", context)

def books(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q="+text
        r = requests.get(url)
        answer = r.json()
        result_list = []
        for i in range(10):
            result_dict = {
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview':answer['items'][i]['volumeInfo'].get('previewLink'),
            }
            result_list.append(result_dict)
            context = {
                'form':form,
                'results':result_list
            }
        return render(request, 'dashboard/books.html', context)    
    else:
        form = DashboardForm()
    context = {'form':form}
    return render(request, "dashboard/books.html", context)

def dictionary(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r = requests.get(url)
        answer = r.json()
        try:
            phonetics = answer[0]['phonetics'][0]['text']
            audio = answer[0]['phonetics'][0]['audio']
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            example = answer[0]['meanings'][0]['definitions'][0]['example']
            synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']
            context = {
                'form':form,
                'input':text,
                'phonetics':phonetics,
                'audio':audio,
                'definition':definition,
                'example':example,
                'synonyms':synonyms
            }
        except:
            context = {
                'form':form,
                'input':''
            }
        return render(request, "dashboard/dictionary.html", context)
    else:
        form = DashboardForm()
        context = {'form':form}
    return render(request, "dashboard/dictionary.html", context)

def wiki(request):
    if request.method == 'POST':
        text = request.POST['text']
        form = DashboardForm(request.POST)
        search = wikipedia.page(text)
        context = {
            'form':form,
            'title':search.title,
            'link':search.url,
            'details':search.summary
        }
        return render(request, "dashboard/wiki.html", context)
    else:
        form = DashboardForm()
        context = {
            'form':form
        }
    return render(request, "dashboard/wiki.html", context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}.")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    context = {
        'form':form
    }
    return render(request, "dashboard/register.html", context)

def references(request):
    # if request.method == "POST":
    #     form = ReferencesForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         references = References(user=request.user, title=request.POST['title'], subject=request.POST['subject'], description=request.POST['description'], file=request.FILES['file'])
    #         references.save()
    #     messages.success(request, "Refernce material added successfully!")
    # else:
    #     form = ReferencesForm()
    # references = ReferencesForm.objects.all()
    # context = {'references':references, 'form':form}
    references = References.objects.all()
    context = {'references':references}
    return render(request, 'dashboard/references.html',context)


class ReferencesDetailView(generic.DetailView):
    model = References