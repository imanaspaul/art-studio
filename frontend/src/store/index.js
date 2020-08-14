import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import BASE_URL from '../utils/endpoint'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    allComepetetions : null,
    error: null,
    loading: true,
    currentComp: null
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
    },
    setItem(state, payload){
      let items = state.allComepetetions.filter((com)=> {return com.id === payload})
      state.currentComp = items[0]
    }
  },
  actions: {
     fetchCompetetions ({commit}) {
        commit("setLoading", true)
       axios.get(`${BASE_URL}/ongoing-competitions/`)
        .then((result)=>{
           commit("setLoading", false)
           commit('setAllCompetetions', result.data)
        })
        .catch((error)=>{
           commit("setLoading", false)
           commit('setError', error)
        })
    },
    setCurrent({commit}, payload){
      console.log("Payload is", payload);
      commit("setItem", payload)
    }
  },
  getters: {
     comp : (state, id) =>{
       console.log(state.allComepetetions);
       return state.allComepetetions.find((com)=> {return com.id === id})
    }
  },
  modules: {
  }
})
