import factory
import faker

from mind_palace.account import models


class UserFactory(factory.django.DjangoModelFactory):

    username = 'john'
    email = 'john.doe@mail.com'
    password = 'password'

    class Meta:
        model = models.User