<script setup>
  import { ref, onMounted, computed } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
  import { userToken } from '../user-token';

  const router = useRouter();

  const props = defineProps({
  secondaryLanguage: {
    type: String,
    required: true
  },
  unit: {
    type: Number,
    required: true
  }
})
  // const fetch = require('node-fetch');
  const quizURL = "http://127.0.0.1:5000/quiz"

  let data
  let quizIndex = ref(0)
  let primaryWord  = ref("")
  let secondaryWord = ref("")
  let questions = []
  let quizLength = 0
  let selectedAnswer = ref("")
  let message = ref("")
  let submitDisabled = computed(() => {
  return selectedAnswer.value == ''
})


  function setQuestions() {

    for(let i=0; i< data.words.length; i++) {

      let coinToss = Math.round(Math.random()) //generate a 1 or 0 randomly

      if(coinToss == 0){ //generate a pair that matches
        let question = {
          primary: data.words[i].primary,
          secondary: data.words[i].secondary,
          match: true
        }

        questions.push(question);

      } else { //generate a pair that doesnt match
        let wrongIndex =i
        while(wrongIndex === i) {
          wrongIndex = Math.floor(Math.random() * data.words.length)
        }

        let question = {
          primary: data.words[i].primary,
          secondary: data.words[wrongIndex].secondary,
          match: false
        }

        questions.push(question);

      }

    }

    primaryWord.value = questions[quizIndex.value].primary

    secondaryWord.value = questions[quizIndex.value].secondary
  }

  function isCorrectAnswer(){
    console.log(selectedAnswer.value)
    console.log(typeof selectedAnswer.value)

    let boolString = (selectedAnswer.value === "true");
    console.log(questions)
    console.log(questions[quizIndex.value].match)
    return boolString === questions[quizIndex.value].match
  }

  function isLastQuestion() {
    return quizIndex.value == quizLength - 1
  }

  function loadNextQuestion(){

    quizIndex.value +=1

    primaryWord.value  = questions[quizIndex.value].primary
    secondaryWord.value = questions[quizIndex.value].secondary

    selectedAnswer.value = ""
    message.value = ""

  }

  function completeQuiz() {
    const options = { 
      language: userToken.language,
      userid: userToken.userId,
      unit: parseInt(props.unit),
      quiz: 3
      
    }
    console.log(props.unit);
    console.log(typeof props.unit);
    console.log(options.unit);
    console.log(typeof options.unit);
    

    // send login data to the API 
    fetch("http://127.0.0.1:5000/user/complete-quiz", { 
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
          
      })
      .catch(err => {
        alert('Unable to get activity. ' + err)
      })
    message.value = "Congratulations, you finished the quiz!"
    router.push("/")  
  }

  function submitAnswer(){

      if(isCorrectAnswer()){

        if(isLastQuestion()) {
          completeQuiz()
        } else {
          loadNextQuestion()
        }
   
      } else {
        message.value = "Incorrect, Try Again."
      }

  }

  function initializeQuiz() {
    //POST request options
    const options = {"primaryLanguage": "primary", secondaryLanguage: props.secondaryLanguage, "unit": props.unit, "length": 10}

    // Fetch the quiz data from the API
    fetch(quizURL, {
      method: 'POST',
      body: JSON.stringify(options),
      headers: { 'Content-Type': 'application/json' }
    }).then(res => res.json())
      .then(json => {
        data = json;
        
        // primaryWord.value = data.words[quizIndex.value].primary;
        // secondaryWord.value = data.words[quizIndex.value].secondary;
        quizLength = data.words.length;

        setQuestions()

      })
      .catch(err => console.log("Unable to load quiz data: " + err))

  }

  // This is a built-in lifecycle hook from Vue
  onMounted(() => {
    console.log("Quiz mounted");
    initializeQuiz()
  });
 
  

</script>

<template>
    <div id="true-false-quiz">
      <div class="progress">{{ quizIndex + 1 }}/{{ quizLength }}</div>
      <div class="question">
        <div>Does the below translation from primary to secondary is True/False?</div>
        <span class="prompt">{{ primaryWord }}</span>
        <br/>
        <span class="prompt">{{ secondaryWord }}</span>
      </div>
      <div class="options">
        <input type="radio" id="true" name="answers" value="true" v-model="selectedAnswer">
        <label for="true">True</label>
        <input type="radio" id="false" name="answers" value="false" v-model="selectedAnswer">
        <label for="false">False</label>
      </div>
      <button @click="submitAnswer" :disabled="submitDisabled" type="button">Submit</button>
      <div class="message">{{ message }}</div>
    </div>
  </template>


<style scoped>

#true-false-quiz {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}

.question {
  font-size: 24px;
  margin-bottom: 20px;
}

.options {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 20px;
}

.options label {
  display: inline-block;
  margin: 0 10px;
  font-size: 20px;
}

button[type="button"] {
  background-color: #c6bfbf;
  border: none;
  color: rgb(10, 9, 9);
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin-bottom: 20px;
  cursor: pointer;
}

.progress {
  font-size: 18px;
  margin-bottom: 20px;
}

.message {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 20px;
}

</style>