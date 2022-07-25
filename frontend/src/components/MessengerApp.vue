<template>
  <div class="wrapper">
    <div class="autocompleteWrapper">
      <vue3-simple-typeahead
        class="autcomplete simple-typeahead"
        id="typeahead_id"
        placeholder="Start writing..."
        :items="searchUsers.map((user) => user.full_name)"
        :minInputLength="1"
        @selectItem="onSelect"
      />
    </div>
    <div class="header">
      <header class="d-flex justify-content-between px-3">
        <h4 class="text-capitalize">
          {{ activeUser.id ? activeUser.full_name : "Inbox" }}
        </h4>
        <button class="btn btn-success" @click="openChat">Update</button>
      </header>
    </div>
    <UserListing
      @updateUserMessages="updateUserMessages($event)"
      :chatId="chatId"
      :chats="chatUsers"
      @onLoadCall="onLoadCall()"
      ref="UserListing"
    />
    <div class="conversation">
      <div class="conversationContainer">
        <span v-if="!activeUser.id" class="welcome">Welcome To Chat Inbox!!</span
        >
        <span v-else-if="this.messages.length <= 0" class="welcome"
          >No conversation Yet!!</span
        >
        <span
          v-else
          class="w-100"
          v-for="message in messages"
          :key="message.id"
        >
          <span
            :class="[
              'badge mb-1 py-2 pr-2',
              `text-bg-${message.type == 'success' ? message.type : 'primary'}`,
              message.type == 'success' ? 'firstPerson' : 'secondPerson',
            ]"
          >
            {{ message.message }}
            <span class="messageTime">{{ message.time }}</span></span
          >
        </span>
      </div>
      <form class="sendMessageContainer" @submit.prevent="onSend">
        <div class="sendContentContainer">
          <textarea
            id="sendContent"
            placeholder="Message content..."
            rows="1"
            v-model.trim="message"
          ></textarea>
        </div>
        <div class="sendButtonContainer">
          <button
            type="submit"
            id="sendButton"
            :disabled="
              message == '' ? true : activeUser.id == null ? true : false
            "
          >
          <span class="w-50 h-50">
            <svg xmlns="http://www.w3.org/2000/svg" class="send-btn" viewBox="0 0 512 512">
              <path
                d="M511.6 36.86l-64 415.1c-1.5 9.734-7.375 18.22-15.97 23.05c-4.844 2.719-10.27 4.097-15.68 4.097c-4.188 0-8.319-.8154-12.29-2.472l-122.6-51.1l-50.86 76.29C226.3 508.5 219.8 512 212.8 512C201.3 512 192 502.7 192 491.2v-96.18c0-7.115 2.372-14.03 6.742-19.64L416 96l-293.7 264.3L19.69 317.5C8.438 312.8 .8125 302.2 .0625 289.1s5.469-23.72 16.06-29.77l448-255.1c10.69-6.109 23.88-5.547 34 1.406S513.5 24.72 511.6 36.86z"
              />
            </svg>
          </span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "../mixin/Toast.js";
import UserListing from "./UserListing.vue";
export default {
  name: "MessengerApp",
  mixins: [toast],
  components: {
    UserListing,
  },
  data() {
    return {
      message: "",
      messages: [],
      chatId: "",
      activeUser: {
        id: null,
        full_name: "",
      },
      searchUsers: [],
      chatUsers: [],
    };
  },
  created() {
    this.onLoadCall();
  },
  mounted() {
    if (!this.$store.getters["isAuthenticated"]) this.$router.push("/log-in");
  },
  computed: {},
  methods: {
    onLoadCall() {
      axios
        .get("/api/chat/")
        .then((response) => {
          if (response.data && response.data.length > 0) {
            this.chatUsers = response.data;
          }
        })
        .catch((error) => {
          toast.ErrorToast(error.message);
        });
      axios
        .get("/auth/users")
        .then((response) => {
          if (response.data && response.data.length > 0) {
            this.searchUsers = response.data;
          }
        })
        .catch((error) => {
          toast.ErrorToast(error.message);
        });
    },
    onSelect(item) {
      let userId = "";
      this.searchUsers.map((user) => {
        if (item == user.full_name) {
          userId = user.id;
          return;
        }
      });
      axios
        .post(`/api/chat/`, { receiver: userId })
        .then((response) => {
          if (response.status == 201) {
            toast.SuccessToast("Chat Created Successfully");
            this.onLoadCall();
          } else {
            toast.SuccessToast("Chat Already Exist");
          }
        })
        .catch((error) => {
          toast.ErrorToast(error.message);
        });
    },
    onSend() {
      if (this.message == "") return;
      axios
        .post(`/api/messages/`, {
          receiver: this.activeUser.id,
          message: this.message,
          chat: this.chatId,
        })
        .then((response) => {
          this.message = "";
        })
        .catch((error) => {
          toast.ErrorToast(error.message);
        });
    },
    updateUserMessages(data) {
      this.messages = data.messages;
      this.chatId = data.chatId;
      this.activeUser = data.user;
    },
    openChat() {
      this.$refs.UserListing.openChat(this.chatId);
    },
  },
};
</script>

<style scoped src="../assets/css/messengerApp.css"></style>
