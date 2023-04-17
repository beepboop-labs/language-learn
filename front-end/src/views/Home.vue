<script setup>
import { userToken } from '../user-token';
import { ref, onMounted, watch } from 'vue'

let loggedin = ref(userToken.getLoggedIn())
// This is a built-in lifecycle hook from Vue
onMounted(() => {
   loggedin.value = userToken.getLoggedIn()
    
  });

  watch(userToken, () => {
  loggedin.value = userToken.getLoggedIn()
})

</script>

<template>
  <div> {{loggedin}}</div>
  <div class="container">
   <div id="login-message" v-if="!loggedin">
    <p>Please login to view the roadmap</p>
  </div>
  </div>


  <div id="roadmap" v-if="loggedin">
    <h1>SPANISH</h1>
    <h2>Unit 1 (present, preterite, imperfect)</h2>
    <p></p>
    <ul>
      <li>Multiple Choice quiz</li>
      <li>Blank Quiz</li>
      <li>True/False</li>
    </ul>
    <h2>Unit 2 (past)</h2>
    <p></p>
    <ul>
      <li>Multiple Choice quiz</li>
      <li>Blank Quiz</li>
      <li>True/False</li>
    </ul>
    <h2>Unit 3 (Conditional, Future)</h2>
    <p></p>
    <ul>
      <li>Multiple Choice quiz</li>
      <li>Blank Quiz</li>
      <li>True/False</li>
    </ul>
  </div>
</template>




<style scoped>
login-message {
  background-color: #f2f2f2;
  padding: 20px;
  text-align: center;
}


#roadmap {
  padding: 20px;
}

#roadmap h1 {
  font-size: 24px;
  font-weight: bold;
}

roadmap h2 {
  font-size: 20px;
  font-weight: bold;
  margin-top: 30px;
}

roadmap ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

roadmap li {
  margin-bottom: 10px;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.image{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.image img {
  display: block;
  margin: auto;
  max-width: 80%;
  height: 50%;
}
</style>