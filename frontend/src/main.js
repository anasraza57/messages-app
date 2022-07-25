import Vue, { createApp } from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import axios from "axios";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import Toaster from "@meforma/vue-toaster";
import SimpleTypeahead from 'vue3-simple-typeahead';
import 'vue3-simple-typeahead/dist/vue3-simple-typeahead.css'; 


axios.defaults.baseURL = "http://127.0.0.1:8000";

createApp(App)
.use(Toaster)
.use(SimpleTypeahead)
.use(store)
.use(router, axios)
.mount("#app");
