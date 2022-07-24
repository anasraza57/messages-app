<template>
  <div class="loginContainer">
    <div class="row justify-content-center">
      <div class="col-lg-4 col-md-6 col-sm-6">
        <div class="card shadow">
          <div class="card-title text-center border-bottom">
            <h2 class="p-3">Login</h2>
          </div>
          <div class="card-body">
            <form @submit.prevent="submitForm">
              <div class="mb-4">
                <label for="username" class="form-label">Username</label>
                <input
                  class="form-control"
                  type="text"
                  name="username"
                  placeholder="Username"
                  v-model="username"
                />
              </div>
              <div class="mb-4">
                <label for="password" class="form-label">Password</label>
                <input
                  class="form-control"
                  type="password"
                  name="password"
                  placeholder="Password"
                  v-model="password"
                />
              </div>
              <div class="d-grid">
                <button type="submit" class="btn text-light main-bg">
                  Login
                </button>
              </div>
              <p class="mt-2 text-secondary">
                Don't have an account? then
                <router-link to="/sign-up" class="text-secondary">
                  Sign Up
                </router-link>
              </p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LogInPage",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  mounted() {
    if (this.$store.getters["isAuthenticated"]) this.$router.push("/");
  },
  methods: {
    submitForm(e) {
      e.preventDefault();
      const formData = {
        username: this.username,
        password: this.password,
      };

      axios
        .post("/api/v1/token/login", formData) // for logout >>>>> /api/v1/token/logout/
        .then((response) => {
          console.log("response", response);
          const token = response.data.auth_token;
          this.$store.commit("setToken", token);
          axios.defaults.headers.common["Authorization"] = "Token" + token;
          localStorage.setItem("token", token);
          this.$router.push("/");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped src="../assets/css/sign.css"></style>
