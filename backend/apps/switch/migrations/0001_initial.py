# Generated by Django 4.1.1 on 2022-10-05 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('hostname', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('switch_type', models.CharField(max_length=255)),
                ('port', models.IntegerField()),
                ('ipv4', models.GenericIPAddressField(protocol='IPv4')),
                ('ipv6', models.GenericIPAddressField(blank=True, null=True, protocol='IPv6')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='switches', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
