from django.contrib import admin
from django.urls import path,include
from autenticacao.views import UserViewSet
from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="ESCOLA API",
      default_version='v1',
      description="API para gerenciamento de Alunos, Cursos e Matriculas",
      terms_of_service="#",
      contact=openapi.Contact(email="danielvitorcg@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'alunos', AlunosViewSet, basename='Alunos')
router.register(r'cursos', CursosViewSet, basename='Cursos')
router.register(r'matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
   path('', include(router.urls) ),
   path('admin/', admin.site.urls),
   path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
   path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
