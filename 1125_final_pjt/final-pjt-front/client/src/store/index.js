import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieList: null,
  },
  getters: {
  },
  mutations: {
    GET_MOVIE_LIST(){
      axios({
        method: 'get',
        url:'http://127.0.0.1:8000/movies/',
      })
      .then((res) =>{
        // console.log(res.data)
        this.state.movieList = res.data
        // console.log(this.movieList)
      })
      .catch((err) => {
        console.log(err);
      })
    },
  },
  actions: {
    
},
  modules: {
  }
})
