# views.py

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import profile  # Adjusted model name to follow Python conventions
import pdfkit
import io


def home(request):
    return render(request,'pdf/home.html')

def accept(request):
    if request.method == 'POST':
        # Retrieve form data using request.POST.get()
        name = request.POST.get("Name", "")
        email = request.POST.get("Email", "")
        phone = request.POST.get("Phone", "")
        summary = request.POST.get("Summary", "")
        degree = request.POST.get("Degree", "")
        school = request.POST.get("School", "")
        university = request.POST.get("University", "")
        previous_work = request.POST.get("Previous_work", "")
        skills = request.POST.get("Skills", "")

        # Create a new Profile instance with form data
        profile_instance = profile(
            name=name,
            email=email,
            phone=phone,
            summary=summary,
            degree=degree,
            school=school,
            university=university,
            previous_work=previous_work,
            skills=skills,
        )

        # Save the profile instance to the database
        profile_instance.save()

    # Render the form template after processing the POST request
    return render(request, 'pdf/base.html')

#we get a specific user id and convert the webpage into the pdf so user can downlaod it as required.

from django.http import HttpResponse
from django.template import loader
from .models import profile  # Import your 'profile' model
import pdfkit

def resume(request, id):
    user_profile = profile.objects.get(pk=id)
    template = loader.get_template('pdf/get_cv.html')
    html = template.render({'user_profile': user_profile})

    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8'
    }

    pdf = pdfkit.from_string(html, False, options)

    # Set the filename based on the 'name' column in the database
    filename = f"{user_profile.name}_{user_profile.id}_resume.pdf"

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response



def get_list(request):

    list=profile.objects.all()

    return render(request,'pdf/all_list.html',{'all_data':list})

def delete_data(request,id):
    delete_list=profile.objects.get(pk=id)
    delete_list.delete()

    return redirect("cv:data_list")


def view_cv(request, id):
    view_data = get_object_or_404(profile, pk=id)  # Use get_object_or_404 to handle the case when the object is not found
    return render(request, 'pdf/view_cv.html', {'view': [view_data]})