from django.urls import reverse
from lost_and_found.objects_posts.tests.views.utils import SetUpMixin


class IndexViewTests(SetUpMixin):
    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('index'))

        self.assertTemplateUsed(response, 'index.html')

    def test_get__when_one_post_expect_context_to_contain_one_post(self):
        response = self.client.get(reverse('index'))

        posts = response.context['posts']

        self.assertEqual(len(posts), 1)
