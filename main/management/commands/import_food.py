import csv
from django.core.management.base import BaseCommand
from addProduct.models import Food

class Command(BaseCommand):
    help = 'Import food data from CSV'

    def handle(self, *args, **kwargs):
        with open("//Users//athallah//Documents//PBP/mangan-yuk//dataset.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Food.objects.create(
                    name=row['Produk Makanan'],
                    restaurant=row['Restoran'],
                    deskripsi=row['Lokasi'],
                    price=float(row['Harga']),
                    preference=row['Preferensi'],
                    image_url=row['URL_Gambar']
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
    