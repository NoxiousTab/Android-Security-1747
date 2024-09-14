from django.core.exceptions import ValidationError

def validate_apk_file(file):
    # Check file extension
    if not file.name.endswith('.apk'):
        raise ValidationError('Invalid file type. Please upload an APK file.')

    # Optional: Check file size (e.g., limit to 10MB)
    if file.size > 10 * 1024 * 1024:
        raise ValidationError('File size exceeds 10MB.')
