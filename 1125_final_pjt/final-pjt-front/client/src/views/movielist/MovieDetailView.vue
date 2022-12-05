<template>
<div class="pb-1" id="main-box">
  <div class="container text-center mb-5 text-bg-dark">
    <h1>{{movie?.title}}        
        <!-- 영화 좋아요 -->
        <button v-if="is_liked" @click="likeMovie"><i class="bi bi-heart-fill" id="heart-fill"></i></button>
        <button v-if="!is_liked" @click="likeMovie"><i class="bi bi-heart" id="heart"></i></button>
    </h1>
    <!-- :style=" {backgroundImage: `url(https://image.tmdb.org/t/p/w500/${movie?.backdrop_path})`}"  -->
    <div class="row text-bg-dark" id="detail-box">
      <div class="col">
      <img id="detail-img" :src="'https://image.tmdb.org/t/p/w500' + movie?.poster_path" class="detail" alt="" style="height:100%" >
      </div>

      <div class="col">
        <!-- <h2>제목 : {{movie?.title}}</h2> -->
        <!-- <p> {{movie?.genre_ids}}</p> -->
        <!-- <p v-for="movie_name, index in movie?.genre_ids" :key="index">{{movie_name.name}}</p> -->
        <div class="d-flex">평점 : {{movie?.vote_average}}</div>
        <div class="d-flex">
          장르 : &nbsp;
          <div class="d-flex">
            <div v-for="(genre, index) in movie?.genre_ids" :key="index" class="card-text">
              <span>{{genre.name}}&nbsp;&nbsp;</span>
            </div>
          </div>
        </div>
        <br>
        <div>{{movie?.overview}}</div>
        <br>
        <CommentWrite :movie="movie" @changecomment="ChangeComment"/>
        <!-- <div v-for="comment in movie?.comment_set" :key="comment.id">{{comment.content}}</div> -->
      </div>
    </div>
    </div>
  </div>
</template>

<script>
import CommentWrite from '@/components/CommentWrite.vue';
import axios from 'axios'

export default {
    name:'MovieDetailView',
    components: {
      CommentWrite
    },
    data() {
        return{
            movie: null,
            movie_pk: this.$route.params.movie_pk,
            is_liked: null,
        }
    },
    methods: {
      likeMovie(){
        axios({
          method:'post',
          url: `http://127.0.0.1:8000/movies/${this.movie_pk}/likes/`,
          headers: { 'Authorization': `Bearer ${localStorage.getItem('jwt')}` },
        })
        .then((res)=>{
          console.log(res)
          this.is_liked = res.data.is_liked
        })
      },
      getMovieInfo(){
        // 영화 정보
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/${this.movie_pk}`
        })
        .then((res)=>{
          this.movie = res.data
          console.log(res)
        })
        .then(()=>{
          this.getUserInfo()
        })
      },
      getUserInfo(){
        // 유저 정보(id 필요) - 좋아요 눌렀는지 확인하기
        const username = localStorage.getItem('username')
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/profile/${username}`
        })
        .then((res) => {
          console.log('유저 정보')
          console.log(res.data.id)
          if (this.movie?.like_users.includes(res.data.id)){
            this.is_liked = true
          } else {
            this.is_liked = false
          }
        })
      },
      ChangeComment(){
        this.getMovieInfo()
      }
    },
    created(){
      this.getMovieInfo()
      // this.getUserInfo()
    }
}
</script>

<style>
.detail{
  height: 90%;
  width: 90%;
  border-radius: 10px;
}
#heart-fill{
  color: red;
}
button {
  background-color: transparent;
  border: none;
  color: white
}
#detail-img:hover {
  transform: none;
}
</style>