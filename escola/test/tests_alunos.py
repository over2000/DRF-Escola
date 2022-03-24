from rest_framework.test import APITestCase
from escola.models import Aluno
from django.urls import reverse
from rest_framework import status

class AlunoTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Alunos-list')
        self.Aluno_1 = Aluno.objects.create(
            nome='Aluno Teste',
            rg='123456789',
            data_nascimento='2005-04-24',
            foto='null'
        )
        
    def test_get_alunos(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_aluno(self):
        data = {
            'nome':'Aluno Teste GET',
            'rg':'123456789',
            'cpf':'06612060174',
            'data_nascimento':'2005-04-24',
            'foto':''
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete_aluno(self):
        response = self.client.delete('/alunos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_aluno(self):
        data = {
            'nome':'Aluno Teste GET',
            'rg':'123456789',
            'cpf':'06612060174',
            'data_nascimento':'2005-04-24',
            'foto':''
        }
        response = self.client.put('/alunos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)