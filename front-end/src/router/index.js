// router/index.js
import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import MultipleChoiceQuiz from "../views/MultipleChoiceQuiz.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import BlankQuiz from "../views/BlankQuiz.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/multiple-choice",
        name: "MultipleChoiceQuiz",
        component: MultipleChoiceQuiz,
    },
    {
        path: "/login",
        name: "Login",
        component: Login,
    },
    {
        path: "/register",
        name: "Register",
        component: Register,
    },
    {
        path: "/blankquiz",
        name: "BlankQuiz",
        component: BlankQuiz,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});
  
export default router;