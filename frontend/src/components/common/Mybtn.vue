<template>
  <router-link :to="to"  class="btn btn-outline-danger my-5">{{ name }}</router-link>
</template>

<script>
export default {
    name: "Button",
    props: ["name", "to"]
}
</script>

<style>
.btn-outline-danger:active {
    outline: none!important;
    color: #fff!important;
    background-color: #dc3545;
}
.btn-outline-danger:hover {
    color: #fff!important;
    background-color: #dc3545;
}
.btn-outline-danger {
    color: red!important;
    border-color: red!important;
}
</style>