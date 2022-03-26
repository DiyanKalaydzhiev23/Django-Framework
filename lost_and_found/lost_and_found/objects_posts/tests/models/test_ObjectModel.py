from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.objects_posts.models import Object


class ObjectModelTests(TestCase):
    def test_object_model_create__with_valid_data__expect_success(self):
        object_instance = Object(
            name="Laptop",
            image="https://laptop.bg/microsoft_surface_laptop_go_1ZO00024.jpg",
            width=55,
            height=55,
            weight=3.5,
        )

        object_instance.full_clean()
        object_instance.save()

        self.assertIsNotNone(object_instance.pk)

    def test_object_model_create__with_first_name_max_length_more_then_10__expect_fail(self):
        object_instance = Object(
            name="EMAG 3050ti unwrapped",
            image="https://laptop.bg/microsoft_surface_laptop_go_1ZO00024.jpg",
            width=55,
            height=55,
            weight=3.5,
        )

        with self.assertRaises(ValidationError) as context:
            object_instance.full_clean()
            object_instance.save()

        self.assertIsNotNone(context.exception)
