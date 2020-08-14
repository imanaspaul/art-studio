<template>
  <div class="container py-5">
      <Heading title="CURRENT EXHIBITIONS"/>
      <div class="row py-5 text-center" v-if="loading">
          <h1>Loading..</h1>
      </div>
      <div class="row" v-else>
          <CompetetionCard 
          v-for="comp in allComepetetions"
          :key="comp.id" 
            :title="comp.name"
            :description="comp.description"
            :thumbnail="comp.thumnail"
            :to="comp.id"
           />
      </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import CompetetionCard from '../components/common/CompetetionCard'
import Heading from '../components/common/Heading'
export default {
    name: "current-exhibitions",
    mounted () {
    this.$store.dispatch('fetchCompetetions')
    },
    computed: mapState([
        'loading',
        'allComepetetions',
        'error',
    ]),
    components: {
        CompetetionCard, 
        Heading
    }
}
</script>

<style>

</style>