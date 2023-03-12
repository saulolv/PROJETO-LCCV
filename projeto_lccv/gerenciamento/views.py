from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from .models import Alunos, Professores, Disciplinas, Frequencia, FrequenciaAluno, DisciplinaAluno, PlanoAula, Atividades, AtividadeAluno
from .serializers import AlunoSerializer, ProfessorSerializer, DisciplinaSerializer, FrequenciaSerializer, FrequenciaAlunoSerializer, DisciplinaAlunoSerializer, PlanoAulaSerializer, AtividadesSerializer, AtividadeAlunoSerializer 


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professores.objects.all()
    serializer_class = ProfessorSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplinaSerializer
    
    def get_queryset(self):
        id_professor = self.kwargs['professores_pk']
        queryset = Disciplinas.objects.filter(id_professor=id_professor)
        return queryset
     

class FrequenciaViewSet(viewsets.ModelViewSet):
    serializer_class = FrequenciaSerializer
    
    def get_queryset(self):
        id_disciplina = self.kwargs['disciplina_pk']
        queryset = Frequencia.objects.filter(id_disciplina=id_disciplina)
        return queryset
    
class FrequenciaAlunoViewSet(viewsets.ModelViewSet):
    serializer_class = FrequenciaAlunoSerializer
    
    def get_queryset(self):
        id_aluno = self.kwargs['alunos_pk']
        id_frequencia = self.kwargs['frequencia_pk']
        queryset = FrequenciaAluno.objects.filter(id_aluno=id_aluno, id_frequencia=id_frequencia)
        return queryset

class DisciplinaAlunoViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplinaAlunoSerializer
    
    def get_queryset(self):
        id_aluno = self.kwargs['alunos_pk']
        id_disciplina = self.kwargs['disciplinas_pk']
        queryset = DisciplinaAluno.objects.filter(id_aluno=id_aluno, id_disciplina=id_disciplina)
        return queryset

class PlanoAulaViewSet(viewsets.ModelViewSet):
    serializer_class = PlanoAulaSerializer
    
    def get_queryset(self):
        id_disciplina = self.kwargs['disciplinas_pk']
        queryset = PlanoAula.objects.filter(id_disciplina=id_disciplina)
        return queryset

class AtividadeViewSet(viewsets.ModelViewSet):
    serializer_class = AtividadesSerializer
    
    def get_queryset(self):
        id_plano_aula = self.kwargs['planoaula_pk']
        id_disciplina = self.kwargs['disciplinas_pk']
        queryset = Atividades.objects.filter(id_plano_aula=id_plano_aula, id_disciplina=id_disciplina)
        return queryset

class AtividadeAlunoViewSet(viewsets.ModelViewSet):
    serializer_class = AtividadesSerializer
    
    def get_queryset(self):
        id_atividade = self.kwargs['atividades_pk']
        id_aluno = self.kwargs['alunos_pk']
        queryset = AtividadeAluno.objects.filter(id_atividade=id_atividade, id_aluno=id_aluno)
        return queryset

