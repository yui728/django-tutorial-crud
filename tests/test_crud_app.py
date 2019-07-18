from django.test import TestCase

class CrudAppTest(TestCase):

    def test_index_01(self):
        response = self.client.get('/crud/')
        # print("\nresponse:\n{}".format(response))
        self.assertTemplateUsed(response, 'crud/index.html')
        self.assertContains(response, "index")

    def test_add_01(self):
        response = self.client.get('/crud/add/')
        # print("\nresponse:\n{}".format(response))
        self.assertTemplateUsed(response, 'crud/edit.html')
        self.assertContains(response, "edit")

    def test_edit_01(self):
        response = self.client.get('/crud/edit/1')
        # print("\nresponse:\n{}".format(response))
        self.assertTemplateUsed(response, 'crud/edit.html')
        self.assertContains(response, "edit")

    def test_delete_01(self):
        response = self.client.get('/crud/delete/')
        # print("\nresponse:\n{}".format(response))
        self.assertContains(response, 'Delete')