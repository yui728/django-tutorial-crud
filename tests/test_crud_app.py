from django.test import TestCase

class CrudAppTest(TestCase):

    fixtures =["crud_testdata.json"] 

    def test_index_01(self):
        response = self.client.get('/crud/')
        # print("\nresponse:\n{}".format(response))
        self.assertTemplateUsed(response, 'crud/index.html')
        # self.assertContains(response, "index")
        print("\nresponse:\n{}".format(response.content))
        self.assertContains(response, r"<thead><tr><th>message</th><th>created_at</th><th>updated_at</th></tr></thead>", html=True)
        self.assertContains(response, r"<tr><td>Test Message01</td><td>2019年7月19日0:00</td><td>2019年7月19日0:05</td></tr>", html=True)
        self.assertContains(response, r"<tr><td>Test Message02</td><td>2019年7月19日1:00</td><td>2019年7月19日1:05</td></tr>", html=True)

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