<script setup>
import { ref, onMounted, watch} from 'vue';
import { userToken } from '../user-token';

let username = ref(userToken.getUsername())
// This is a built-in lifecycle hook from Vue
onMounted(() => {
  
   username.value = userToken.getUsername()
  
    
  });

  watch(userToken, () => {
  username.value = userToken.getUsername()
})
    
    
let showProfileMenu = ref(false);

function toggleProfileMenu() {
    showProfileMenu.value = !showProfileMenu.value;
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
                    <li>
                        <router-link to="/multiple-choice">Multiple Choice Quiz</router-link>
                    </li>
                    <li>
                        <router-link to="/blankquiz">BlankQuiz</router-link>
                    </li>
                    <li>
                        <router-link to="/truefalse">TrueFalse</router-link>
                    </li>
                </ul>
            <div v-if="!username" class="login-button">
                <router-link to="/login">Login</router-link>
            </div>
            <div v-if="username" class="username">
                <button class="profile-button" @click="toggleProfileMenu">{{ username }}</button>
                <div class="profile-menu" v-if="showProfileMenu">
                    <ul>
                        <li><router-link to="/profile">Profile</router-link></li>
                        <li><button @click="logout">Logout</button></li>
                    </ul>
                </div>
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

  .dropdown {
    position: absolute;
    top: 30px;
    right: 0;
    width: 200px;
    background-color: white;
    z-index: 1;
    border: 1px solid black;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    display: none;
  }

  .dropdown-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 10px;
  }

  .dropdown:hover .dropdown-content {
    display: flex;
  }

  .dropdown-item {
    padding: 10px;
  }

  .logout-button {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #ff7676;
    border-radius: 5px;
    padding: 5px 10px;
    color: white;
    cursor: pointer;
    margin-top: 10px;
  }

  .logout-button:hover {
    background-color: #e35555;
  }
}
}
</style>
