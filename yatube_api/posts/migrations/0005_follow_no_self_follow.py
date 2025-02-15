# Generated by Django 5.1.6 on 2025-02-15 20:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_follow_user_follow'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(condition=models.Q(('user', models.F('following')), _negated=True), name='no_self_follow', violation_error_message='Нельзя подписаться на самого себя'),
        ),
    ]
