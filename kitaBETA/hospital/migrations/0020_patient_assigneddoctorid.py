

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_remove_patient_assigneddoctorid'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='assignedDoctorId',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
