<template>
  <div class="container py-5">
      <h4>{{ currentComp.name }}</h4>
      <p>{{ currentComp.description }}</p>
      <div>
          <div v-for="art in currentComp.artworks" :key="art.id">
              <div v-if="art.approved">
                  <div v-if="art.position > 0">
                      <div v-if="art.position === 1">
                          <Position :name="art.title"/>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Position from '../components/common/Position'
export default {
    name: "Current-competetion-details",
    mounted () {
        this.$store.dispatch('setCurrent', this.$route.params.id)
    },
    computed: mapState([
        'currentComp'
    ]),
    components : {
        Position
    }
}
</script>

<style>

</style>