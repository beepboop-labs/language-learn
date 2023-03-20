<script>
export default {
data() {
return {
showMobileMenu: false,
};
},
methods: {
showMenu() {
this.showMobileMenu = !this.showMobileMenu;
},
},
};
</script>

<template>
    <div id="navbar">
        <div class="nav-menu"> 
            <i class="fas fa-bars" @click="showMenu()"> </i> 
            <div class="nav-content" :class="this.showMobileMenu ? 'open-menu' : 'closed-menu'"> 
            <div class="logo">
                <router-link to="/">LOGO</router-link>
            </div> 
                <ul class="nav-items">
                    <li>
                        <router-link to="/multiple-choice">Multiple Choice Quiz</router-link>
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


i {
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

