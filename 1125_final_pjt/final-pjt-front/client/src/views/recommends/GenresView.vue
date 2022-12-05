<template>
  <div id="main-box">
    <h1>장르 추천</h1>
    <!-- 장르 종류 -->
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="모험">
      <label class="form-check-label" for="inlineCheckbox1">모험</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="판타지">
      <label class="form-check-label" for="inlineCheckbox2">판타지</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="애니메이션">
      <label class="form-check-label" for="inlineCheckbox3">애니메이션</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="checkbox" id="inlineCheckbox4" value="공포">
      <label class="form-check-label" for="inlineCheckbox4">공포</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="checkbox" id="inlineCheckbox5" value="액션">
      <label class="form-check-label" for="inlineCheckbox5">액션</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="checkbox" id="inlineCheckbox6" value="코미디">
      <label class="form-check-label" for="inlineCheckbox6">코미디</label>
    </div>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="checkbox" id="inlineCheckbox7" value="로맨스">
      <label class="form-check-label" for="inlineCheckbox7">로맨스</label>
    </div>
    <button @click="searchGenre"> 검색하기 </button>

    <div v-if="matchingMovie?.length" style="height:115vh;">
      <GenreItem style="float:left; margin:10px;" v-for="movie in matchingMovie" :key="movie.id" :movie='movie'/>
    </div>

  </div>
  <!-- 장르: 모험 판타지 애니메이션 드라마 공포 액션 코미디 역사 서부 스릴러 범죄 다큐멘터리 SF 미스터리 음악 로맨스 가족 전쟁 TV영화 -->
</template>

<script>
import _ from 'lodash'
import GenreItem from '@/components/GenreItem'

export default {
    name:"GenresView",
    components: {GenreItem},
    data(){
      return {
        matchingMovie: null,
        genres: ['모험', '판타지', '애니메이션', '공포', '액션', '코미디', '로맨스']
      }
    },
    computed:{
      movieList(){
        return this.$store.state.movieList
      }
    },
    methods:{
      searchGenre(){
        // 태그들에서 체크된 경우의 장르이름만 가져오기
        const checkTags = document.querySelectorAll('.form-check-input')
        const checkGenres = []
        checkTags.forEach((checkTag)=>{
        if(checkTag.checked){
          checkGenres.push(checkTag.value)
        }
       })
        console.log(checkGenres)

        const matchingGenre = _.sampleSize(this.movieList?.filter((movie)=>{
          if (movie.genre_ids.some((genre)=>checkGenres.includes(genre.name))){
            return movie
          }
        }), 10)

        console.log(matchingGenre)
        this.matchingMovie = matchingGenre
      }
    }
}
</script>

<style>

</style>