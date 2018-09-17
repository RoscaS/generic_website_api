import git, requests, json
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GrecaptchaToken


class GitPullView(APIView):
    def get(self, request, format=None):
        if (request.META['HTTP_CHECK'] == settings.GIT_PULL_CHECK):
            front = settings.FRONTEND_DIR
            repo = git.Repo(front)
            pull = repo.git.pull()
            return Response(pull)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class Grecaptcha(APIView):
    def get(self, request):
        pass

    def post(self, request, format=None):
        if (request.data):
            secret = settings.GOOGLE_RECAPTCHA
            token = request.data['token']
            GrecaptchaToken.objects.create(token=token)
            p = requests.post(
                url='https://www.google.com/recaptcha/api/siteverify',
                data={'secret': secret, 'response': token}
            )
            print(p.content.decode())
            if json.loads(p.content.decode())['success']:
                return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

