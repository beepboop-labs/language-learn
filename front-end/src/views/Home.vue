<script setup>


</script>

<template>
  <div class="row">
        <div class="col-md-12">
            <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="images/istockphoto-1268465415-612x612.jpg" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                        <img src="images/istockphoto-1268465415-612x612.jpg" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                        <img src="images/istockphoto-1268465415-612x612.jpg" class="d-block w-100" alt="...">
                    </div>
                </div>
                <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </a>
                <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </a>
            </div>

        </div>
    </div>
  <div id="home">
    <h1>Homepage</h1>
    <router-link to = "/multiple-choice">Multiple Choice Quiz</router-link>
    <br>
    <router-link to = "/login">Login</router-link>
    <br>
    <router-link to = "/register">Register</router-link>
  </div>
</template>

<style scoped>

</style>