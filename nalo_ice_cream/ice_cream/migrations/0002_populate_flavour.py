from django.db import migrations, models

def populate_flavour(apps, schema):
    Flavour = apps.get_model('ice_cream', 'Flavour')

    Flavour.objects.create(name='Cherry',           img_path='ice_cream/cherry.jpg')
    Flavour.objects.create(name='Chocolate-Orange', img_path='ice_cream/chocolate-orange.jpg')
    Flavour.objects.create(name='Pistachio',        img_path='ice_cream/pistachio.jpg')
    Flavour.objects.create(name='Raspberry',        img_path='ice_cream/raspberry.jpg')
    Flavour.objects.create(name='Vanilla',          img_path='ice_cream/vanilla.jpg')


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ice_cream", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(populate_flavour)
    ]
