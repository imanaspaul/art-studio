<template>
  <div class="container-fluid bg-white">
      <div class="container py-5 text-center">
        <Heading title="OUR MISSION" subheading='Our primary mission is to empower artists by helping them to gain recognition.' />
        <div class="row text-center">
          <div class="col-md-6 offset-md-3">
               
                <p>{{des}}</p>
          </div>
        </div>
  </div>
  </div>
</template>

<script>
import Heading from '../common/Heading'
export default {
    name: "OurMission",
    props: ['des'],
    components : {
        Heading,
    }
}
</script>

<style scoped>
.vertical-line{
    content: '';
    width: 30px;
    height: 2px;
    border-bottom: 2px solid red;
    transform-origin: center 1.5px;
}


</style>