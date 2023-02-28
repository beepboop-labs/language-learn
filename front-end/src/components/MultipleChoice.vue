<script setup>
  import data from '../data.json';

  // console.log(data)
  let currentScore = 0
  let currentIndex = 0;
  let englishWord  = data.words[currentIndex].english
  let spanishWord = data.words[currentIndex].spanish
  let answerOptions = []
  let quizLength = data.words.length
  let selectedAnswer = ""

  let gradeMsg = ""

  function setAnswerOptions() {
    // add the correct answer to the answer options
    answerOptions.push(data.words[currentIndex].spanish)
    
    // add 3 random options that are not the correct answer
    let choice = currentIndex
    for(let i=0; i < 3; i++){
      while(answerOptions.includes(data.words[choice].spanish)) {
        choice = Math.floor(Math.random() * data.words.length)
      }

      answerOptions.push(data.words[choice].spanish)
    }

    // scramble the answer options array
    answerOptions = answerOptions.sort((a, b) => 0.5 - Math.random());
  }

  function checkAnswer(){
    console.log(selectedAnswer)
    console.log(data.words[currentIndex].spanish)
    return  selectedAnswer == data.words[currentIndex].spanish
  }

  function submitAnswer(){
    console.log("Button was clicked")
    console.log(checkAnswer())
    // The answer is correct
    if(checkAnswer()){

    // increment the score
    currentScore += 1
    console.log(currentScore)
    // move to the next question
    currentIndex +=1

    gradeMsg = ""

    //reset the quiz options
    setAnswerOptions()

    // the answer is incorrect    
    } else {
      gradeMsg = "Incorrect, Try Again."
    }
    this.$forceUpdate()
  }

  
  setAnswerOptions()
  console.log(answerOptions)


</script>

<template>
  <div class="content">
    <div class = "progress">{{ currentIndex }}/{{ quizLength }}</div>
    <div class = "question">
        <span class = "prompt">How do you say </span>
        <span class = "keyword">"{{englishWord}}"</span>
    </div>
    <div class = "options">
        <div v-for="option in answerOptions">
            <input type = "radio" :id = "option" name = "answers" :value = "option" v-model="selectedAnswer">
            <label :for ="option"> {{ option }} </label>
        </div>
    </div>
    <button @click="submitAnswer" type ="button"> Submit </button>
    <div class="grade-msg">{{ gradeMsg }}</div>
  </div>
</template>

<style scoped>

</style>
