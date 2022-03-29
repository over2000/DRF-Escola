from rest_framework.test import APITestCase
from escola.models import Matricula, Aluno, Curso
from django.urls import reverse
from rest_framework import status

class MatriculaTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Matriculas-list')
        aluno = Aluno.objects.create(
            nome='Aluno Teste',
            rg='123456789',
            data_nascimento='2005-04-24',
            foto='null'
        )
        curso = Curso.objects.create(
            codigo_curso='CTT1', 
            descricao='Curso teste 1', 
            nivel='B'
        )
        self.Matricula_1 = Matricula.objects.create(
            aluno=aluno,
            curso=curso,
            periodo='M'
        )


    def test_get_matriculas(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    
    def test_post_matricula(self):
        data = {
            'periodo':'M',
            'aluno':1,
            'curso':1
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


    def test_delete_matricula(self):
        response = self.client.delete('/matriculas/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


    def test_put_matricula(self):
        data = {
            'periodo':'M',
            'aluno':1,
            'curso':1
        }
        response = self.client.put('/matriculas/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)