<template>
  <div id="app">
    <TheNav/>
    <div>
      <router-view/>
    </div>
  </div>
</template>
<script>
// import TheNav from './components/common/TheNav'
export default {
  components : {
    TheNav  : () => import(/* webpackChunkName: "Thenav" */'./components/common/TheNav'),
  }
}
</script>

<style>
body{
  font-family: arial;
}
p{
    font-size: 20px;
}

@media only screen and (max-width: 1500px) {
  .nav-item{
    margin-right:0px;
}
.nav-link{
  font-size: 13px!important;
}
}
@media only screen and (max-width: 1250px) {
  .nav-item{
    margin-right:0px;
}
.nav-link{
  font-size: 9px!important;
}
}
</style>
