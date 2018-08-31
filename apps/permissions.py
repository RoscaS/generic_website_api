# from rest_framework.permissions import (
#     BasePermission,
#     IsAdminUser,
#     IsAuthenticatedOrReadOnly
# )
# from jose import jwt
#
#
# def get_token_auth_header(request):
#     auth = request.META.get("HTTP_AUTHORIZATION", None)
#     try:
#         parts = auth.split()
#         token = parts[1]
#         return token
#     except:
#         return None
#
# class is_admin_or_read_only(BasePermission):
#
#     def has_permission(self, request, view):
#         token = get_token_auth_header(request)
#         if token:
#             unverified_claims = jwt.get_unverified_claims(token)
#             scope = unverified_claims.get('scope', None)
#             if 'full_access' in scope:
#                 # print(unverified_claims)
#                 # debug(unverified_claims, True)
#                 return True
#         # print(scope)
#         # print("\n\n is NOT admin")
#         return IsAuthenticatedOrReadOnly.has_permission(self, request, view)
#
#
