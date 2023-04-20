// router/index.js
import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import MultipleChoiceQuiz from "../views/MultipleChoiceQuiz.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import BlankQuiz from "../views/BlankQuiz.vue";
import TrueFalse from "../views/TrueFalse.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/multiple-choice/:secondaryLanguage/:unit",
        name: "MultipleChoiceQuiz",
        component: MultipleChoiceQuiz,
        props: true,
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
        path: "/blankquiz/:secondaryLanguage/:unit",
        name: "BlankQuiz",
        component: BlankQuiz,
        props: true,
    },
    {
        path: "/truefalse/:secondaryLanguage/:unit",
        name: "TrueFalse",
        component: TrueFalse,
        props: true,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});
  
export default router;