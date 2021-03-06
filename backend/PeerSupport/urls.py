from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from allauth.account.views import ConfirmEmailView
from rest_framework.authtoken.views import obtain_auth_token
from profile.views import null_view, getUserEmail, complete_view, ProfileViewSet, PreStudyQuizViewSet, PostStudyQuizViewSet, WeekPostStudyQuizViewSet, UserQuizViewSet, CounselorQuizViewSet, ResearchQuizViewSet, get_chats, get_friends, validate_user_group
from events.views import EventViewSet
from chat.views import ChatViewSet
from message.views import MessageFlagViewSet

router = routers.DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('events', EventViewSet)
router.register('chats', ChatViewSet)
router.register('flags', MessageFlagViewSet)
router.register('events', EventViewSet)
router.register('prestudyquiz', PreStudyQuizViewSet)
router.register('poststudyquiz', PostStudyQuizViewSet)
router.register('weekpoststudyquiz', WeekPostStudyQuizViewSet)

urlpatterns = [
    path('api/api/', include(router.urls)),
    path('api/admin/', admin.site.urls),
    path('api/get-chats/', get_chats),
    path('api/get-user-email', getUserEmail),
    path('api/get-friends/', get_friends),
    path('api/validate-user-group/', validate_user_group),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/api-token-auth/', obtain_auth_token),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/rest-auth/registration/account-email-verification-sent/',
         null_view, name='account_email_verification_sent'),
    path('api/rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$',
         ConfirmEmailView.as_view(), name='account_confirm_email'),
    path('api/rest-auth/registration/complete/$',
         complete_view, name='account_confirm_complete'),
    path(
        'api/rest-auth/password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', null_view, name='password_reset_confirm'),
]
