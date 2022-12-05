<template>
<div class="pb-5 container" style="height:100vh" id="main-box">
  <h2 v-show="!like_movies">좋아요한 영화가 없습니다.</h2>
  <div class="d-flex justify-content-start" >
    <div v-for="movie in like_movies" :key="movie.id">
    <div class="card text-bg-dark " style="width: 14rem; margin:0.5rem;">
    <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movie.id} }" class="item d-flex justify-content-center align-items-center" >
          <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" class="card-img cardimg" style="height:25rem;">
    </router-link>
  </div>
  </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'LikedView',
    data(){
        return{
            like_movies: null,
        }
    },
    created(){
        const username = this.$route.params.username
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/profile/${username}/like_movies`,
          headers: { 'Authorization': `Bearer ${localStorage.getItem('jwt')}` },
        })
        .then((res)=>{
          console.log('좋아요한 영화 정보')
          console.log(res)
          this.like_movies = res.data
        })
    }
    
}
</script>

<style>
img {
  object-fit: cover;
}
</style>