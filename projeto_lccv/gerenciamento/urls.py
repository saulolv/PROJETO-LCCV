from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
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

schema_view = get_schema_view(
    openapi.Info(
        title="Documentação API",
        default_version='v1',
        description="Documentação da API para a prova do LCCV",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@apitest.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('disciplinas/<int:id_disciplina>/alunos/<int:id_aluno>/faltas/', views.FaltaAlunoDisciplina.as_view(), name='falta_aluno_disciplina'),
    path('disciplinas/<int:id_disciplina>/frequencia/', views.FrequenciaDisciplina.as_view(), name='frequencia_disciplina'),
    path('professores/<int:id_professor>/disciplinas/', views.ProfessorDisciplina.as_view(), name='professor_disciplinas'),
    path('disciplinas/<int:id_disciplina>/alunos', views.AlunoDisciplina.as_view(), name='alunos_disciplina'),
]
