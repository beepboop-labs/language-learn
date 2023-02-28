<script setup>
  import data from '../data.json';
  // console.log(data)
  let currentScore = 0
  let currentIndex = 0;
  let englishWord  = data.words[currentIndex].english
  let spanishWord = data.words[currentIndex].spanish
  let answerOptions = []
  let quizLength = data.words.length

  let gradeMsg = ""

  function setAnswerOptions() {
    // add the correct answer to the answer options
    answerOptions.push(data.words[currentIndex].spanish)
    
    // choose 3 random options that are not the correct answer
    for(let i=0; i < 3; i++){
      let choice = currentIndex

      while(choice == currentIndex) {
        choice = Math.floor(Math.random() * data.words.length)
      }

      answerOptions.push(data.words[choice].spanish)
    }

    // scramble the answer options array
    answerOptions = answerOptions.sort((a, b) => 0.5 - Math.random());
  }

  function checkAnswer(str){
    return  str == data.words[currentIndex].spanish
  }

  function submitAnswer(str){
    
    // The answer is correct
    if(checkAnswer(str)){

    // increment the score
    currentScore += 1

    // move to the next question
    currentIndex +=1

    gradeMsg = ""

    //reset the quiz options
    setAnswerOptions()

    // the answer is incorrect    
    } else {
      gradeMsg = "Incorrect, Try Again."
    }
  }

  
  setAnswerOptions()



</script>

<template>
  <div class="content">
    <div class = "progress">{{ currentIndex }}/{{ quizLength }}</div>
    <div class = "question">
        <span class = "prompt">How do you say </span>
        <span class = "keyword">"{{englishWord}}"</span>
    </div>
    <div class = "options">
        <div>
            <input type = "radio" id = "text" name = "answers" value = "text">
            <label for ="text"> text </label>
        </div>
    </div>
    <button type ="button"> Submit </button>
    <div class="grade-msg">{{ gradeMsg }}</div>
  </div>
</template>

<style scoped>

</style>
