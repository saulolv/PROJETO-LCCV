from django.db import models
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    tags=['Alunos'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'nome': openapi.Schema(type=openapi.TYPE_STRING),
            'cpf': openapi.Schema(type=openapi.TYPE_STRING),
            'rg': openapi.Schema(type=openapi.TYPE_STRING),
            'matricula': openapi.Schema(type=openapi.TYPE_STRING),
            'telefone': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
    responses={
        200: openapi.Response('Aluno criado com sucesso'),
        400: 'Erro na requisição'
    },
    manual_parameters=[
        openapi.Parameter('id_aluno', openapi.IN_PATH, description="ID do aluno", type=openapi.TYPE_INTEGER)
    ]
)
class Alunos(models.Model):
    id_aluno = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=8)
    matricula = models.CharField(max_length=8)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.nome}"
    

@swagger_auto_schema(
    tags=['Professores'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'nome': openapi.Schema(type=openapi.TYPE_STRING),
            'cpf': openapi.Schema(type=openapi.TYPE_STRING),
            'rg': openapi.Schema(type=openapi.TYPE_STRING),
            'matricula': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'telefone': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
    responses={
        200: openapi.Response('Professor criado com sucesso'),
        400: 'Erro na requisição'
    },
    manual_parameters=[
        openapi.Parameter('id_professor', openapi.IN_PATH, description="ID do professor", type=openapi.TYPE_INTEGER)
    ]
)
class Professores(models.Model):
    id_professor = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=8)
    codigo = models.CharField(max_length=8)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return f"{self.nome}"
    

class Disciplinas(models.Model):
    id_disciplina = models.IntegerField(primary_key=True)
    id_professor = models.ForeignKey(Professores, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=7)
    carga_horaria = models.IntegerField(null=True)
    ementa = models.TextField()
    
    def __str__(self):
        return f"{self.nome}"


class Frequencia(models.Model):
    id_frequencia = models.IntegerField(primary_key=True)
    id_materia = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    dia = models.DateField()
    
    def __str__(self):
        return f"Frequencia - {self.id_materia.nome}"

class FrequenciaAluno(models.Model):
    id = models.IntegerField(primary_key=True)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    id_frequencia = models.ForeignKey(Frequencia, on_delete=models.CASCADE)
    presenca = models.CharField(max_length=1, default='T')
    
    def __str__(self):
        return f"Frequencia - {self.id_frequencia.id_materia.nome} - {self.id_aluno}"

class DisciplinaAluno(models.Model):
    id_matricula = models.IntegerField(primary_key=True)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    id_disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    nota = models.FloatField()

    def __str__(self):
        return f"{self.id_disciplina.nome} - {self.id_aluno}"

class PlanoAula(models.Model):
    id_plano_aula = models.IntegerField(primary_key=True)
    id_disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    tema_aula = models.CharField(max_length=255)
    conteudo = models.TextField()
    metodo = models.CharField(max_length=50)
    dia = models.DateField()
    
    def __str__(self):
        return f"Plano de aula - {self.id_disciplina.nome}"
    

class Atividades(models.Model):
    id_atividade = models.IntegerField(primary_key=True)
    atividade = models.TextField()
    tipo = models.CharField(max_length=50)
    data_postagem = models.DateField()
    data_entrega = models.DateField()
    id_disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    id_plano_aula = models.ForeignKey(PlanoAula, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Atividades - {self.id_disciplina.nome}"
    

class AtividadeAluno(models.Model):
    id = models.IntegerField(primary_key=True)
    id_atividade = models.ForeignKey(Atividades, on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    nota = models.FloatField()
    
    def __str__(self):
        return f"Atividade  - {self.id_aluno} - {self.id_atividade.id_disciplina.nome}"

