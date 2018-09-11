import git
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


class GitPullView(APIView):
    def get(self, request, format=None):
        if (request.META['HTTP_CHECK'] == settings.GIT_PULL_CHECK):
            front = settings.FRONTEND_DIR
            repo = git.Repo(front)
            pull = repo.git.pull()
            return Response(pull)
        return Response('Not allowed')
