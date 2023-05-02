<script setup>
  import { ref, onMounted } from 'vue'
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

  const quizURL = "http://127.0.0.1:5000/quiz"

  let data
  let quizIndex = ref(0)
  let secondaryWord  = ref("")
  let answer = ""
  let quizLength = 0
  let userAnswer = ref("")
  let message = ref("")
  let showSkipButton = ref(false)


  function initializeQuiz() {
    const options = {"primaryLanguage": "primary", secondaryLanguage: props.secondaryLanguage, "unit": props.unit, "length": 10}


    // Fetching the quiz data from the API
    fetch(quizURL, {
      method: 'POST',
      body: JSON.stringify(options),
      headers: { 'Content-Type': 'application/json' }
    }).then(res => res.json())
      .then(json => {

        data = json;

        answer = data.words[quizIndex.value].primary;
        secondaryWord.value = data.words[quizIndex.value].secondary;
        console.log(data);
        quizLength = data.words.length;
      })
      .catch(err => console.log("Unable to load quiz data: " + err))

  }

  function loadNextQuestion(){
    if (quizIndex.value < quizLength-1){

    
    quizIndex.value += 1
    secondaryWord.value = data.words[quizIndex.value].secondary
    answer = data.words[quizIndex.value].primary
    userAnswer.value = ""
    message.value = ""
    showSkipButton.value = false
    }
  }

  function submitAnswer(){
  console.log(userAnswer.value)
  console.log(answer)
    if(userAnswer.value.toLowerCase() === answer.toLowerCase()){
      if(isLastQuestion()) {
        completeQuiz()
      } else {
        loadNextQuestion()
      }
    } else {
      message.value = "Incorrect, Try Again."
      showSkipButton.value = true
    }
}

  function completeQuiz() {
    const options = { 
      language: userToken.language,
      userid: userToken.userId,
      unit: parseInt(props.unit),
      quiz: 2
      
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

  function isLastQuestion() {
    return quizIndex.value == quizLength - 1
  }

  // This is a built-in lifecycle hook from Vue
  onMounted(() => {
    console.log("Quiz mounted");
    initializeQuiz()
  });
</script>

<template>
  <div id="fill-in-the-blank-quiz">
    <div class="progress">{{ quizIndex + 1 }}/{{ quizLength }}</div>
    <div class="question">
      <span class="prompt">{{ secondaryWord }}</span>
      <input type="text" v-model="userAnswer" placeholder=" " />
    </div>
    <button @click="submitAnswer" type="button">Submit</button>
    <div class="message">{{ message }}</div>
    <button :if="showSkipButton" @click="loadNextQuestion" type="button">Skip</button>
  </div>
</template>

<style scoped>

</style>
