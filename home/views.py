from django.shortcuts import render, redirect

KURSUS = {
    "web-dev": {
        "nama": "Web Development",
        "deskripsi": "Kursus ini dirancang untuk pemula hingga menengah yang ingin menjadi Web Developer profesional.",
        "materi": [
            "HTML5 & Semantic HTML",
            "CSS3 & Responsive Design",
            "JavaScript Dasar & Lanjutan",
            "React.js",
            "Project Website Nyata"
        ],
        "manfaat": [
            "Mampu membuat website modern & responsif",
            "Memahami workflow Frontend Developer",
            "Memiliki portfolio profesional",
            "Siap melamar kerja sebagai Web Developer"
        ],
        "durasi": "12 Minggu",
        "level": "Pemula - Menengah"
    },
    "python": {
        "nama": "Python Programming",
        "deskripsi": "Belajar Python dari dasar hingga penerapan di Data Science dan AI.",
        "materi": [
            "Python Dasar",
            "Struktur Data & OOP",
            "Data Analysis dengan Pandas",
            "Machine Learning Dasar",
            "Mini Project"
        ],
        "manfaat": [
            "Menguasai bahasa Python",
            "Mampu mengolah & menganalisis data",
            "Dasar kuat untuk AI & Machine Learning",
            "Peluang karir luas (Data, Backend, AI)"
        ],
        "durasi": "10 Minggu",
        "level": "Pemula"
    },
    "mobile": {
        "nama": "Mobile Development",
        "deskripsi": "Bangun aplikasi mobile Android & iOS dengan teknologi modern.",
        "materi": [
            "Dasar Mobile App",
            "Flutter & Dart",
            "React Native",
            "API Integration",
            "Build & Publish App"
        ],
        "manfaat": [
            "Mampu membuat aplikasi Android & iOS",
            "Menguasai cross-platform development",
            "Portfolio aplikasi nyata",
            "Siap menjadi Mobile Developer"
        ],
        "durasi": "14 Minggu",
        "level": "Menengah"
    }
}


def index(request):
    return render(request, 'home/index.html', {"kursus": KURSUS})

def detail(request, slug):
    return render(request, 'home/detail.html', {
        "kursus": KURSUS[slug],
        "slug": slug
    })

def daftar(request, slug):
    if request.method == "POST":
        return redirect('sukses')
    return render(request, 'home/daftar.html', {
        "kursus": KURSUS[slug]
    })

def sukses(request):
    return render(request, 'home/sukses.html')
