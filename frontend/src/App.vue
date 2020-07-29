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
.nav-item{
    margin-right:30px;
    
}
.active{
    transition: cubic-bezier(0.075, 0.82, 0.165, 1);
}
.nav-link:hover{
    color: grey!important;
}
.router-link-exact-active {
    border: 1.5px solid red;
}
.nav-item:last-child{
    margin-right: 0px;
}
.nav-link{
  font-size: 11px!important;
  font-weight: 500!important;
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
