

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='assignedDoctorId',
        ),
    ]
