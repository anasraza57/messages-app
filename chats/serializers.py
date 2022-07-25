from django.db.models import Q
from rest_framework import serializers

from chats.models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = '__all__'

    def create(self, validated_data):
        owner = validated_data.get('owner')
        receiver = validated_data.get('receiver')
        existing_chat = Chat.objects.filter(
                Q(owner=owner, receiver=receiver) |
                Q(owner=receiver, receiver=owner)
        ).first()
        if existing_chat:
            return existing_chat
        return Chat.objects.create(**validated_data)


class GetChatSerializer(serializers.ModelSerializer):
    receiver_name = serializers.ReadOnlyField()

    class Meta:
        model = Chat
        fields = ['id', 'created_at', 'receiver_name']


class ChatMessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'created_at', 'message']


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        return Message.objects.create(**validated_data)


class RetrieveChatSerializer(serializers.ModelSerializer):
    receiver_name = serializers.ReadOnlyField()
    chat_messages = ChatMessagesSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'created_at', 'receiver_name', 'chat_messages']


