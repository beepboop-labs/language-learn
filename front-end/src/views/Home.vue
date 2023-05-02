<script setup>
import { userToken } from '../user-token';
import { ref, onMounted, watch } from 'vue'

let activity = ref({
    "userid": null,
    "username": null,
    "language": null,
    "activity": {
      "unit1": {
        "q1": false ,
        "q2": false ,
        "q3": false 
      },
      "unit2": {
        "q1": false ,
        "q2": false ,
        "q3": false 
      },
      "unit3": {
        "q1": false ,
        "q2": false ,
        "q3": false 
      }
    },
  })
let loggedin = ref(userToken.getLoggedIn())
// This is a built-in lifecycle hook from Vue
onMounted(() => {
  
   loggedin.value = userToken.getLoggedIn()
   if(loggedin.value){
    getActivity()

   }
   
    
  });

  watch(userToken, () => {
  loggedin.value = userToken.getLoggedIn()
})

function setLanguage(lang){
  userToken.language = lang
  console.log(lang)
  console.log(userToken.language)
  getActivity()

}
function getActivity(){
  const options = { 
      language: userToken.language,
      userid: userToken.userId,
    }

    // send login data to the API 
    fetch("http://127.0.0.1:5000/user/activity", { 
      method: 'POST',
      body: JSON.stringify(options),
      headers: { 'Content-Type': 'application/json' } 
    }).then(res => res.json().then(json => ({
        response: res,
        json
      })))
      .then(({ response, json }) => {
          if(!response.ok){
            throw new Error(response.status + " " + json.message);
          }
          
          activity.value = json
          
      })
      .catch(err => {
        alert('Unable to get activity. ' + err)
      })
  }


</script>

<template>
  <div class="container">
    <div class="welcome" v-if="!loggedin">
      <h1>Welcome to the Language Learning App!</h1>
      <p>Please login or register to view the course roadmap</p>
    
      <img src="../assets/Images/istockphoto-1268465415-612x612.jpg" class="image" alt="...">
    </div>
   <!-- <div id="login-message" v-if="!loggedin">
    <p>Please login to view the roadmap</p>
  </div> -->
  <!-- <div>{{ activity.spanish.unit1.q1 }}</div> -->
  <div id="roadmap" v-if="loggedin">
    <h4>Choose a language:</h4>
    <button type="button" @click="setLanguage('spanish')">Spanish</button>
    <button type="button" @click="setLanguage('swahili')">Swahili</button>
    <h1>{{ userToken.language }}</h1>
    <h2>Unit 1</h2>
    <ul> 
      <li>
        <router-link :to="{name: 'MultipleChoiceQuiz', params:{secondaryLanguage: userToken.language, unit: 1}}">Multiple Choice</router-link>
        <span v-if="activity.activity.unit1.q1">  -->Completed!</span>
      </li>
      <li>
        <router-link :to="{name: 'BlankQuiz', params:{secondaryLanguage: userToken.language, unit: 1}}">Fill in the Blank</router-link>
        <span v-if="activity.activity.unit1.q2">  -->Completed!</span>
      </li>
      <li>
        <router-link :to="{name: 'TrueFalse', params:{secondaryLanguage: userToken.language, unit: 1}}">True or False</router-link>
        <span v-if="activity.activity.unit1.q3">  -->Completed!</span>
      </li>
    </ul>
    <h2>Unit 2</h2>
    <p></p>
    <ul>
      <li>
        <router-link :to="{name: 'MultipleChoiceQuiz', params:{secondaryLanguage: userToken.language, unit: 2}}">Multiple Choice</router-link>
        <span v-if="activity.activity.unit2.q1">  -->Completed!</span>
      </li>
      <li>
        <router-link :to="{name: 'BlankQuiz', params:{secondaryLanguage: userToken.language, unit: 2}}">Fill in the Blank</router-link>
        <span v-if="activity.activity.unit2.q2">  -->Completed!</span>
      </li>
      <li>
        <router-link :to="{name: 'TrueFalse', params:{secondaryLanguage: userToken.language, unit: 2}}">True or False</router-link>
        <span v-if="activity.activity.unit2.q3">  -->Completed!</span>
      </li>
      
    </ul>
    <h2>Unit 3</h2>
    <p></p>
    <ul>
      <li>
        <router-link :to="{name: 'MultipleChoiceQuiz', params:{secondaryLanguage: userToken.language, unit: 3}}">Multiple Choice</router-link>
        <span v-if="activity.activity.unit3.q1">  -->Completed!</span>
      </li>
      <li>
        <router-link :to="{name: 'BlankQuiz', params:{secondaryLanguage: userToken.language, unit: 3}}">Fill in the Blank</router-link>
        <span v-if="activity.activity.unit3.q2">  -->Completed!</span>
      </li>
      <li>
        <router-link :to="{name: 'TrueFalse', params:{secondaryLanguage: userToken.language, unit: 3}}">True or False</router-link>
        <span v-if="activity.activity.unit3.q3">  -->Completed!</span>
      </li>
    </ul>
  </div>
  </div>
</template>




<style scoped>
#login-message {
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
  display: block;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  margin-bottom: 40px;
}

.welcome {
  text-align: center;
}
.image{
  display: flex;
  margin: 0 auto;
  height: 60vh;
  width: 60vw;
}

.image img {
  display: block;
  margin: auto;
  max-width: 80%;
  height: 50%;
}
</style>
