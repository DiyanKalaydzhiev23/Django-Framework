from lost_and_found.objects_posts.tests.views.utils import SetUpMixin
from django.urls import reverse


class EditViewTests(SetUpMixin):
    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('edit', kwargs={'pk': self.POST.pk}))
        self.assertTemplateUsed(response, 'post_edit.html')

    def test_get__form_in_context(self):
        response = self.client.get(reverse('edit', kwargs={'pk': self.POST.pk}))
        form = response.context['post_form']

        self.assertIsNotNone(form)
