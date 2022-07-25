<template>
  <div class="usersList">
    <a
      v-for="user in users"
      data-activity="1"
      data-last="1"
      data-uid="1"
      data-username="username"
      @click="() => openChat(user.id)"
      :class="['profileContainer', activeUser.id == user.id && 'active']"
      :key="user.id"
    >
      <div class="profileHolder">
        <div class="profileName">
          {{ user.username }}
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
              <a class="dropdown-item" href="#">Delete</a>
            </div>
          </div>
        </div>
      </div>
    </a>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "UserListing",
   props: ['activeUser', 'users'],
  data() {
    return {
      // activeUser: {
      //   id: null,
      //   full_name: "",
      // },
    }
  },
  mounted() {
    console.log('wasem', this.users)
  },
  methods: {
    openChat(id) {
      // axios
      //   .get(`/api/chat/${id}/`)
      //   .then((response) => {
      //     this.messages = response.chat_messages;
      //     this.activeUser.full_name = response.receiver_name;
          this.$emit('updateActiveUser', id);
          // console.log(this.$refs.userlisting)
        
        // })
        // .catch((error) => {
        //   this.$toast.success(error.message, {
        //     position: "top-right",
        //     max: 3,
        //   });
        // });
    },
  }
};
</script>


<style scoped src="@/assets/css/messengerApp.css"></style>