from django.db import models
from db.models import BaseModel
from users.models import User

# Create your models here.


class Chat(BaseModel):
    owner = models.ForeignKey(
        User,
        related_name='owned_chats',
        help_text="User who created this conversation",
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User,
        related_name='received_chats',
        help_text="User with whom this conversation is started",
        on_delete=models.CASCADE
    )

    @property
    def receiver_name(self):
        return f"{self.receiver.first_name} {self.receiver.last_name}"

    @property
    def owner_name(self):
        return f"{self.owner.first_name} {self.owner.last_name}"


class Message(BaseModel):
    chat = models.ForeignKey(
        'Chat',
        related_name='chat_messages',
        help_text='Chat from which message belongs',
        on_delete=models.CASCADE
    )

    sender = models.ForeignKey(
        User,
        related_name='user_messages',
        help_text="Sender of this message",
        on_delete=models.PROTECT,
    )

    receiver = models.ForeignKey(
        User,
        related_name='messages',
        help_text="Receiver of this message",
        on_delete=models.CASCADE
    )

    message = models.TextField()

    def __str__(self):
        return f'{self.id} : {self.sender} sends message to {self.receiver}'
