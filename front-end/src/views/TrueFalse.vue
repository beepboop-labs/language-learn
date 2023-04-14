<script setup>
  import { ref, onMounted } from 'vue'

  // const fetch = require('node-fetch');
  const quizURL = "http://127.0.0.1:5000/quiz"

  let data
  let quizIndex = ref(0)
  let englishWord  = ref("")
  let spanishWord = ref("")
  let questions = []
  let quizLength = 0
  let selectedAnswer = ref("")
  let message = ref("")


  function setQuestions() {

    for(let i=0; i< data.words.length; i++) {

      let coinToss = Math.round(Math.random()) //generate a 1 or 0 randomly

      if(coinToss == 0){ //generate a pair that matches
        let question = {
          english: data.words[i].english,
          spanish: data.words[i].spanish,
          match: true
        }

        questions.push(question);

      } else { //generate a pair that doesnt match
        let wrongIndex =i
        while(wrongIndex === i) {
          wrongIndex = Math.floor(Math.random() * data.words.length)
        }

        let question = {
          english: data.words[i].english,
          spanish: data.words[wrongIndex].spanish,
          match: false
        }

        questions.push(question);

      }

    }

    englishWord.value = questions[quizIndex.value].english

    spanishWord.value = questions[quizIndex.value].spanish
  }

  function isCorrectAnswer(){
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

    englishWord.value  = questions[quizIndex.value].english
    spanishWord.value = questions[quizIndex.value].spanish

    selectedAnswer.value = ""
    message.value = ""

  }

  function completeQuiz() {
    message.value = "Congratulations, you finished the quiz!"
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
    const options = {}

    // Fetch the quiz data from the API
    fetch(quizURL, {
      method: 'POST',
      body: JSON.stringify(options),
      headers: { 'Content-Type': 'application/json' }
    }).then(res => res.json())
      .then(json => {
        data = json;
        
        // englishWord.value = data.words[quizIndex.value].english;
        // spanishWord.value = data.words[quizIndex.value].spanish;
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
        <div>Does the below translation from english to spanish is True/False?</div>
        <span class="prompt">{{ englishWord }}</span>
        <br/>
        <span class="prompt">{{ spanishWord }}</span>
      </div>
      <div class="options">
        <input type="radio" id="true" name="answers" value="true" v-model="selectedAnswer">
        <label for="true">True</label>
        <input type="radio" id="false" name="answers" value="false" v-model="selectedAnswer">
        <label for="false">False</label>
      </div>
      <button @click="submitAnswer" type="button">Submit</button>
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