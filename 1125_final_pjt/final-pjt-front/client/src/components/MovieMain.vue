<template>
  <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel"  v-if="movieList?.length">
    <div class="carousel-inner" style="width:100px height:100px">
      <div class="carousel-item active" style="width:100px height:100px">
        <div class="d-flex flex-row">
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[0].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[0].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[1].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[1].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[2].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[2].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[3].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[3].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[4].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[4].poster_path" alt="">
            </router-link>
          </div>
        </div>
      </div>
      <div class="carousel-item">
        <div class="d-flex flex-row">
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[5].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[5].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[6].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[6].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[7].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[7].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[8].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[8].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[9].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[9].poster_path" alt="">
            </router-link>
          </div>
        </div>
      </div>
      <div class="carousel-item">
        <div class="d-flex flex-row">
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[10].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[10].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[11].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[11].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[12].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[12].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[13].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[13].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[14].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[14].poster_path" alt="">
            </router-link>
          </div>
        </div>
      </div>
      <div class="carousel-item">
        <div class="d-flex flex-row">
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[15].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[15].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[16].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[16].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[17].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[17].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[18].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[18].poster_path" alt="">
            </router-link>
          </div>
          <div id="img-box">
            <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movieList[19].id} }">
              <img id="img-img" :src="'https://image.tmdb.org/t/p/w500' + movieList[19].poster_path" alt="">
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name:'MovieMain',
    computed:{
        movieList(){
        console.log(this.$store.state.movieList);
        return _.sampleSize(this.$store.state.movieList, 20)
      }
    },

}
</script>

<style>
#img-box{
  height: 450px;
  width: auto;
  /* width: 200px; */
  /* height:500px; */
}
#img-img{
  width: auto;
  height: 100%;
  margin-left: 10px;
  margin-right: 10px;
  object-fit: cover;
}
</style>