<template>
  <div class="bg-dark" id="main-box">
    <h1>평점</h1>
    <RandomItem style="float:left; margin:10px;" v-for="movie in voteavgList" :key="movie.id" :movie='movie'/>
    <!-- <div v-for="movie in voteavgList" :key="movie.id" style="float:left; margin:10px; border:0;">
        <div class="container text-center">
            <div class="bg-dark d-flex flex-wrap row" style="width: 300px;">
              <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" class="card-img col-6">
              <div class="card-img-overlay">
                  <h5 class="card-title">{{movie.title}}</h5>
              </div>
            </div>  
        </div>        
    </div> -->
  </div>
</template>

<script>
import _ from 'lodash'
import RandomItem from '@/components/RandomItem'

export default {
    name:'VoteavgView',
    components:{RandomItem},
    computed:{
      voteavgList(){
        return _.orderBy(this.$store.state.movieList, 'vote_average', 'desc')?.slice(1,6)
    },
    }
}
</script>

<style>

</style>