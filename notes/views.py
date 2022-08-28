import json
from .context_processors import include_login_form
from django.contrib.auth.views import LoginView
from django.core import serializers
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.http import JsonResponse, request, HttpResponse, HttpResponseRedirect
from .forms import NoteForm, UserForm
from .models import Notes
from django.contrib.auth.models import User
from author.models import Author


# Create your views here.


def home_view(request):
    return render(request, 'notes/home.html')



class NotesView(ListView):
    model = Notes
    paginate_by = 5
    template_name = 'notes/notelist.html'


class Login(LoginView):
    form_class = include_login_form
    template_name = "notes/home.html"
    success_url = reverse_lazy('notes:home')

# class NotesDetailView(DetailView):
#    model = Notes
#    note_form = NoteForm()
#    template_name = 'notes/notesdetail.html'


def note_detail(request, pk):
    note = Notes.objects.get(id=pk)
    note_form = NoteForm()
    context = {
        'instance': note,
        'note_form': note_form,
    }

    return render(request, 'notes/notesdetail.html', context)


def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        author_id = request.POST.get('author')
        img = request.POST.get('image')

        author = Author.objects.get(id=author_id)

        Notes.objects.create(title=title, description=description, author=author, image=img)

    return redirect('notes:notes-list')


class SignUpView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'notes/signup.html'
    success_url = reverse_lazy('notes:sign-up')

    def form_valid(self, form):
        form.save()
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True}, status=201)
        return redirect(reverse('notes:sign-up'))

    def form_invalid(self, form):
        errors = form.errors
        return JsonResponse({'error': errors}, status=403)

    def form_submit(self, request, form, **kwargs):
        print("dsadsa")
        print(request.headers.get('x-requested-with'))
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # form = UserForm(request.POST)
            if form.is_valid():
                instance = form.save()
                form_instance = serializers.serialize('json', [instance, ])
                return JsonResponse({'success': True, 'instance': form_instance}, status=201)
            else:
                errors = form.errors
                errors_msg = serializers.serialize('json', [errors, ])
                return JsonResponse({'error': errors_msg}, status=403)
        return redirect('notes:sign-up')


def delete_note(request, pk):
    if request.method == 'POST':
        note_instance = Notes.objects.get(id=pk)
        note_instance.delete()

    return redirect('notes:notes-list')


class NoteDeleteView(DeleteView):
    model = Notes
