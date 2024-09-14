from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import subprocess
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.core.exceptions import ValidationError
from .file_validation import validate_apk_file
from .apk_processing import enhance_security

@csrf_exempt
def upload_apk(request):
    if request.method == 'POST' and 'apk_file' in request.FILES:
        apk_file = request.FILES['apk_file']

        # Validate file type and size
        try:
            validate_apk_file(apk_file)
        except ValidationError as e:
            return HttpResponseBadRequest(f"Invalid file: {e}")

        fs = FileSystemStorage()
        filename = fs.save(apk_file.name, apk_file)
        uploaded_file_url = fs.url(filename)

        # Get selected enhancements
        enhancements = request.POST.getlist('enhancements')

        try:
            # Process the APK
            enhanced_apk_path = enhance_security(fs.path(filename), enhancements)
            enhanced_apk_url = fs.url(os.path.basename(enhanced_apk_path))
        except Exception as e:
            return HttpResponseBadRequest(f"Error processing APK: {e}")

        return render(request, 'security_enhancer/result.html', {
            'original_file': uploaded_file_url,
            'enhanced_file': enhanced_apk_url,
            'enhancements': enhancements
        })

    return render(request, 'security_enhancer/upload.html')
