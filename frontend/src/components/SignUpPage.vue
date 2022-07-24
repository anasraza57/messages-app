<template>
  <div class="loginContainer">
    <div class="row justify-content-center">
      <div class="col-lg-4 col-md-6 col-sm-6">
        <div class="card shadow">
          <div class="card-title text-center border-bottom">
            <h2 class="p-3">Sign Up</h2>
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
                  Sign Up
                </button>
              </div>
              <p class="mt-2 text-secondary">
                Already have an account? then
                <router-link to="/log-in" class="text-secondary">
                  Login
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
  name: "SignUpPage",
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
        .post("/api/v1/users/", formData)
        .then((response) => {
          this.$router.push("/log-in");
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped src="../assets/css/sign.css"></style>
