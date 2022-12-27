import factory

from apps.account.factories import UserFactory
from apps.todos import models


class TaskFactory(factory.django.DjangoModelFactory):
    """Factory for Task model."""

    name = factory.Faker("name")
    description = factory.Faker("catch_phrase")
    is_done = factory.Faker("pybool")
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = models.Task
