from django.shortcuts import render
from .models import Track
from .forms import TrackForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def track_list(request):
    tracks = Track.objects.all()
    return render(request, 'music/track_list.html', {'tracks': tracks})
def track_detail(request, pk):
    track = Track.objects.get(pk=pk)
    return render(request, 'music/track_detail.html', {'track': track})

def track_create(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            track = form.save() 
            return redirect('track_detail', pk=track.pk)
    else:
        form = TrackForm()
    return render(request, 'music/track_form.html', {'form': form})


def track_update(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES, instance=track)
        if form.is_valid():
            form.save()
            return redirect('track_detail', pk=pk)
    else:
        form = TrackForm(instance=track)
    return render(request, 'music/track_form.html', {'form': form})
def track_delete(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        track.delete()
        return redirect('track_list')
    return render(request, 'music/track_confirm_delete.html', {'track': track})