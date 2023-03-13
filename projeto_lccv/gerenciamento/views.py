from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date


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



class FaltaAlunoDisciplina(APIView):
    def get(self, request, id_disciplina, id_aluno):
        disciplina_aluno = get_object_or_404(DisciplinaAluno, id_disciplina=id_disciplina, id_aluno=id_aluno)
        
        frequencias_aluno = FrequenciaAluno.objects.filter(id_aluno=id_aluno, id_frequencia__id_materia=id_disciplina)
        total_aulas = Frequencia.objects.filter(id_materia=id_disciplina).count()
        total_faltas = frequencias_aluno.filter(presenca='F').count()
        
        frequencia = round(((total_aulas - total_faltas) / total_aulas) * 100, 2) if total_aulas > 0 else 0
        nota = disciplina_aluno.nota
        
        aluno_info = {
        'nome': disciplina_aluno.id_aluno.matricula,
        'cpf': disciplina_aluno.id_aluno.cpf,
        'matricula': disciplina_aluno.id_aluno.matricula,
        'nota': nota,
        'frequencia': f"{frequencia}%",
        'faltas': total_faltas,
        }
        return Response(aluno_info)
        
 
class FrequenciaDisciplina(APIView):
    def post(self, request, id_disciplina):
        try:
            disciplina = Disciplinas.objects.get(id_disciplina=id_disciplina)
        except Disciplinas.DoesNotExist:
            return Response(f"Disciplina com id {id_disciplina} não encontrada", status=status.HTTP_404_NOT_FOUND)
        
        nova_frequencia = Frequencia.objects.create(id_materia=disciplina, dia=date.today())
        
        for aluno_presenca in request.data:
            try:
                aluno = Alunos.objects.get(pk=aluno_presenca['id_aluno'])
            except Alunos.DoesNotExist:
                return Response(f"Aluno com id {aluno_presenca['id_aluno']} não encontrado", status=status.HTTP_404_NOT_FOUND)
            
            FrequenciaAluno.objects.create(id_aluno=aluno, id_frequencia=nova_frequencia, presenca=aluno_presenca['presenca'])
        
        return Response(status=status.HTTP_201_CREATED)


class ProfessorDisciplina(APIView):
    def get(self, request, id_professor):
        disciplinas =   Disciplinas.objects.filter(id_professor=id_professor)
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)


class AlunoDisciplina(APIView):
    def get(self, request, id_disciplina):
        disciplina = Disciplinas.objects.get(pk=id_disciplina)
        disciplina_alunos = DisciplinaAluno.objects.filter(id_disciplina=disciplina)
        alunos = [da.id_aluno for da in disciplina_alunos]
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)