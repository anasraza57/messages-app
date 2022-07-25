from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response

from chats.models import Chat, Message
from chats.serializers import (ChatSerializer, MessageSerializer, GetChatSerializer, ChatMessagesSerializer,
                               RetrieveChatSerializer)


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        owner = request.user.id
        data['owner'] = owner
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "invalid data"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Chat is deleted!"}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.queryset.filter(Q(owner=user) | Q(receiver=user))
        serializer_data = GetChatSerializer(queryset, many=True)
        return Response(serializer_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RetrieveChatSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        sender = request.user.id
        data['sender'] = sender
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "invalid data"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Message is deleted!"}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        query_params = request.query_params
        chat_id = query_params.get('chat_id')
        if not chat_id:
            return Response({'message': 'invalid chat id'}, status=status.HTTP_400_BAD_REQUEST)
        queryset = self.queryset.filter(chat_id=chat_id)
        serializer = ChatMessagesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
