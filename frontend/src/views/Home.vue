<template>
  <div class="home">
     <Hero/>
     <OurMission des='The International Art Showcase (IAS) was established as a platform for emerging and established artists to exhibit their work to a global audience. Our website features a curated selection of contemporary art, as well as international art market news relevant to professional artists.'/>
     <div class="container py-5 text-center">
       <Heading title="ONLINE GALLERY" subheading='Our online exhibitions give artists an opportunity to receive international exposure.' />
       <v-lazy-image 
       src="https://static.wixstatic.com/media/6b110f_b2a162fc682d4cc2ad7b75288eae9f92~mv2.png/v1/fill/w_1170,h_502,al_c,q_90/virtual-3d-gallery_orig.webp" alt="gallery-image" class="img-fluid" style="width:900px"
       src-placeholder="https://coolbackgrounds.io/images/backgrounds/black/black-contour-f41038db.svg"
       />
       <br>
       <Mybtn name="ONLINE GALLERY"/>
       <div class="text-center px-5">
         <p>IAS organizes juried online art shows on a monthly basis. Each exhibition is presented in one of our virtual 3D gallery spaces and features only the very best artworks submitted in response to our open-competition calls. Selected artists will gain recognition by being awarded a "Best of Show", or one of our three "Merit Award" certificates. These selected artists will also get additional exposure by being promoted on our Featured Artists page.</p>
       </div>
       <Mybtn name="CALL-FOR-ARTIST"/>
     </div>
     <img 
      src="../assets/bg.webp"
      src-placeholder="https://coolbackgrounds.io/images/backgrounds/black/black-contour-f41038db.svg"
      alt="backgroud image" 
      class="img-fluid"
     >
    <div class="container-fluid bg-white">
       <div class="container">
        <OurMission
         des="Here at International Art Showcase, we love art. Each week, we feature an artist whose work inspires us. Our Featured Artists page highlights the 'Best of Show' and Merit Award' winners of our monthly exhibitions. The page also features some of today's most talented artists."
         title='FEATURED ARTISTS'
         
         />
     </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Home',
  components: {
    Hero : () => import(/* webpackChunkName: "hero" */ '../components/pageComponent/Hero'),
    OurMission  : () => import(/* webpackChunkName: "our-mission" */ '../components/pageComponent/OurMission'),
    Heading : () => import(/* webpackChunkName: "heading" */'../components/common/Heading'),
    Mybtn : () => import(/* webpackChunkName: "Mybtn" */'../components/common/Mybtn'),
  }
}
</script>
<style lang="css" scoped>
.v-lazy-image {
  filter: blur(10px);
  transition: filter 0.7s;
}
.v-lazy-image-loaded {
  filter: blur(0);
}
</style>
