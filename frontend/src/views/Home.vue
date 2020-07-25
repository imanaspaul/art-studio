<template>
  <div class="home">
     <Hero/>
     <OurMission/>
     <div class="container py-5 text-center">
       <Heading title="ONLINE GALLERY" subheading='Our online exhibitions give artists an opportunity to receive international exposure.' />
       <img src="https://static.wixstatic.com/media/6b110f_b2a162fc682d4cc2ad7b75288eae9f92~mv2.png/v1/fill/w_1170,h_502,al_c,q_90/virtual-3d-gallery_orig.webp" alt="gallery-image" class="img-fluid" width="900px">
     </div>
  </div>
</template>

<script>
import Hero from '../components/pageComponent/Hero'
import OurMission from '../components/pageComponent/OurMission'
import Heading from '../components/common/Heading'
export default {
  name: 'Home',
  components: {
    Hero,
    OurMission,
    Heading
  }
}
</script>
