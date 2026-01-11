from django.shortcuts import render, redirect

COURSES = {
    "web-development": {
        "slug": "web-development",
        "title": "Web Development",
        "category": "Fullstack Web",
        "description": "Belajar membangun aplikasi web modern dan scalable.",
        "what_you_learn": [
            "HTML, CSS, JavaScript",
            "React & Next.js",
            "Tailwind CSS",
            "Backend API & Deployment",
        ],
        "benefits": [
            "Portfolio project",
            "Mentoring privat",
            "Akses materi seumur hidup",
        ],
"schedule": ["Online", "Flexible", "12 Minggu"]
    },
    "python-engineering": {
        "slug": "python-engineering",
        "title": "Python Engineering",
        "category": "Python & Data",
        "description": "Dari automation hingga backend dan AI integration.",
        "what_you_learn": [
            "Python Fundamental",
            "Django Backend",
            "Automation Script",
            "Data & AI dasar",
        ],
        "benefits": [
            "Real-world project",
            "Mentor profesional",
            "Sertifikat",
        ],
        "schedule": ["Online", "Live Session", "10 Minggu"],
    },
    "mobile-development": {
        "slug": "mobile-development",
        "title": "Mobile Development",
        "category": "Mobile Apps",
        "description": "Bangun aplikasi Android & iOS dari satu codebase.",
        "what_you_learn": [
            "Flutter & Dart",
            "UI/UX Mobile",
            "API Integration",
            "App Deployment",
        ],
        "benefits": [
            "Build 2 Apps",
            "Career guidance",
            "Community access",
        ],
        "schedule": ["Online", "Project-based", "12 Minggu"],
    },
}


def home(request):
    return render(request, "home.html")

def course_detail(request, slug):
    course = COURSES.get(slug)
    return render(request, "detail.html", {"course": course})

def course_register(request, slug):
    course = COURSES[slug]

    if request.method == 'POST':
        request.session['form_data'] = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'gender': request.POST.get('gender'),
            'age': request.POST.get('age'),
            'city': request.POST.get('city'),
            'education': request.POST.get('education'),
            'experience': request.POST.get('experience'),
            'goal': request.POST.get('goal'),
            'device': request.POST.get('device'),
        }
        return redirect('course_confirm', slug=slug)

    return render(request, 'daftar.html', {'course': course})



def course_confirm(request, slug):
    course = COURSES[slug]
    data = request.session.get('form_data')

    return render(request, 'konfirmasi.html', {
        'course': course,
        'data': data
    })

def process_payment(request, slug):
    if request.method == "POST":
        return redirect('payment_success', slug=slug)

def payment_success(request, slug):
    course = COURSES[slug]
    return render(request, 'payment_success.html', {'course': course})

def about(request):
    return render(request, 'about.html')

