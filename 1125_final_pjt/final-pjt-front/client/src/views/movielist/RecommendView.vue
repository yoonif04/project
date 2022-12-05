<template>
  <div >
    <!-- <h2>추천 페이지</h2> -->
    
    <!-- 평점 순 -->
    <br>
    <h3 class="text-left" style="text-align:left; margin-left: 20px">평점 순</h3>
    <div class="card-group">
        <MovieList v-for="movie in voteavgList" :key="movie.id" :movie="movie"/>
        <hr>
    </div>
    
    <!-- 랜덤 -->
    <br>
    <h3 class="text-left" style="text-align:left; margin-left: 20px">랜덤</h3>
    <div class="card-group">
        <MovieList v-for="movie in randomList" :key="movie.id" :movie="movie" class="rm_page"/>
        <hr>
    </div>
    
    <!-- 장르 - 판타지 -->
    <br>
    <h3 class="text-left" style="text-align:left; margin-left: 20px">판타지</h3>
    <div class="card-group">
        <MovieList v-for="movie in genreList" :key="movie.id" :movie="movie"/>
        <hr>
    </div>
    
    <!-- 클래식: 2000~2009 -->
    <br>
    <h3 class="text-left" style="text-align:left; margin-left: 20px">클래식</h3>
    <div class="card-group">
        <MovieList v-for="movie in classicList" :key="movie.id" :movie="movie"/>
        <hr>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import MovieList from '@/components/MovieList'

export default {
  name: "RecommendView",
  components:{
    MovieList
  },
  computed:{
    voteavgList(){
        return _.orderBy(this.$store.state.movieList, 'vote_average', 'desc')?.slice(1,6)
    },
    randomList(){
        return _.sampleSize(this.$store.state.movieList, 5)
    },
    genreList(){
        const fantasy = _.sampleSize(this.$store.state.movieList?.filter((movie) => {
            if (movie.genre_ids.some((genre)=> genre.name === '판타지')){
                return movie
            }
        }), 5)
        return fantasy
    },
    classicList(){
        const newYear = _.sampleSize(this.$store.state.movieList?.filter((movie)=>{
            const year = Number(movie.release_date.slice(0,4))
            if(year < 2000){
                return movie
            }
        }), 5)
        console.log('클래식')
        console.log(newYear)
        return newYear
    }
  },
  data(){
    return {
    }
  }
}
</script>

<style>
.rm_page :scope{
  justify-content: flex-start;
  border: 1px solid whitesmoke;
}
</style>