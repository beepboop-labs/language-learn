<script setup>
import { ref, onMounted } from 'vue';
    
    
let showMobileMenu= ref(false);

function showMenu() {
    showMobileMenu = !showMobileMenu;
}
    

</script>

<template>
    <div id="navbar">
        <div class="nav-menu">
            <div class="hamburger" @click="showMenu" >
                <font-awesome-icon icon="fa-bars" />
            </div> 
            <div class="nav-content" :class="this.showMobileMenu ? 'open-menu' : 'closed-menu'"> 
            <div class="logo">
                <router-link to="/">LOGO</router-link>
            </div> 
                <ul class="nav-items">
                    <li>
                        <router-link to="/multiple-choice">Multiple Choice Quiz</router-link>
                    </li>
                    <li>
                        <router-link to="/blankquiz">BlankQuiz</router-link>
                    </li>
                </ul>
            <div class="login-button">
                <router-link to="/login">Login</router-link>
            </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.nav-menu {
    background-color: #ffdfa8;
}
.nav-content {
    display: flex;
    justify-content: space-between;
    padding: 10px 30px;
    align-items: center;
}
.nav-items {
    display: flex;
    justify-content: center;
    align-items: center;
    list-style: none;
    margin: 0;
    padding: 0;
}

li {
    padding: 0 10px;   
}


.hamburger {
    display: none;
}

/* Mobile version - hidden hamburger menu */
@media screen and (max-width: 768px) {
.nav-menu {
    padding-top: 10px;
    position: absolute;
    width: 100%;
}
.open-menu {
    opacity: 1;
    height: 150px;
}
.closed-menu {
    opacity: 0;
    height: 0;
    padding: 0;
}
.nav-content {
    flex-direction: column;
    z-index: 100;
    position: relative;
    transition: all 0.2s ease-out;
}
.nav-items {
    flex-direction: column;
}

i {
    display: block;
    text-align: right;
    padding: 0 10px 10px 0;
}

}
</style>

