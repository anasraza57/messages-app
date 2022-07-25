<template>
  <div class="wrapper">
    <div class="autocompleteWrapper">
      <vue3-simple-typeahead
        class="autcomplete simple-typeahead"
        id="typeahead_id"
        placeholder="Start writing..."
        :items="usersList"
        :minInputLength="1"
        @selectItem="onSelect"
        @onInput="onInputEventHandler"
      />
    </div>
    <div class="header">
      <header>
        <h4>
          {{ activeUser.id ? activeUser.full_name : "Inbox" }}
        </h4>
      </header>
    </div>
    <UserListing @updateActiveUser="updateActiveUser($event)" :activeUser="activeUser" :users="users"  />
    <div class="conversation">
      <div class="conversationContainer">
        <span v-if="!activeUser.id" class="welcome"
          >Welcome To Chat Inbox!!</span
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
            clas
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
          <button type="submit" id="sendButton" :disabled="btnDisable">
            <!-- <img src="../assets/paper-plane.png" class="img-fluid" alt=""> -->
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import UserListing from './UserListing.vue';
export default {
  name: "MessengerApp",
  components: {
    UserListing
},
  data() {
    return {
      message: "",
      btnDisable: true,
      activeUser: {
        id: null,
        full_name: "",
      },
      usersList: [],
      users: [],
      messages: [],
    };
  },
  created() {
    axios
      .get("/api/chat/")
      .then((response) => {
        const usersResponse = response.data.results;
        this.users = usersResponse;
        if (usersResponse.length >= 1) {
          this.usersList = usersResponse.map((user) => user.username);
        }
      })
      .catch((error) => {
        this.$toast.success(error.message, {
          position: "top-right",
          max: 3,
        });
      });
  },
  mounted() {
    if (!this.$store.getters["isAuthenticated"]) this.$router.push("/log-in");
  },

  updated() {
    if (this.message == "" && this.activeUser.id) {
      this.btnDisable = true;
    } else {
      this.btnDisable = false;
    }
  },
  methods: {
    onSelect(item) {
      let userId = "";
      this.users.map((user) => {
        if (item == user.username) {
          userId = user.id;
          return;
        }
      });
      axios
        .post(`/api/chat/`, { receiver: userId })
        .then((response) => {
          console.log("waseem", response);
        })
        .catch((error) => {
          this.$toast.success(error.message, {
            position: "top-right",
            max: 3,
          });
        });
    },
    onSend() {
      if (this.message == "") return;
      axios
        .post(`/api/chat/`, { receiver: id, message: message, chat: "" })
        .then((response) => {
          this.message = "";
          console.log("waseem", response);
          // this.users = json.parse(response.data.users);
        })
        .catch((error) => {
          this.$toast.success(error.message, {
            position: "top-right",
            max: 3,
          });
        });
    },
    onInputEventHandler() {},
  updateActiveUser(id) {
    console.log(id)
  }
  },
};
</script>

<style scoped src="../assets/css/messengerApp.css"></style>
