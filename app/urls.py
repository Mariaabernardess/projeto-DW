from rest_framework.routers import DefaultRouter
from .views import EstudanteViewSet, CursoViewSet, MatriculaViewSet

router = DefaultRouter()
router.register('estudantes', EstudanteViewSet)
router.register('cursos', CursoViewSet)
router.register('matriculas', MatriculaViewSet)

urlpatterns = router.urls