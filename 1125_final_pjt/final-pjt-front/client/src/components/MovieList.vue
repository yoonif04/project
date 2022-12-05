<template>
  <div class="card text-bg-dark d-flex" style="width: 18rem">
    <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movie.id} }" class="item d-flex justify-content-center align-items-center">
      <div class="d-flex flex-wrap">
          <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" class="card-img-top cardimg " alt="">
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name:'MovieList',
  props:{
    movie: Object
  },
}
</script>

<style scoped>
.cardimg{
  height:450px;
}

.truncate {
  overflow:hidden;
  line-height: 2rem;
  max-height: 8rem;
  -webkit-box-orient: vertical;
  display: block;
  display: -webkit-box;
  overflow: hidden !important;
  text-overflow: ellipsis;
  -webkit-line-clamp: 4;
}


</style>

