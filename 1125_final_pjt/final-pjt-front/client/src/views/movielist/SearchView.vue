<template>
  <div>
    <h1>
      <b class="fst-italic">{{ keyword }}&nbsp;&nbsp;</b>검색 결과
    </h1>
    <div class="container search_card" style="margin: auto;">
    <div v-if="matchingMovie?.length" class="card text-bg-dark d-flex" style="max-width: 80%;">
        <div v-for="movie in matchingMovie" :key="movie.id">
          <div class="card mb-3" style="max-width: 100%; heigth: 100%;">
            <div class="row g-0">
              <div class="col-md-4">
                <router-link :to="{name: 'MovieDetailView', params: {movie_pk: movie.id} }">
                  <img
                    :src="'https://image.tmdb.org/t/p/w500' + movie?.poster_path"
                    class="img-fluid rounded-start"
                    alt="..."
                  />
                </router-link>
              </div>
                <div class="col-md-8 bg-dark">
                  <div class="card-body text-align-around">
                    <h3 class="card-title">{{ movie.title }}</h3><br>
                    <p class="card-text">{{movie.overview}}</p><br>
                    <div class="d-flex">
                      <div v-for="(genre, index) in movie.genre_ids" :key="index" class="card-text">
                        <span>{{genre.name}}&nbsp;&nbsp;</span>
                      </div>
                    </div>
                  </div>
                </div>
            </div>
          </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  name: "SearchView",
  data() {
    return {
      matchingMovie: null,
    };
  },
  computed: {
    keyword() {
      return this.$route.params.keyword;
    },
    movieList() {
      return this.$store.state.movieList;
    },
  },
  created() {
    const keyword = this.$route.params.keyword;
    const movieList = this.movieList;
    const matching = movieList?.filter((movie) => {
      if (movie.title.includes(keyword) || movie.overview.includes(keyword)) {
        return movie;
      }
    });
    this.matchingMovie = matching;
  },
};
</script>

<style>
.search_card{
  justify-content: center;
}
</style>