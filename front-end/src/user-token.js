import { reactive } from 'vue'

export let userToken = reactive({
  userId: null,
  username: null,
  loggedin: false,
   
  setUser(userId, username) {
    this.userId = userId,
    this.username = username
    this.loggedin = true
    console.log("successfully set user in store")
  },
  getUsername(){
    return this.username;
  },
  getUserId() {
    return this.userId;
  },
  getLoggedIn(){
    console.log(this.loggedin)
    return this.loggedin;
  },
  clearUser() {
    this.userId = null;
    this.username = null;
    this.loggedin = false;
  }

})