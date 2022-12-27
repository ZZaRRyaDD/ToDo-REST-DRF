from apps.account.factories import UserFactory
from apps.todos.factories import TaskFactory
from apps.wall.factories import CommentFactory, PostFactory

COUNT_USERS = 10


def run():
    """Generate examples."""
    users = UserFactory.create_batch(size=COUNT_USERS)
    for user in users:
        task = TaskFactory.create(user=user)
        post = PostFactory.create(user=user, task=task)
        for commentator in users:
            CommentFactory.create(user=commentator, post=post)
