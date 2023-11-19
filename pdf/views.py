from django.shortcuts import render
from .models import profile

def accept(request):
    if request.method == 'POST':
        # Retrieve form data using request.POST.get()
        name = request.POST.get("Name","")
        Email = request.POST.get("Email", "")
        Phone = request.POST.get("Phone", "")
        Summary = request.POST.get("Summary", "")
        Degree = request.POST.get("Degree", "")
        School = request.POST.get("School", "")
        University = request.POST.get("University", "")
        Previous_work = request.POST.get("Previous_work", "")
        Skills = request.POST.get("Skills", "")

        # Create a new Profile instance with form data
        profile_instance = profile(
            name=name,
            email=Email,
            phone=Phone,
            summary=Summary,
            degree=Degree,
            school=School,
            university=University,
            previous_work=Previous_work,
            skills=Skills,
        )

        # Save the profile instance to the database
        profile_instance.save()

    # else:
    #     # Render the form template for GET requests
    #     return render(request, 'pdf/base.html')

    # Render the form template after processing the POST request
    return render(request, 'pdf/base.html')
