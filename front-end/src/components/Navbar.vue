<script setup>
import { ref, onMounted } from 'vue';
    
    
let showMobileMenu= ref(false);

function showMenu() {
    showMobileMenu.value = !showMobileMenu.value;
}
    
</script>

<template>
    <div id="navbar">
        <div class="nav-menu">
            <div class="hamburger" @click="showMenu" >
                <font-awesome-icon icon="fa-bars" />
            </div> 
            <div class="nav-content" :class="{ 'open-menu': showMobileMenu, 'close-menu': !showMobileMenu }"> 
            <div class="logo">
                <router-link to="/">Home</router-link>
            </div> 
                <ul class="nav-items">
                    <li>
                        <router-link to="/register">Register</router-link>
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
#navbar {
    background-color: #ffdfa8;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 30px;
}

.nav-menu {
    background-color: #767676;
    
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
#navbar {
    padding-top: 10px;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
}

.nav-menu {
    background-color: #ffdfa8;
}
.open-menu {
    opacity: 1;
    height: 150px;
}
.close-menu {
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

.hamburger {
    display: block;
    text-align: right;
    padding: 0 10px 10px 0;
}

}
</style>

