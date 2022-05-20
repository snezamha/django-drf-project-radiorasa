from django.db import models
from django_resized import ResizedImageField
# Create your models here.


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            'فرمت فایل ارسالی معتبر نیست. فرمت های معتبر : jpg و png  می باشد.')
    if value.size > 2621440:
        raise ValidationError(
            'حجم فایل ارسالی می بایست کمتر از 2.5 مگا بایت باشد.')


class Audio(models.Model):
    title = models.CharField(max_length=250,verbose_name="عنوان")
    artwork = ResizedImageField(validators=[validate_file_extension], size=[500, 500], crop=[
        'middle', 'center'], blank=True, null=True, upload_to='audios/cover/%Y/%m/%d/', verbose_name="کاور")
    url = models.FileField(upload_to='audios/',verbose_name="انتخاب فایل صوتی")
    sort = models.IntegerField(verbose_name="موقعیت")
    date = models.DateTimeField(verbose_name="تاریخ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="آخرین به روز رسانی")

    class Meta:
        verbose_name = 'بخش'
        verbose_name_plural = 'لیست پخش'

    def __str__(self):
        return self.title
