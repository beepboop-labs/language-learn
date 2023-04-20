<script setup>
import { userToken } from '../user-token';
import { ref, onMounted, watch } from 'vue'

let activity = ref({
    "user-id": null,
    "username": null,
    "spanish": {
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
    "swahili": {
      "unit1": {
        "q1": false ,
        "q2": false ,
        "q3": false
      },
      "unit2": {
        "q1": false ,
        "q2": false,
        "q3": false 
      },
      "unit3": {
        "q1": false ,
        "q2": false ,
        "q3": false 
      }
    } 
  })
let loggedin = ref(userToken.getLoggedIn())
// This is a built-in lifecycle hook from Vue
onMounted(() => {
  
   loggedin.value = userToken.getLoggedIn()
   getActivity()
    
  });

  watch(userToken, () => {
  loggedin.value = userToken.getLoggedIn()
})

function getActivity(){
  const options = { 
      username: userToken.getUsername(),   
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
          console.log(json.spanish.unit1.q1)
          activity.value = json
          
      })
      .catch(err => {
        alert('Unable to get activity. ' + err)
      })
  }


</script>

<template>
  <div class="container">
    <img src="../assets/Images/istockphoto-1268465415-612x612.jpg" class="image" alt="..." v-if="!loggedin">
    
   <!-- <div id="login-message" v-if="!loggedin">
    <p>Please login to view the roadmap</p>
  </div> -->
  <!-- <div>{{ activity.spanish.unit1.q1 }}</div> -->
  <div id="roadmap" v-if="loggedin">
    <h1>SPANISH</h1>
<<<<<<< HEAD
    <h2>Unit 1</h2>
=======
    <h2>Unit 1 (present, preterite, imperfect)</h2>
>>>>>>> 579cc42906ade52f75538ec5030e2ee8c9391bc1
    <p></p>
    <ul>
      
      <li>
<<<<<<< HEAD
        <router-link :to="{name: 'MultipleChoiceQuiz', params:{secondaryLanguage: 'spanish', unit: 1}}">Multiple Choice</router-link>
        <span v-if="activity.spanish.unit1.q1">  -->Completed!</span>
      </li>
      <li>
        <router-link :to="{name: 'BlankQuiz', params:{secondaryLanguage: 'spanish', unit: 1}}">Fill in the Blank</router-link>
        <span v-if="activity.spanish.unit1.q2">  -->Completed!</span>
      </li>
      <li>
        <router-link :to="{name: 'TrueFalse', params:{secondaryLanguage: 'spanish', unit: 1}}">True or False</router-link>
        <span v-if="activity.spanish.unit1.q3">  -->Completed!</span>
      </li>
    </ul>
    <h2>Unit 2</h2>
    <p></p>
    <ul>
      <li>
        <router-link :to="{name: 'MultipleChoiceQuiz', params:{secondaryLanguage: 'spanish', unit: 2}}">Multiple Choice</router-link>
        <span v-if="activity.spanish.unit2.q1">  -->Completed!</span>
      </li>
      <li>
        <router-link :to="{name: 'BlankQuiz', params:{secondaryLanguage: 'spanish', unit: 2}}">Fill in the Blank</router-link>
        <span v-if="activity.spanish.unit2.q2">  -->Completed!</span>
      </li>
      <li>
        <router-link :to="{name: 'TrueFalse', params:{secondaryLanguage: 'spanish', unit: 2}}">True or False</router-link>
        <span v-if="activity.spanish.unit2.q3">  -->Completed!</span>
      </li>
      
    </ul>
    <h2>Unit 3</h2>
    <p></p>
    <ul>
      <li>
        <router-link :to="{name: 'MultipleChoiceQuiz', params:{secondaryLanguage: 'spanish', unit: 3}}">Multiple Choice</router-link>
        <span v-if="activity.spanish.unit3.q1">  -->Completed!</span>
      </li>
      <li>
        <router-link :to="{name: 'BlankQuiz', params:{secondaryLanguage: 'spanish', unit: 3}}">Fill in the Blank</router-link>
        <span v-if="activity.spanish.unit3.q2">  -->Completed!</span>
      </li>
      <li>
        <router-link :to="{name: 'TrueFalse', params:{secondaryLanguage: 'spanish', unit: 3}}">True or False</router-link>
        <span v-if="activity.spanish.unit3.q3">  -->Completed!</span>
=======
        <span>Multiple Choice Quiz</span>
        <span v-if="activity.spanish.unit1.q1">  -->Completed</span>
      </li>
      <li>
        <span>Blank Quiz</span>
        <span v-if="activity.spanish.unit1.q2">  -->Completed</span>
      </li>
      <li>
        <span>True/False</span>
        <span v-if="activity.spanish.unit1.q3">  -->Completed</span>
      </li>
    </ul>
    <h2>Unit 2 (past)</h2>
    <p></p>
    <ul>
      <li>
        <span>Multiple Choice Quiz</span>
        <span v-if="activity.spanish.unit2.q1">  -->Completed</span>
      </li>
      <li>
        <span>Blank Quiz</span>
        <span v-if="activity.spanish.unit2.q2">  -->Completed</span>
      </li>
      <li>
        <span>True/False</span>
        <span v-if="activity.spanish.unit2.q3">  -->Completed</span>
      </li>
      
    </ul>
    <h2>Unit 3 (Conditional, Future)</h2>
    <p></p>
    <ul>
      <li>
        <span>Multiple Choice Quiz</span>
        <span v-if="activity.spanish.unit3.q1">  -->Completed</span>
      </li>
      <li>
        <span>Blank Quiz</span>
        <span v-if="activity.spanish.unit3.q2">  -->Completed</span>
      </li>
      <li>
        <span>True/False</span>
        <span v-if="activity.spanish.unit3.q3">  -->Completed</span>
>>>>>>> 579cc42906ade52f75538ec5030e2ee8c9391bc1
      </li>
    </ul>
  </div>
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