<script>
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: "App",
  components: {
    Navbar,
    Footer
  }
};
</script>

<template>
  <Navbar />
  <div id="content">
    <router-view />
  </div>
  <Footer />
</template>

