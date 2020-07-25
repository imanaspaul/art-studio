<template>
  <div id="app">
    <TheNav/>
    <div>
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
body{
  font-family: arial;
}
@media only screen and (max-width: 1345px) {
  .nav-item{
    margin-right:0px;
}
.nav-link{
  font-size: 13px!important;
}
}
</style>
