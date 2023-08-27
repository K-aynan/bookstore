<<<<<<< HEAD
import factory 

from product.models import Product
from product.models import Category

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('pystr')
=======
import factory

from product.models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
>>>>>>> 1e4bc09f8054df132a7460d0f0fd37450506453a
    active = factory.Iterator([True, False])

    class Meta:
        model = Category

<<<<<<< HEAD
class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker('pyint')
    category = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker('pystr')
=======

class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pyint")
    category = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker("pystr")
>>>>>>> 1e4bc09f8054df132a7460d0f0fd37450506453a

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
<<<<<<< HEAD
        
=======

>>>>>>> 1e4bc09f8054df132a7460d0f0fd37450506453a
        if extracted:
            for category in extracted:
                self.category.add(category)

    class Meta:
        model = Product