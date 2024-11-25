from django.db import models
import uuid


class Artikel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    judul = models.CharField(max_length=200)  # Maksimum panjang 200 karakter
    tanggal = models.DateField(auto_now_add=True)  # Secara otomatis menggunakan tanggal saat artikel dibuat
    isi = models.TextField()  # Untuk teks panjang
    gambar_url = models.URLField(max_length=1000)  # URL gambar dengan panjang maksimum 500 karakter

    def __str__(self):
        return self.judul
