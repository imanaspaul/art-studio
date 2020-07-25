<template>
  <div class="row text-center">
        <div class="col-md-6 offset-md-3 pt-5">
              <h1 class="font-weight-bold">{{ title }}</h1>
               <svg class="line" x="0px" y="0px"
width="100" height="100"
viewBox="0 0 172 172"
style=" fill:#000000;"><g transform=""><g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z" fill="none"></path><path d="" fill="none"></path><path d="" fill="none"></path><path d="" fill="none"></path><path d="" fill="none"></path><path d="" fill="none"></path><g fill="#ff0d0d"><path d="M6.88,82.56v6.88h158.24v-6.88z"></path></g></g></g></svg>
              <p class="py-3 font-weight-bold">{{subheading}}</p>   
        </div>
    </div>
</template>

<script>
export default {
    props: ['title', 'subheading']
}
</script>

<style>
.line{
    margin-top: -30px;
}
</style>