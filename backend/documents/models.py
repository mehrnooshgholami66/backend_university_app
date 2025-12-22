# documents/models.py
import os
import uuid
from django.db import models
from django.conf import settings


def upload_path(instance, filename):
    """
    documents/<file_type>/<uuid>.<ext>
    """
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join(
        "documents",
        instance.file_type,
        filename
    )


class Document(models.Model):
    DOCUMENT = "document"
    ARTICLE = "article"

    TYPE_CHOICES = [
        (DOCUMENT, "Document"),
        (ARTICLE, "Article"),
    ]

    title = models.CharField(max_length=255)

    file = models.FileField(
        upload_to=upload_path   # 👈 این خط مهم‌ترینه
    )

    file_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )

    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

