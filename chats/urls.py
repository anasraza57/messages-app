from chats.views import ChatViewSet, MessageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'chat', ChatViewSet, basename='chat')
router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = router.urls
