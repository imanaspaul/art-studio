<template>
  <div id="app">
    <TheNav/>
    <div class="container">
      <router-view/>
    </div>
  </div>
</template>
<script>
import TheNav from './components/common/TheNav'
export default {
  components : {
    TheNav
  }
}
</script>

<style>
@media only screen and (max-width: 1330px) {
  .nav-item{
    margin-right:0px;
}
.nav-link{
  font-size: 13px!important;
}
}
</style>
