# Generated by Django 2.1.15 on 2020-09-02 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE_ARRENDADOR', models.CharField(max_length=255)),
                ('NOMBRE_ARRENDATARIO', models.CharField(max_length=255)),
                ('SERVICIO_A_OFRECER', models.CharField(max_length=255)),
                ('FECHA_INICIO', models.DateTimeField(default='2021-09-02 16:19:25', null=True)),
                ('FECHA_FINAL', models.DateTimeField(default='2021-09-02 16:19:25', null=True)),
                ('PRECIO_INMUEBLE', models.FloatField()),
                ('PRECIO_DEPOSITO', models.FloatField()),
                ('MONTO_PENDIENTE', models.FloatField()),
                ('PORCENTAJE_AUMENTO', models.FloatField()),
                ('PLAZO_GRACIA', models.CharField(max_length=1)),
                ('DIRRECCION_ARRENDADOR', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODE', models.CharField(max_length=100)),
                ('ADDRESS', models.CharField(max_length=500)),
                ('PUBLIC_DEED', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LandLord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME_LANDLORD', models.CharField(max_length=200)),
                ('ADDRESS', models.CharField(max_length=500)),
                ('CURP', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FECHA', models.DateTimeField(auto_now_add=True)),
                ('MONTO', models.FloatField()),
                ('RESTANTE', models.FloatField(blank=True, default=None, null=True)),
                ('FECHA_LIMITE', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('size', models.FloatField()),
                ('photo', models.URLField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='api.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODE', models.CharField(max_length=10)),
                ('DESCRIPTION', models.CharField(max_length=500)),
                ('PRICE', models.FloatField()),
                ('DEPOSIT', models.FloatField()),
                ('PERCENT_INCREASE', models.FloatField()),
                ('type', models.CharField(max_length=50)),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='api.Estate')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='api.Pet')),
            ],
        ),
        migrations.AddField(
            model_name='pay',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pays', to='api.Property'),
        ),
        migrations.AddField(
            model_name='contract',
            name='DEPARTAMENTO',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='api.Property'),
        ),
    ]
