<template>
  <div class="text-bg-dark" id="main-box">
    <h1 v-if="!isLogin">오늘의 영화</h1>
    <h1 v-if="isLogin">{{username}}님 반갑습니다.</h1>
    <div class="d-flex flex-wrap justify-content-center">
    <MovieMain/>
    <!-- <MovieList v-for="movie in movieList" :key="movie.id" :movie="movie"/>  -->
    </div>
    <div>
    <RecommendView v-show="isLogin" />
    </div>
    </div>
</template>

<script>
// import MovieList from '@/components/MovieList'
import RecommendView from '@/views/movielist/RecommendView'
import MovieMain from '@/components/MovieMain'

export default {
    name: 'HomeView',
    components: {RecommendView, MovieMain,},
    computed:{
      movieList(){
        console.log(this.$store.state.movieList);
        return this.$store.state.movieList?.slice(1,11)
      }
    },
    data(){
      return {
        isLogin: null,
        username: null
      }
    },
    created(){
        // this.$store.commit('GET_MOVIE_LIST')
        // 로그인 여부에 따라 변수 바꾸기
        if (localStorage.getItem('username')){
          this.isLogin = true
          this.username = localStorage.getItem('username')
        } else {
          this.isLogin = false
        }
    },
    }

</script>

<style>

</style>