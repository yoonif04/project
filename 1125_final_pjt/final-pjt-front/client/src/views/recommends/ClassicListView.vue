<template>
  <div id="main-box">
    <h1>클래식 영화</h1>
          <RandomItem style="float:left; margin:10px;" v-for="movie in classicList" :key="movie.id" :movie='movie'/>
    <!-- <div v-for="movie in classicList" :key="movie.id">
        <div>
            <div class="card text-bg-dark d-flex flex-wrap" style="width: 200px;">
            <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" class="card-img">
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
    name:'ClassicListView',
    components:{RandomItem},
    computed:{
      classicList(){
        const newYear = _.sampleSize(this.$store.state.movieList?.filter((movie)=>{
            const year = Number(movie.release_date.slice(0,4))
            if(year < 2000){
                return movie
            }
        }), 10)
        console.log('클래식')
        console.log(newYear)
        return newYear
    }
    }
}
</script>

<style>

</style>