import factory.fuzzy

from book.models import Book, Author, Genre


class GenreFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'title_%d' % n)
    description = factory.fuzzy.FuzzyText(length=100)

    class Meta:
        model = Genre


class AuthorFactory(factory.django.DjangoModelFactory):
    first_name = factory.Sequence(lambda n: 'first_name_%d' % n)
    last_name = factory.Sequence(lambda n: 'last_name_%d' % n)
    bio = factory.fuzzy.FuzzyText(length=100)

    class Meta:
        model = Author


class BookFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'title_%d' % n)
    description = factory.fuzzy.FuzzyText(length=100)

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for author in extracted:
                self.authors.add(author)

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for genre in extracted:
                self.genres.add(genre)

    class Meta:
        model = Book
