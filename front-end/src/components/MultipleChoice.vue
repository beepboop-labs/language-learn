<script setup>
import data from '../data.json';

console.log(data)

let currentScore = 0
let english  = data.words[currentIndex].english
let spanish = data.words[currentIndex].spanish
let currentIndex = 0;
let answerOptions = []

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
  } else {
    gradeMsg = "Incorrect"
  }
}



</script>

<template>
  <div class="content">
    <div class = "question">
        <div class = "prompt">
            How do you say 
        </div>
        <div class = "keyword">
            Yourself
        </div>
    </div>
    <div class = "options">
        <div>
            <input type = "radio" id = "text" name = "answers" value = "text">
            <label for ="text"> text </label>
        </div>
    </div>
    <button type ="button"> Submit </button>
  </div>
</template>

<style scoped>

</style>
