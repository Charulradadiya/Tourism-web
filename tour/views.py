from django.shortcuts import render,redirect
from .models import Tour,Reviews
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')

def service(request):
    searchTerm = request.GET.get('search')
    if searchTerm:
        tours = Tour.objects.filter(title=searchTerm)
    else:
         tours=Tour.objects.all()
    return render(request,'service.html',{'tours':tours})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def detail(request,tour_id):
        tours = get_object_or_404(Tour,pk=tour_id)
        reviews = Reviews.objects.filter(tour = tours) 
        return render(request, 'detail.html',{'tour':tours,'reviews': reviews})

@login_required
def createreview(request, tour_id):
        tour = get_object_or_404(Tour,pk=tour_id)
        if request.method == 'GET':
            return render(request, 'createreview.html', {'tour': tour})
        else:
            try:
                myreview = request.POST.get('myreview')
                newReview = Reviews()
                newReview.user = request.user
                newReview.tour = tour
                newReview.text = myreview
                newReview.save()
                return redirect('detail', newReview.tour.id)
            except ValueError:
                return render(request, 'createreview.html', {'error':'bad datapassed in'})

@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Reviews,pk=review_id,user=request.user)
    if request.method == 'GET':
        return render(request, 'updatereview.html', {'review': review})
    else:
        try:
            review.text = request.POST.get('myreview')
            review.save()
            return redirect('detail', review.tour.id)
        except ValueError:
            return render(request, 'updatereview.html', {'review': review, 'error':'Bad data in form'})

@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Reviews, pk=review_id,user=request.user)
    review.delete()
    return redirect('detail', review.tour.id)