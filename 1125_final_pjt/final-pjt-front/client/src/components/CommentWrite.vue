<template>
  <div>
    <!-- 댓글 쓰기 -->
    <form @submit.prevent="commentWrite" class="d-flex flex-row" id="comment-form">
        <label for="content"></label>
        <input type="text" id="content" v-model.trim="content" class="form-control me-2" placeholder="댓글쓰기">
        <input type="submit" value="완료" class="btn btn-outline-light">
    </form>
    <br>
    <!-- 댓글 목록
    <div v-for="comment in comment_set" :key="comment.id">
      user name:
      <router-link :to="{name:'ProfileView', params:{username:comment.user.username} }"> {{comment.user.username}}</router-link>
       -  content: {{comment.content}}
    </div> -->
    
    <table class="table table-dark table-striped table-bordered w-100" v-if="comment_set?.length" id ="comment-table">
      <thead>
      <tr>
        <th scope="col"></th>
        <th scope="col">아이디</th>
        <th scope="col">댓글 내용</th>
      </tr>
      </thead>
      <tbody v-for="(comment, index) in comment_set" :key="index">
        <tr>
          <th scope="row">{{index+1}}</th>
          <td><router-link :to="{name:'ProfileView', params:{username:comment.user.username} }"> {{comment.user.username}}</router-link></td>
          <div class="d-flex flex-row justify-content-center">
            <td>{{comment.content}}
            </td>
            <form @submit.prevent="deleteComment(comment)" v-if="comment.user.username === username">
              <button><i class="bi bi-trash"></i></button>
              <!-- <input type="submit" value="삭제" class="btn btn-outline-light" style="width:20px; height:20px"> -->
            </form>
          </div>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommentWriteView',
  props: {
    movie: Object
  },
  data(){
    return {
        content: null,
        isLogin: null,
    }
  },
  computed: {
    username(){
      return localStorage.getItem('username')
    },
    comment_set(){
      return this.movie?.comment_set
    }
  },
  methods: {
    commentWrite(){
        // 로그인 안된 상태에서 댓글쓰려고하면
        if(!this.isLogin){
          alert('로그인해주세요')
          return
        }
        const content = this.content
        // const movie_pk = this.$route.params.movie_pk
        if (!content){
          alert('내용을 입력해주세요')
          return
        }
        axios({
            method: 'post',
            url: `http://127.0.0.1:8000/movies/${this.movie.id}/comments/`,
            headers: { 'Authorization': `Bearer ${localStorage.getItem('jwt')}` },
            data: {content}
        })
         .then(() => {
            console.log(this.movie.id)
            this.$emit('changecomment')
            this.content = null
         })
    },
    deleteComment(comment){
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/comments/${comment.id}/`,
        headers: { 'Authorization': `Bearer ${localStorage.getItem('jwt')}` },
      })
      .then(()=>{
        console.log(this.movie.id)
        this.$emit('changecomment')
      })
    }
  },
  created(){
    if(localStorage.getItem('username')){
      this.isLogin = true
    } else {
      this.isLogin = false
    }
  }
}
</script>

<style>
#comment-form{
  width: 80%;
  height: 35px;
  margin: auto;
}
#comment-table {
  margin-left:auto;
  margin-right:auto;
  width: 500px;
}
th{
  text-align: center;
  vertical-align: middle!important;;
}

td{
  text-align: center;
  vertical-align: middle!important;;
}
</style>