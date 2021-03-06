from django.test import TestCase
from charme.core.models import PostsBlog, Author, PostCategories


class BlogTest(TestCase):
    reset_sequence = True

    def setUp(self):
        self.author = Author(name="Luiz Felipe", email="lf.divino@gmail.com")
        self.author.save()
        self.category = PostCategories(name="Moda")
        self.category.save()
        self.post = PostsBlog(
            title="Primeiro Post no site",
            body="Este é o primeiro post que eu faço no site Charme Todo Dia!",
            author=self.author,
        )
        self.post.save()

    def test_author_created(self):
        self.assertEqual(self.author.id, 1)

    def test_created_post(self):
        self.assertEqual(self.post.id, 1)
