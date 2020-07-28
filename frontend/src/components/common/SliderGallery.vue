<template>
  <swiper class="swiper" :options="swiperOption">
    <swiper-slide v-for="image in images" :key="image.id">
        <img :src="image.img" alt="slider-gallery" width="300" height="250" style="object-fit: cover">
    </swiper-slide>
  </swiper>
</template>

<script>
  import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
  import 'swiper/css/swiper.css'

  export default {
    name: 'swiper-example-loop',
    title: 'Loop mode / Infinite loop',
    components: {
      Swiper,
      SwiperSlide
    },
    data() {
      return {
        swiperOption: {
          slidesPerView: 1,
          spaceBetween: 30,
          loop: true,
          autoplay: {
            delay: 2000,
            disableOnInteraction: false
          },
        },
        images : [
          {'id': 1, 'img': "https://static.wixstatic.com/media/6b110f_5fe87ddafaa54cdda94679294d518936~mv2.jpg/v1/fill/w_424,h_306,al_c,lg_1,q_80/6b110f_5fe87ddafaa54cdda94679294d518936~mv2.webp"},
          {'id': 2, 'img': "https://static.wixstatic.com/media/6b110f_be61e849d7aa47028e3ee8db72279cb2~mv2.jpg/v1/fill/w_216,h_306,al_c,lg_1,q_80/6b110f_be61e849d7aa47028e3ee8db72279cb2~mv2.webp"},
          {'id': 3, 'img': "https://static.wixstatic.com/media/6b110f_adf1f3b58dfa4ba3936aae0d66390662~mv2.jpg/v1/fill/w_306,h_306,al_c,lg_1,q_80/6b110f_adf1f3b58dfa4ba3936aae0d66390662~mv2.webp"},
        ]
      }
    }
  }
</script>
