import os, git

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ControlView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, fromat=None):
        front = settings.FRONTEND_DIR
        repo = git.Repo(front)
        print(repo.description)
        # g = git.cmd.Git(front)
        return Response()
