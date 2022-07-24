import { createRouter, createWebHistory } from "vue-router";
import SignUp from "@/views/SignUp";
import LogIn from "@/views/LogIn";
import MessengerApp from "@/views/MessengerApp";

const routes = [
  {
    path: "/",
    name: "MessengerApp",
    component: MessengerApp,
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: SignUp,
  },
  {
    path: "/log-in",
    name: "LogIn",
    component: LogIn,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
