from django.test import TestCase
from lost_and_found.objects_posts.models import Post, Object


class SetUpMixin(TestCase):
    def setUp(self):
        super().__init__()
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

        self.POST.save()
