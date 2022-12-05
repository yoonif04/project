<template>
  <div>
    <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movie.id} }">
    <div class="bg-dark d-flex flex-wrap" style="width:18rem; padding:0;">
    <div style="width: 18rem; height:27rem;float:left; margin:0; margin-top: 50px; background-color:transparent">
    <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" class="card-img random_img" >
    <!-- <div class="card-img-overlay" >
        <h5 class="card-title">{{movie.title}}</h5>
    </div> -->
    </div>
    </div>  
    </router-link>
    <p>{{movie.title}}</p>
  </div>
</template>

<script>
export default {
    name:'RandomItem',
    props:{
        movie:Object
    }
}
</script>

<style>
.random_img{
 width: 100%; 
 height:100%;
}
</style>