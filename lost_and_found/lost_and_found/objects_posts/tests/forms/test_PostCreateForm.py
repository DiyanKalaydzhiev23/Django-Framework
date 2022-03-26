from django.test import TestCase
from lost_and_found.objects_posts.forms import PostCreateForm, ObjectForm


class PostCreateFormTests(TestCase):
    DATA = {
        'title': 'Laptop',
        'description': 'Some Description',
        'author_name': 'Ivan',
        'author_phone': '088836454',
        'object_title': 'Laptop',
        'image': 'http://www.diankalaydzhiev.ml',
        'width': 35,
        'height': 44,
        'weight': 10,
    }

    def test_post_create_form_and_object_create_form_save__when_valid(self):
        form = PostCreateForm(self.DATA)
        self.assertTrue(form.is_valid())

    def test_post_create_form_save_when_invalid(self):
        self.DATA['title'] = "Emag Laptop unwrapped 3050ti ryzen 5 1390lv"

        form = PostCreateForm(self.DATA)
        self.assertFalse(form.is_valid())
