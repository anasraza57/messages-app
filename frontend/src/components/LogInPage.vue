<template>
  <div class="loginContainer">
    <div class="row justify-content-center">
      <div class="col-lg-4 col-md-6 col-sm-6">
        <div class="card shadow">
          <div class="card-title text-center border-bottom">
            <h2 class="p-3">Login</h2>
          </div>
          <div class="card-body">
            <form @submit.prevent="onSubmit">
              <div class="mb-4">
                <label for="username" class="form-label">User Name</label>
                <input
                  class="form-control"
                  type="text"
                  name="form.username"
                  placeholder="Username"
                  v-model.trim="form.username"
                />
                <small
                  class="error"
                  v-for="(error, index) of v$.form.username.$errors"
                  :key="index"
                >
                  {{ capitalizeFirstLetter(error.$property) }}
                  {{ error.$message }}
                </small>
              </div>
              <div class="mb-4">
                <label for="password" class="form-label">Password</label>
                <input
                  class="form-control"
                  type="password"
                  name="form.password"
                  placeholder="Password"
                  v-model.trim="form.password"
                />
                <small
                  class="error"
                  v-for="(error, index) of v$.form.password.$errors"
                  :key="index"
                >
                  {{ capitalizeFirstLetter(error.$property) }}
                  {{ error.$message }}
                </small>
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
import useVuelidate from "@vuelidate/core";
import { required, minLength } from "@vuelidate/validators";

export default {
  name: "LogInPage",

  data: () => ({
    form: {
      password: "",
      username: ""
    },
  }),

  setup: () => ({ v$: useVuelidate() }),

  validations() {
    return {
      form: {
        username: { required },
        password: { required, min: minLength(8) },
      },
    };
  },

  mounted() {
    if (this.$store.getters["isAuthenticated"]) this.$router.push("/");
  },

  methods: {
    onSubmit() {
      this.v$.form.$touch();
      if (this.v$.form.$error) return;
      axios
        .post("/auth/login/", this.form)
        .then((response) => {
          const token = response.data.auth_token;
          this.$store.commit("setToken", token);
          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          this.$router.push("/");
          this.$toast.success("Logged In Successfully", {
            position: "top-right",
            max: 3,
          });
        })
        .catch((error) => {
          this.$toast.success(error.message, {
            position: "top-right",
            max: 3,
          });
        });
    },

    capitalizeFirstLetter(words) {
      var separateWord = words.toLowerCase().split("_");
      for (var i = 0; i < separateWord.length; i++) {
        separateWord[i] =
          separateWord[i].charAt(0).toUpperCase() +
          separateWord[i].substring(1);
      }
      return separateWord.join(" ");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped src="../assets/css/sign.css"></style>
