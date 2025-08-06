from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render
from django.core.files.storage import default_storage

def upload_file(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]
        file_name = default_storage.save(file.name, file)
        return render(request, "upload.html", {
            "message": f"✅ File uploaded successfully as {file_name}"
        })
    return render(request, "upload.html")


def home(request):
    return HttpResponse("Hello World from Django!")

