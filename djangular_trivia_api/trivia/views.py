from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer


# ReadOnlyModelViewSet: only read-only GET requests for data
class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
