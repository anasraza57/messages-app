<template>
  <div class="usersList">
    <a
      v-for="chat in chats"
      data-activity="1"
      data-last="1"
      data-uid="1"
      data-username="username"
      @click="() => openChat(chat.id)"
      :class="['profileContainer', chatId == chat.id && 'active']"
      :key="chat.id"
    >
      <div class="profileHolder">
        <div class="profileName">
          {{ chat.receiver_name }}
        </div>
      </div>
      <div class="profileOptions">
        <div class="lastDate">
          <div class="dropdown">
            <button
              class="btn btn-secondary dropdown-toggle"
              type="button"
              id="dropdownMenuButton"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              <img src="../assets/dots-menu.png" alt="" class="img-fluid" />
            </button>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
              <a class="dropdown-item" @click="()=>deleteChat(chat.id)" href="#">Delete</a>
            </div>
          </div>
        </div>
      </div>
    </a>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "../mixin/Toast.js";

export default {
  name: "UserListing",
  props: ["chatId", "chats"],
  data() {
    return {};
  },
  methods: {
    openChat(id) {
      axios
        .get(`/api/chat/${id}/`)
        .then((response) => {
          this.$emit("updateUserMessages", {
            messages: response.data.chat_messages,
            chatId: id,
            user: {
              full_name: response.data.receiver_name,
              id: response.data.receiver,
            },
          });
        })
        .catch((error) => {
          toast.ErrorToast(error.message);
        });
    },
    deleteChat(id) {
      axios
        .delete(`/api/chat/${id}/`)
        .then((response) => {
          this.$emit("onLoadCall");
        })
        .catch((error) => {
          toast.ErrorToast(error.message);
        });
    },
  },
};
</script>

<style scoped src="@/assets/css/messengerApp.css"></style>
