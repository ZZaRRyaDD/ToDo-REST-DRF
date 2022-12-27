import factory

from apps.wall import models
from apps.todos.factories import TaskFactory
from apps.account.factories import UserFactory


class PostFactory(factory.django.DjangoModelFactory):
    """Factory for Post model."""

    text = factory.Faker("catch_phrase")
    user = factory.SubFactory(UserFactory)
    task = factory.SubFactory(TaskFactory)

    class Meta:
        model = models.Post


class CommentFactory(factory.django.DjangoModelFactory):
    """Factory for Comment model."""

    text = factory.Faker("catch_phrase")
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)

    class Meta:
        model = models.Comment
