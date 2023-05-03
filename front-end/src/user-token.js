import { reactive } from 'vue'

export const userToken = reactive({
  userId: null,
  username: null,
  loggedin: false,
  language: "spanish",
   
  setUser(userId, username) {
    console.log(userId)
    console.log(username)
    console.log(this.loggedin)
    this.userId = userId
    this.username = username
    this.loggedin = true
    console.log(this.loggedin)
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