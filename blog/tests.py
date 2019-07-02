# from django.test import TestCase, Client
# # from bs4 import BeautifulSoup
# from django.contrib.auth.models import User
# from .models import Post
#
# def create_post(title, content, author):
#     post_right = Post.objects.create(
#         title=title,
#         content=content,
#         author=author
#     )
#     return post_right
#
# class TestModel(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.author_000 = User.objects.create(username='daniel', password = 'nopassword')
#
#     def test_post(self):
#         post_000 = create_post(
#             title='The first post',
#             content='Hello, this is first post',
#             author=self.author_000,
#         )
#
