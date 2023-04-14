<script setup>
  import { ref, onMounted } from 'vue'

  const quizURL = "http://127.0.0.1:5000/quiz"

  let data
  let quizIndex = ref(0)
  let spanishWord  = ref("")
  let answer = ""
  let quizLength = 0
  let userAnswer = ref("")
  let message = ref("")
  let showSkipButton = ref(false)

  function initializeQuiz() {
    const options = {}

    // Fetching the quiz data from the API
    fetch(quizURL, {
      method: 'POST',
      body: JSON.stringify(options),
      headers: { 'Content-Type': 'application/json' }
    }).then(res => res.json())
      .then(json => {

        data = json;

        answer = data.words[quizIndex.value].english;
        spanishWord.value = data.words[quizIndex.value].spanish;
        console.log(data);
        quizLength = data.words.length;
      })
      .catch(err => console.log("Unable to load quiz data: " + err))

  }

  function loadNextQuestion(){
    quizIndex.value += 1
    spanishWord.value = data.words[quizIndex.value].spanish
    answer = data.words[quizIndex.value].english
    userAnswer.value = ""
    message.value = ""
    showSkipButton.value = false
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
    message.value = "Congratulations, you finished the quiz!"
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
      <span class="prompt">{{ spanishWord }}</span>
      <input type="text" v-model="userAnswer" placeholder=" " />
    </div>
    <button @click="submitAnswer" type="button">Submit</button>
    <div class="message">{{ message }}</div>
    <button :if="showSkipButton" @click="loadNextQuestion" type="button">Skip</button>
  </div>
</template>

<style scoped>

</style>
