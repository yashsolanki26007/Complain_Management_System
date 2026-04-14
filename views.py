from django.shortcuts import render, redirect, get_object_or_404
from .models import Complaint
from .forms import ComplaintForm

def home(request):
    total = Complaint.objects.count()
    pending = Complaint.objects.filter(status='Pending').count()
    resolved = Complaint.objects.filter(status='Resolved').count()
    return render(request, 'complaints/home.html', {
        'total': total,
        'pending': pending,
        'resolved': resolved
    })

def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/submit.html', {'form': form})

def complaint_list(request):
    complaints = Complaint.objects.all().order_by('-submitted_at')
    status_filter = request.GET.get('status', '')
    if status_filter:
        complaints = complaints.filter(status=status_filter)
    return render(request, 'complaints/list.html', {
        'complaints': complaints,
        'status_filter': status_filter
    })

def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        complaint.status = new_status
        complaint.save()
        return redirect('complaint_list')
    return render(request, 'complaints/detail.html', {'complaint': complaint})

def delete_complaint(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    complaint.delete()
    return redirect('complaint_list')

def success(request):
    return render(request, 'complaints/success.html')