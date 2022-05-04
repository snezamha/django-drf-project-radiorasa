from django.db import models
from django_resized import ResizedImageField

# Create your models here.


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Audio(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    artwork = ResizedImageField(validators=[validate_file_extension], size=[500, 500], crop=[
        'middle', 'center'], upload_to='audios/cover/%Y/%m/%d/', verbose_name="کاور")
    url = models.FileField(upload_to='audios/')
    durations = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="آخرین به روز رسانی")

    def __str__(self):
        return self.title
