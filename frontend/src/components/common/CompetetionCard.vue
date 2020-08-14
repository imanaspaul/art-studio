<template>
  <div class="col-md-6 col-lg-4 mb-4">
      <div class="card border-0">
           <v-lazy-image class="hero-img" 
            :src="thumbnail" alt="Image-hero" 
            style="width:100%; height:280px"
            src-placeholder='https://digitalsynopsis.com/wp-content/uploads/2017/06/beautiful-color-palettes-combinations-schemes-grey-lavender-colors.png'
            />
          <div class="card-body">
              <h4>{{title}}</h4>
              <p>{{ description }}</p>
          </div>
          <div class="card-footer text-center bg-white border-0 py-0">
              <Mybtn name="SEE PERTICIPENTS" :to="{ name: 'ExhibitionDetail', params: { id: to }}" />
          </div>
      </div>
  </div>
</template>

<script>
import Mybtn from './Mybtn'
export default {
    name: "completetion-card",
    props : {
        title: String,
        description: String,
        thumbnail: String,
        to: String
    },
    components : {
        Mybtn
    }
}
</script>

<style>

</style>