<template>
  <div id="main-box">
    <h1 class="justify-content-center d-flex flex-row">{{userinfo?.username}}의 프로필 
      <div v-if="currentUser !== userinfo?.username">
        <button v-if="is_followed" @click="followUser"><i class="bi bi-person-plus-fill"></i></button>
        <button v-else @click="followUser"><i class="bi bi-person-plus"></i></button>
      </div>
    </h1>
    <p>이메일 : {{userinfo?.email}}</p>
    <p>팔로워 수 : {{followers_count}} | 팔로잉 수 : {{followings_count}}</p>
    
    <hr>
    <!-- 좋아요한 영화 정보 -->
    <router-link :to="{name:'LikedView', params:{username:userinfo?.username} }"><h3>좋아요한 영화</h3></router-link>
    <p v-for="movie in like_movies" :key="movie.id">
      <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movie.id} }">{{movie.title}}</router-link>
    </p>
    <hr>
    <!-- 좋아요한 영화 워드 클라우드 -->
    <button @click="getWordCloud">워드클라우드</button>
    <div v-if="defaultWords.length">
      <wordcloud
        :data="defaultWords"
        nameKey="name"
        valueKey="value"
        :showTooltip="false"
        :wordClick="getWordCloud">
      </wordcloud>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import wordcloud from 'vue-wordcloud'

export default {
    name:'ProfileView',
    components:{
      wordcloud
    },
    computed: {
      currentUser(){
        return localStorage.getItem('username')
      },
    },
    data() {
      return {
        // 프로필 페이지 주인의 정보
        userinfo: null,
        // 팔로우 여부
        is_followed: null,
        followers_count : null,
        followings_count : null,
        like_movies: null,
        // myColors: ['#793c3c', '#E1B4B4', '#DB6E6E', '#A85454'],
        // myColors: ['#0000FF', '#0A6EFF', '#1E96FF', '#3CAEFF'],
        // myColors: ['#FF6347', '#FFA500', '#008000', '#0000FF', '#9400D3'],
        defaultWords: []
      }
    },
    methods:{
      followUser(){
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/accounts/${this.userinfo.username}/follow/`,
          headers: { 'Authorization': `Bearer ${localStorage.getItem('jwt')}` },
        })
        .then((res)=>{
          console.log('팔로우/언팔로우 누름')
          console.log(res)
          this.is_followed = res.data.is_followed
          this.followers_count = res.data.followers_count
          this.followings_count = res.data.followings_count
        })
      },
      getWordCloud(){
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/profile/${this.userinfo.username}/movies_wordcloud`,
          headers: { 'Authorization': `Bearer ${localStorage.getItem('jwt')}` },
        })
        .then((res)=> {
          this.defaultWords = res.data
        })
        .catch(()=>{
          alert('좋아요를 더 눌러주세요!')
        })
      }
    },
    created(){
      // 프로필 페이지 주인의 정보
      const username = this.$route.params.username
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile/${username}`,
        headers: { 'Authorization': `Bearer ${localStorage.getItem('jwt')}` },
      })
      .then((res) => {
        console.log('프로필 페이지 주인의 정보')
        console.log(res)
        this.userinfo = res.data
      })
      .then(()=>{
        // 팔로우 상태 보고 변수 바꾸기
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/${this.userinfo.username}/follow_check/`,
          headers: { 'Authorization': `Bearer ${localStorage.getItem('jwt')}` },
        })
         .then((res)=>{
          console.log('팔로우 여부')
          console.log(res)
          this.is_followed = res.data.is_followed
          this.followers_count = res.data.followers_count
          this.followings_count = res.data.followings_count
         })
         .catch((err) => console.log(err))
      })
      .then(()=>{
        // 좋아요한 영화 정보
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
      })
    }
}
</script>

<style>

</style>