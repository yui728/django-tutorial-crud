from django.test import TestCase
from django.urls import reverse
from with_asserts.mixin import AssertHTMLMixin

class CrudAppTest(TestCase, AssertHTMLMixin):

    fixtures =["crud_testdata.json"] 

    def test_index_01(self):
        response = self.client.get('/crud/')
        # print("\nresponse:\n{}".format(response))
        self.assertTemplateUsed(response, 'crud/index.html')
        # self.assertContains(response, "index")
        # print("\nresponse:\n{}".format(response.content))
        self.assertContains(response, r'<thead><tr><th>message</th><th>created_at</th><th>updated_at</th><th>  </th></tr></thead>', html=True)
        self.assertContains(response, r'<tr><td><input type="checkbox" name="delete_ids" value="1" /></td><td>Test Message01</td><td>2019年7月19日0:00</td><td>2019年7月19日0:05</td><td><a href="/crud/edit/1">更新画面へ</a></td></tr>', html=True)
        self.assertContains(response, r'<tr><td><input type="checkbox" name="delete_ids" value="2" /></td><td>Test Message02</td><td>2019年7月19日1:00</td><td>2019年7月19日1:05</td><td><a href="/crud/edit/2">更新画面へ</a></td></tr>', html=True)
        self.assertContains(response, r'<a href="/crud/add/">登録画面へ</a>', html=True)
        # delete_url = reverse('crud:delete')ß
        self.assertHTML(response, 'form[method="POST", action="/crud/delete/"]')
        self.assertHTML(response, 'input[type="submit", value="削除"]')

    def test_add_01(self):
        response = self.client.get('/crud/add/')
        # print("\nresponse:\n{}".format(response.content))
        self.assertTemplateUsed(response, 'crud/edit.html')
        # self.assertContains(response, "edit")
        self.assertContains(response, r'<a href="/crud/">一覧画面へ</a>')
        self.assertContains(response, r'<label>メッセージ<input type="text" name="message" maxlength="255" required id="id_message"></label>')
        self.assertFormError(response, 'form', 'message', None)

    def test_add_02(self):
        response = self.client.post('/crud/add/', {"message": "Test Message03"})
        self.assertRedirects(response, '/crud/')
        response2 = self.client.get('/crud/')
        self.assertContains(response2, r"<td>Test Message01</td>", html=True)

    def test_add_03(self):
        response = self.client.post('/crud/add/', {"message": ""})
        # print("\nresponse:\n{}".format(response.content))
        self.assertTemplateUsed(response, 'crud/edit.html')
        self.assertContains(response, r'<a href="/crud/">一覧画面へ</a>')
        self.assertContains(response, r'<label>メッセージ<input type="text" name="message" maxlength="255" required id="id_message"></label>')
        self.assertFormError(response, 'form', 'message', "このフィールドは必須です。")

    def test_edit_01(self):
        response = self.client.get('/crud/edit/1')
        # print("\nresponse:\n{}".format(response))
        self.assertTemplateUsed(response, 'crud/edit.html')
        self.assertContains(response, r'<label>メッセージ<input type="text" name="message" maxlength="255" required id="id_message" value="Test Message01"></label>', html=True)
        # self.assertContains(response, "edit")

    def test_edit_02(self):
        response = self.client.get('/crud/edit/99')
        # print("\nresponse:\n{}".format(response))
        self.assertEquals(response.status_code, 404)

    def test_edit_03(self):
        response = self.client.post('/crud/edit/1', {"message": "Test Message01-1"})
        # print("\nresponse:\n{}".format(response))
        self.assertRedirects(response, reverse('crud:index'))

        response2 = self.client.get('/crud/')
        self.assertContains(response2, r'<td>Test Message01-1</td>', html=True)
        self.assertNotContains(response2, r'<tr><td>Test Message01</td><td>2019年7月19日0:00</td><td>2019年7月19日0:05</td><td><a href="/crud/edit/1">更新画面へ</a></td></tr>', html=True)

    def test_delete_01(self):
        response = self.client.post('/crud/delete/', {"delete_ids": [1, 2]})
        self.assertRedirects(response, '/crud/')
        # print("\nresponse:\n{}".format(response))
        # self.assertContains(response, 'Delete')

    def test_delete_02(self):
        response = self.client.get('/crud/delete/', {"delete_ids": [1, 2]})
        print('¥nresponse¥n{}'.format(response))
        self.assertEqual(response.status_code, 405)