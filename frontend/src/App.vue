<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-light">
      <div class="container-fluid">
        <a class="navbar-brand">Messaging App</a>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <li v-if="!this.$store.getters['isAuthenticated']" class="nav-item">
              <router-link class="nav-link active" to="/sign-up"
                >Sign Up
              </router-link>
            </li>
            <li v-if="!this.$store.getters['isAuthenticated']" class="nav-item">
              <router-link class="nav-link" to="/log-in">Sign In</router-link>
            </li>
            <li v-else class="nav-item">
              <button class="btn btn-outline-danger" @click="signout">
                Sign Out
              </button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      loggedIn: false,
    };
  },
  beforeCreate() {
    this.$store.commit("initializeStore");
    const token = this.$store.state.token;
    axios.defaults.headers.post["Content-Type"] =
      "application/json;charset=utf-8";
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  methods: {
    signout(e) {
      e.preventDefault();
      axios
        .get("/auth/logout")
        .then((response) => {
          console.log("response", response);
          this.$store.commit("removeToken");
          axios.defaults.headers.common["Authorization"] = "";
          localStorage.setItem("token", "");
          this.$router.push("/log-in");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style src="./assets/css/global.css"></style>
