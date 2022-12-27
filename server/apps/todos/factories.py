from datetime import datetime, timedelta

import factory
import pytz

from apps.todos import models
from apps.account.factories import UserFactory


class TaskFactory(factory.django.DjangoModelFactory):
    """Factory for Task model."""

    name = factory.Faker("name")
    description = factory.Faker("catch_phrase")
    is_done = factory.Faker("pybool")
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = models.Task
