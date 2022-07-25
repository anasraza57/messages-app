<template>
  <div class="loginContainer">
    <div class="d-flex align-items-center justify-content-center">
      <div class="m-3 signup-box">
        <div class="card shadow">
          <div class="card-title text-center border-bottom">
            <h2 class="p-3">Sign Up</h2>
          </div>
          <div class="card-body">
            <form @submit.prevent="onSubmit">
              <div class="mb-4">
                <label for="first_name" class="form-label">First Name</label>
                <input
                  class="form-control"
                  type="text"
                  name="form.first_name"
                  placeholder="First Name"
                  v-model.trim="form.first_name"
                />
                <small
                  class="error"
                  v-for="(error, index) of v$.form.first_name.$errors"
                  :key="index"
                >
                  {{ capitalizeFirstLetter(error.$property) }}
                  {{ error.$message }}
                </small>
              </div>
              <div class="mb-4">
                <label for="last_name" class="form-label">Last Name</label>
                <input
                  class="form-control"
                  type="text"
                  name="form.last_name"
                  placeholder="Last name"
                  v-model.trim="form.last_name"
                />
                <small
                  class="error"
                  v-for="(error, index) of v$.form.last_name.$errors"
                  :key="index"
                >
                  {{ capitalizeFirstLetter(error.$property) }}
                  {{ error.$message }}
                </small>
              </div>
              <div class="mb-4">
                <label for="username" class="form-label">Username</label>
                <input
                  class="form-control"
                  type="text"
                  name="form.username"
                  placeholder="username"
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
              <div class="mb-4">
                <label for="confirm_password" class="form-label"
                  >Confirm Password</label
                >
                <input
                  class="form-control"
                  type="password"
                  name="form.confirm_password"
                  placeholder="Confirm Password"
                  v-model.trim="form.confirm_password"
                />
                <small
                  class="error"
                  v-for="(error, index) of v$.form.confirm_password.$errors"
                  :key="index"
                >
                  {{ capitalizeFirstLetter(error.$property) }}
                  {{ error.$message }} <br />
                </small>
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
import useVuelidate from "@vuelidate/core";
import { required, minLength, sameAs } from "@vuelidate/validators";

export default {
  name: "SignUpPage",

  data: () => ({
    form: {
      first_name: "",
      last_name: "",
      username: "",
      password: "",
      confirm_password: "",
    },
  }),

  setup: () => ({ v$: useVuelidate() }),

  validations() {
    return {
      form: {
        last_name: { required },
        first_name: { required },
        username: { required },
        password: { required, min: minLength(8) },
        confirm_password: {
          required,
          sameAsPassword: sameAs(this.form.password),
        },
      },
    };
  },

  mounted() {
    if (this.$store.getters["isAuthenticated"]) this.$router.push("/");
  },

  methods: {
    onSubmit: function () {
      this.v$.form.$touch();
      if (this.v$.form.$error) return;
      axios
        .post("/auth/register/", this.form)
        .then((response) => {
          this.$router.push("/log-in");
          this.$toast.success("User Created Successfully", {
            position: "top-right",
            max: 3,
          });
        })
        .catch((error) => {
          this.$toast.error(error.message, {
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

<style scoped src="../assets/css/sign.css"></style>
