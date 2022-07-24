<template>
  <div class="wrapper">
    <div class="search">
      <!--      <fa class="magnifying-glass"></fa>-->
      <input
        type="text"
        name="search"
        id="search"
        placeholder="Search users..."
      />
    </div>
    <div class="header">
      <ul class="nav-left">
        <li>
          <button type="button"><i class="fa fa-bars"></i></button>
        </li>
      </ul>
      <header>
        <h1><a href="#">inbox</a></h1>
      </header>
      <div class="nav-right">
        <a href="javascript:;"
          ><img src="https://via.placeholder.com/80" alt="profile pic"
        /></a>
      </div>
    </div>
    <div class="usersList">
      <a
        v-for="user in users"
        class="profileContainer"
        data-activity="1"
        data-last="1"
        data-uid="1"
        data-username="username"
        @click="() => openChat(user.id)"
        :key="user.id"
      >
        <div class="profileAvatar">
          <img src="https://via.placeholder.com/80" alt="Username" />
        </div>
        <div class="profileHolder">
          <div class="profileName">{{ user.userName }}</div>
          <div class="profileLastMsg">{{ user.lastMessage }}</div>
        </div>
        <div class="profileOptions">
          <!--          <div class="lastDate">14/2</div>-->
          <div class="settingsGear"><i class="fa fa-gear"></i></div>
        </div>
      </a>
    </div>
    <div class="conversation">
      <div class="conversationContainer">
        <span class="w-100" v-for="message in messages" :key="message.id">
          <span
            :class="[
              'badge mb-1 py-2 pr-2',
              `text-bg-${message.color}`,
              message.class,
            ]"
            clas
          >
            {{ message.text }}
            <span class="messageTime">{{ message.time }}</span></span
          >
        </span>
      </div>
      <div class="sendMessageContainer">
        <div class="sendContentContainer">
          <textarea
            id="sendContent"
            placeholder="Message content..."
            rows="1"
          ></textarea>
        </div>
        <div class="sendButtonContainer">
          <button type="button" id="sendButton">
            <fa icon="paper-plane"></fa>
          </button>
        </div>
      </div>
    </div>
    <div class="usersProfile"></div>
  </div>
</template>

<script>
export default {
  name: "MessengerApp",
  data() {
    return {
      users: [
        {
          id: 1,
          userName: "Hassaan",
          image: "https://via.placeholder.com/80",
          lastMessage: "Hassaan*",
        },
        {
          id: 2,
          userName: "Anas",
          image: "https://via.placeholder.com/80",
          lastMessage: "Anas*",
        },
      ],
      messages: [
        {
          class: "firstPerson",
          text: "Hi",
          id: 1,
          user: 1,
          time: "12:00AM",
          color: "success",
        },
        {
          class: "firstPerson",
          text: "Hi",
          id: 2,
          user: 1,
          time: "12:00AM",
          color: "success",
        },
        {
          class: "secondPerson",
          text: "Hi",
          id: 3,
          user: 2,
          time: "12:00AM",
          color: "primary",
        },
        {
          class: "firstPerson",
          text: "How are you doing?",
          id: 4,
          user: 1,
          time: "12:00AM",
          color: "success",
        },
        {
          class: "secondPerson",
          text: "I am fine What about you?",
          id: 5,
          user: 2,
          time: "12:00AM",
          color: "primary",
        },
        {
          class: "firstPerson",
          text: "I am fine thank you",
          id: 6,
          user: 1,
          time: "12:00AM",
          color: "success",
        },
        {
          class: "secondPerson",
          text: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
          id: 7,
          user: 2,
          time: "12:00AM",
          color: "primary",
        },
        {
          class: "firstPerson",
          text: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
          id: 8,
          user: 1,
          time: "12:00AM",
          color: "success",
        },
        {
          class: "secondPerson",
          text: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
          id: 9,
          user: 2,
          time: "12:00AM",
          color: "primary",
        },
      ],
    };
  },
  mounted() {
    if (!this.$store.getters["isAuthenticated"]) this.$router.push("/log-in");
  },
  methods: {
    openChat(id) {
      console.log("openChat", id);
    },
  },
};
</script>

<style scoped src="../assets/css/messengerApp.css"></style>
