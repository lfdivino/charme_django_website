from django.test import TestCase


class BlogTest(TestCase):

    def setUp(self):
        self.author = Author(name="Luiz Felipe", email="lf.divino@gmail.com")
        self.author.save()
        self.post = Post(
            title="Primeiro Post no site",
            body="Este é o primeiro post que eu faço no site Charme Todo Dia!",
            author=self.author
        )
        self.post.save()

   # def test_post_index(self):