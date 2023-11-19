# views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import profile  # Adjusted model name to follow Python conventions
import pdfkit
import io

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

def resume(request, id):
    user_profile = profile.objects.get(pk=id)
    template = loader.get_template('pdf/get_cv.html')
    html = template.render({'user_profile': user_profile})  

    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8'
    }

    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'  # Fix this line

    return response
