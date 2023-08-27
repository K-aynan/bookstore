<<<<<<< HEAD
import factory 

from django.contrib.auth.models import User
from product.factories import ProductFactory
from order.models import Order

class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')
=======
import factory
from django.contrib.auth.models import User

from order.models import Order
from product.factories import ProductFactory


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("pystr")
    username = factory.Faker("pystr")
>>>>>>> 1e4bc09f8054df132a7460d0f0fd37450506453a

    class Meta:
        model = User

<<<<<<< HEAD
class OrderFactory(factory.django.DjangoModelFactory):
    User = factory.SubFactory(UserFactory)

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        
=======

class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return

>>>>>>> 1e4bc09f8054df132a7460d0f0fd37450506453a
        if extracted:
            for product in extracted:
                self.product.add(product)

    class Meta:
        model = Order