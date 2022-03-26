from django.core.exceptions import ValidationError
from django.test import TestCase
from lost_and_found.objects_posts.models import Post, Object


class PostModelTests(TestCase):
    def setUp(self):
        self.OBJECT = Object(
            name="Laptop",
            image="https://laptop.bg/microsoft_surface_laptop_go_1ZO00024.jpg",
            width=55,
            height=55,
            weight=3.5,
        )
        self.OBJECT.save()

        self.POST = Post(
            title="Phone",
            description="Samsung",
            author_name="Ivan",
            author_phone="0885555134",
            object=self.OBJECT,
        )

    def test_post_model__with_valid_data__expect_success(self):
        post = self.POST
        post.full_clean()
        post.save()

        self.assertIsNotNone(post.pk)

    def test_post_model__with_invalid_title__expect_fail(self):
        post = self.POST

        post.title = "Laptop emag 3050ti unwrapped with ryzen 5"

        with self.assertRaises(ValidationError) as context:
            post.full_clean()
            post.save()

        self.assertIsNotNone(context.exception)

    def test_post_model__with_invalid_author_name__expect_fail(self):
        post = self.POST

        post.author_name = "Ivan Ivanov Petrov Vasilev"

        with self.assertRaises(ValidationError) as context:
            post.full_clean()
            post.save()

        self.assertIsNotNone(context.exception)

    def test_post_model__with_invalid_author_phone__expect_fail(self):
        post = self.POST

        post.author_phone = "0894876428452635465237654762"

        with self.assertRaises(ValidationError) as context:
            post.full_clean()
            post.save()

        self.assertIsNotNone(context.exception)

    def test_post_model__found_field_default_w__with_false__expect_success(self):
        post = self.POST
        post.full_clean()
        post.save()

        self.assertFalse(post.found)
