<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
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
