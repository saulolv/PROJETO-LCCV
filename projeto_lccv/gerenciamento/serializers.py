from rest_framework import serializers
from .models import Alunos, Professores, Disciplinas, Frequencia, FrequenciaAluno, DisciplinaAluno, PlanoAula, Atividades, AtividadeAluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alunos
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professores
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplinas
        fields = '__all__'
        
class FrequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequencia
        fields = '__all__'

class FrequenciaAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequenciaAluno
        fields = '__all__'

class DisciplinaAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplinaAluno
        fields = '__all__'

class PlanoAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoAula
        fields = '__all__'

class AtividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividades
        fields = '__all__'
        
class AtividadeAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtividadeAluno
        fields = '__all__'