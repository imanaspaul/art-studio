import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import BASE_URL from '../utils/endpoint'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    allComepetetions : null,
    error: null,
    loading: true
  },
  mutations: {
    setAllCompetetions(state, data){
       state.allComepetetions = data
    },
    setError(state, error){
      state.error = error
    },
    setLoading(state, loadding){
      state.loading = loadding
    }
  },
  actions: {
     fetchCompetetions ({commit}) {
        commit("setLoading", true)
       axios.get(`${BASE_URL}/all-competitions/`)
        .then((result)=>{
           commit("setLoading", false)
           commit('setAllCompetetions', result.data)
        })
        .catch((error)=>{
           commit("setLoading", false)
           commit('setError', error)
        })
    }
  },
  modules: {
  }
})
