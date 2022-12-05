<template>
  <div id="main-box">
    <h1>랜덤 추천</h1>
    <RandomItem style="float:left; margin:10px;" v-for="movie in randomList" :key="movie.id" :movie='movie'/>
  </div>
</template>

<script>
import _ from 'lodash'
import RandomItem from '@/components/RandomItem'

export default {
    name:"RandomView",
    components:{RandomItem},
    computed:{
      randomList(){
        return _.sampleSize(this.$store.state.movieList, 15)
    }
    },
}
</script>

<style>

</style>