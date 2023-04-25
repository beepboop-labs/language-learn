<script setup>
  import { ref, watch, onMounted } from 'vue';
  import { useRouter, useRoute } from 'vue-router'

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
  let answerOptions = []
  let quizLength = 0
  let selectedAnswer = ref("")
  let message = ref("")



  function setAnswerOptions() {
    // reset to an empty array
    answerOptions = []

    // add the correct answer
    answerOptions.push(data.words[quizIndex.value].secondary)
    
    // add 3 random options that are not the correct answer
    let choice = quizIndex.value
    
    for(let i=0; i < 3; i++){

      // don't add words that are already in the array
      while(answerOptions.includes(data.words[choice].secondary)) {
        choice = Math.floor(Math.random() * data.words.length)
      }

      answerOptions.push(data.words[choice].secondary)
    }

    // scramble the answer options so the correct answer isnt
    // always in the same position
    answerOptions = answerOptions.sort((a, b) => 0.5 - Math.random());
  }

  function isCorrectAnswer(){
    return  selectedAnswer.value == data.words[quizIndex.value].secondary
  }

  function isLastQuestion() {
    return quizIndex.value == quizLength - 1
  }

  function loadNextQuestion(){

    quizIndex.value +=1

    primaryWord.value  = data.words[quizIndex.value].primary
    secondaryWord.value = data.words[quizIndex.value].secondary

    //reset the quiz options
    setAnswerOptions()
    selectedAnswer.value = ""
    message.value = ""

  }

  function completeQuiz() {
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
    const options = {"primaryLanguage": "english", secondaryLanguage: props.secondaryLanguage, "unit": props.unit, "length": 10}
    console.log(options)
    // Fetch the quiz data from the API
    fetch(quizURL, {
      method: 'POST',
      body: JSON.stringify(options),
      headers: { 'Content-Type': 'application/json' }
    }).then(res => res.json())
      .then(json => {
        data = json;

        console.log(json)
        
        primaryWord.value = data.words[quizIndex.value].primary;
        secondaryWord.value = data.words[quizIndex.value].secondary;
        quizLength = data.words.length;

        setAnswerOptions()

      })
      .catch(err => console.log("Unable to load quiz data: " + err))

  }

  // This is a built-in lifecycle hook from Vue
  onMounted(() => {
    console.log("Quiz mounted");
    // console.log($route.params.langauge)
    // console.log($route.params.unit)
    initializeQuiz(props.language, props.unit)
  });
 
  

</script>

<template>
  <br>
  MULTIPLE CHOICE QUIZ
  <br><br>
  <div id="multiple-choice-quiz">
    <div class = "progress">{{ quizIndex + 1 }}/{{ quizLength }}</div>
    <div class = "question">
        <span class = "prompt">How do you say </span>
        <span class = "keyword">"{{primaryWord}}"</span>
    </div>
    <div class = "options">
        <div v-for="option in answerOptions">
            <input type = "radio" :id = "option" name = "answers" :value = "option" v-model="selectedAnswer">
            <label :for ="option"> {{ option }} </label>
        </div>
    </div>
    <button @click="submitAnswer" type ="button"> Submit </button>
    <div class="message">{{ message }}</div>
  </div>
</template>

<style scoped>

</style>
