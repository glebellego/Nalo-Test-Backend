
from django.db import migrations, models

def populate_stock(apps, schema):
    Flavour = apps.get_model('ice_cream', 'Flavour')
    Stock = apps.get_model('ice_cream', 'Stock')

    for flavour in Flavour.objects.all():
        Stock.objects.create(
            flavour = flavour,
            amount = 40
        )
    

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ice_cream", "0002_populate_flavour"),
    ]

    operations = [
        migrations.RunPython(populate_stock),
    ]
