import git
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class GitPullView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, fromat=None):
        front = settings.FRONTEND_DIR
        repo = git.Repo(front)
        pull = repo.git.pull()
        return Response(pull)
