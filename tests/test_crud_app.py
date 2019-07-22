from django.test import TestCase

class CrudAppTest(TestCase):

    fixtures =["crud_testdata.json"] 

    def test_index_01(self):
        response = self.client.get('/crud/')
        # print("\nresponse:\n{}".format(response))
        self.assertTemplateUsed(response, 'crud/index.html')
        # self.assertContains(response, "index")
        # print("\nresponse:\n{}".format(response.content))
        self.assertContains(response, r'<thead><tr><th>message</th><th>created_at</th><th>updated_at</th><th>  </th></tr></thead>', html=True)
        self.assertContains(response, r'<tr><td>Test Message01</td><td>2019年7月19日0:00</td><td>2019年7月19日0:05</td><td><a href="/crud/edit/1">更新画面へ</a></td></tr>', html=True)
        self.assertContains(response, r'<tr><td>Test Message02</td><td>2019年7月19日1:00</td><td>2019年7月19日1:05</td><td><a href="/crud/edit/2">更新画面へ</a></td></tr>', html=True)
        self.assertContains(response, r'<a href="/crud/add/">登録画面へ</a>', html=True)

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
        print("\nresponse:\n{}".format(response.content))
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

    def test_delete_01(self):
        response = self.client.get('/crud/delete/')
        # print("\nresponse:\n{}".format(response))
        self.assertContains(response, 'Delete')