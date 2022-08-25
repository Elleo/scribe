from django.db import models
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor

class Show(models.Model):
    name = models.CharField(max_length=255)
    script = models.TextField(null=True, blank=True)
    language = models.CharField(default='en-us', max_length=32, choices=[
        ("ca", "Catalan"),
        ("cn", "Chinese"),
        ("cs", "Czech"),
        ("nl", "Dutch"),
        ("en-us", "English (US)"),
        ("en-gb", "English (British)"),
        ("en-in", "English (Indian)"),
        ("es", "Esperanto"),
        ("fa", "Farsi"),
        ("fr", "French"),
        ("de", "German"),
        ("hi", "Hindi"),
        ("it", "Italian"),
        ("ja", "Japanese"),
        ("kz", "Kazakh"),
        ("pl", "Polish"),
        ("ru", "Russian"),
        ("es", "Spanish"),
        ("tr", "Turkish"),
        ("vn", "Vietnamese"),
        ("uk", "Ukranian")])
    prioritise_accuracy = models.BooleanField(default=False)
    image = fields.ImageField(null=True, blank=True, dependencies=[
        FileDependency(processor=ImageProcessor(
            format='JPEG', scale={'max_width': 1280, 'max_height': 1280})
            )
        ])

    def __str__(self):
        return self.name
