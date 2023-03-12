from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'alunos', views.AlunoViewSet, basename='alunos')
router.register(r'professores', views.ProfessorViewSet, basename='professores')
router.register(r'disciplinas', views.DisciplinaViewSet, basename='disciplinas')
router.register(r'frequencia', views.FrequenciaViewSet, basename='frequencia')
router.register(r'frequencia_aluno', views.FrequenciaAlunoViewSet, basename='frquencia_aluno')
router.register(r'disciplinas_aluno', views.DisciplinaAlunoViewSet, basename='disciplinas_aluno')
router.register(r'plano-aula', views.PlanoAulaViewSet, basename='plano-aula')
router.register(r'atividades', views.AtividadeViewSet, basename='atividades')
router.register(r'atividades_aluno', views.AtividadeAlunoViewSet, basename='atividades_aluno')

urlpatterns = [
    path('', include(router.urls)),
    path('disciplinas/<int:id_disciplina>/alunos/<int:id_aluno>/faltas/', views.FaltaAlunoDisciplina.as_view(), name='falta_aluno_disciplina'),
    path('disciplinas/<int:id_disciplina>/frequencia/', views.FrequenciaDisciplina.as_view(), name='frequencia_disciplina'),
    path('professores/<int:id_professor>/disciplinas/', views.ProfessorDisciplina.as_view(), name='professor_disciplinas'),
    path('disciplinas/<int:id_disciplina>/alunos', views.AlunoDisciplina.as_view(), name='alunos_disciplina'),

]
