<template>
  <div class="col-md-12">
      <div class="row">
          <div class="col-md-6">
              <h5>First Place</h5>
              
          </div>
          <div class="col-md-6">
              <h5>{{ name }}</h5>
              
          </div>
      </div>
  </div>
</template>

<script>
export default {
    name: "position-card",
    props: [
        "name",
        "image",
        "details",
    ]
}
</script>

<style>

</style>