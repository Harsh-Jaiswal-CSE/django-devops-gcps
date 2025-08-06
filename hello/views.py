from django.shortcuts import render
from google.cloud import storage
from django.conf import settings
import os

def upload_file(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]

        # Initialize GCP Storage Client
        storage_client = storage.Client()
        bucket_name = "hello-django-bucket"  # 🔹 Replace with your bucket name
        bucket = storage_client.bucket(bucket_name)

        # Upload file
        blob = bucket.blob(file.name)
        blob.upload_from_file(file, content_type=file.content_type)

        return render(request, "upload.html", {
            "message": f"✅ File uploaded successfully to GCS as {file.name}"
        })

    return render(request, "upload.html")
