<template>
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
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  methods: {
    signout(e) {
      e.preventDefault();
      // axios
      //   .post("/api/v1/token/logout") // for logout >>>>> /api/v1/token/logout/
      //   .then((response) => {
      //     console.log("response", response);
      this.$store.commit("setToken", "");
      this.$store.commit("removeToken");
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.setItem("token", "");
      this.$router.push("/log-in");
      // })
      // .catch((error) => {
      //   console.log(error);
      // });
    },
  },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
