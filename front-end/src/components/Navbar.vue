<script setup>
import { ref, onMounted, watch} from 'vue';
import { userToken } from '../user-token';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();

let username = ref(userToken.getUsername())
// This is a built-in lifecycle hook from Vue
onMounted(() => {
   username.value = userToken.getUsername()
  });

  watch(userToken, () => {
  username.value = userToken.getUsername()
})
    
    
let showMobileMenu = ref(false);

function toggleMobileMenu() {
    console.log("clicked")
    showMobileMenu.value = !showMobileMenu.value;
}

function logout(){
  userToken.clearUser();
  router.push('/')

}
    
</script>

<template>
    <div id="navbar">
        <div class="nav-menu">
            <div class="hamburger" @click="toggleMobileMenu" >
                <font-awesome-icon icon="fa-bars" />
            </div> 
            <div class="nav-content" :class="{ 'open-menu': showMobileMenu, 'close-menu': !showMobileMenu }"> 
            <div class="logo">
                <router-link to="/">Home</router-link>
            </div> 
                <ul class="nav-items">
                    <li v-if="!username">
                        <router-link to="/register">Register</router-link>
                    </li>
                    <li>
                      <div v-if="!username" class="login-button">
                          <router-link to="/login">Login</router-link>
                      </div>
                    </li>
                    <li>
                      <div v-if="username" class="username">
                        {{ username }} / <button @click="logout">Logout</button>
                      </div>
                      
                    </li>
                </ul>
            
            <!-- <div v-if="username" class="username">
                <button class="profile-button" @click="toggleProfileMenu">{{ username }}</button>
                <div class="profile-menu" v-if="showProfileMenu">
                    <ul>
                        <li><button @click="logout">Logout</button></li>
                    </ul>
                </div>
            </div> -->
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
    padding-top: 10px;
    position: absolute;
    width: 100%;
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

li {
  padding: 0 10px;
}

.open-menu {
    opacity: 1;
  }

  .close-menu {
    opacity: 0;
    height: 0;
    padding: 0;
  }

.hamburger {
    display: block;
    text-align: right;
    padding: 0 10px 10px 0; 
}

}

</style>
