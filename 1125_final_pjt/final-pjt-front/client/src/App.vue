<template>
  <div id="app" class="text-bg-dark">
    <header class="px-3 py-2 text-bg-dark fixed-top">
      <div class="d-flex flex-row justify-content-between">
        <div>
          <ul class="nav">
            <li class="nav-item">
              <router-link to="/" class="nav-link active">
                <img
                  src="./assets/y_y.png"
                  width="70"
                  height="48"
                  style="object-fit: cover"
                />
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                to="/"
                class="nav-link active"
                style="color: white; margin-top: 7px"
                >Home</router-link
              >
            </li>
            <li class="nav-item" v-show="isLogin">
              <router-link
                :to="{ name: 'LikedView', params: { username: username } }"
                class="nav-link active"
                style="color: white; margin-top: 7px"
                >Liked</router-link
              >
            </li>
            <li>
              <div class="dropdown">
                <div
                  class="btn btn-dark dropdown-toggle"
                  type="button"
                  data-bs-toggle="dropdown"
                  style="margin-top: 7.5px"
                >
                  Recommend
                </div>
                <ul class="dropdown-menu dropdown-menu-dark">
                  <router-link
                    :to="{
                      name: 'VoteavgView',
                    }"
                    ><li><a class="dropdown-item">평점</a></li></router-link
                  >
                  <router-link :to="{ name: 'RandomView' }"
                    ><li><a class="dropdown-item">랜덤</a></li></router-link
                  >
                  <router-link
                    :to="{
                      name: 'ClassicListView',
                    }"
                    ><li><a class="dropdown-item">클래식</a></li></router-link
                  >
                  <router-link :to="{ name: 'GenresView' }"
                    ><li><a class="dropdown-item">장르</a></li></router-link
                  >
                </ul>
              </div>
            </li>
          </ul>
        </div>
        <div>
          <ul class="nav">
            <li>
              <form @submit.prevent="searchMovie" class="d-flex flex-row">
                <input
                  class="form-control me-2"
                  id="search"
                  type="search"
                  aria-label="Search"
                  placeholder="검색할 내용을 입력하세요"
                  style="margin-top: 8px"
                />
                <input
                  class="btn btn-outline-light"
                  type="submit"
                  value="검색"
                  style="margin-top: 8px"
                />
              </form>
            </li>
            <li v-show="!isLogin">
              <router-link
                :to="{ name: 'LoginView' }"
                class="nav-link"
                style="color: white; margin-top: 7px"
                >Login</router-link
              >
            </li>
            <li v-show="!isLogin">
              <router-link
                :to="{ name: 'SignupView' }"
                @click.native="Logout"
                class="nav-link"
                style="color: white; margin-top: 7px"
                >Sign-up</router-link
              >
            </li>
            <li v-show="isLogin">
              <router-link
                :to="{ name: 'LoginView' }"
                @click.native="Logout"
                class="nav-link"
                style="color: white; margin-top: 7px"
                >Logout</router-link
              >
            </li>
            <li v-show="isLogin">
              <router-link
                :to="{
                  name: 'ProfileView',
                  params: { username: username },
                }"
                class="nav-link"
                style="color: white; margin-top: 7px"
                >Profile</router-link
              >
            </li>
          </ul>
        </div>
      </div>
    </header>
    <router-view @login="Login" :key="$route.fullPath" class="space" />
    <div
      id="carouselExampleIndicators"
      class="carousel slide"
      data-bs-ride="true"
    ></div>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
  computed: {
    username() {
      return localStorage.getItem("username");
    },
  },
  data() {
    return {
      isLogin: false,
      search_movie: null,
    };
  },
  methods: {
    Login() {
      this.isLogin = true;
    },
    Logout() {
      localStorage.removeItem("jwt"),
        localStorage.removeItem("username"),
        (this.isLogin = false);
    },
    searchMovie() {
      const inputTag = document.querySelector("#search");
      console.log(inputTag.value);
      if (inputTag.value === "") {
        alert("키워드를 입력하세요");
        return;
      }
      this.$router.push({
        name: "SearchView",
        params: { keyword: inputTag.value },
      });
      inputTag.value = null;
    },
  },
  created() {
    if (localStorage.getItem("jwt")) {
      this.isLogin = true;
    } else {
      this.isLogin = false;
    }

    this.$store.commit("GET_MOVIE_LIST");
  },
};
</script>

<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: "Jua", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
header {
  margin-bottom: 0px;
}
.space {
  margin-top: 15px;
  padding-top: 50px;
  height: 350vh;
}

img:hover {
  transform: scale(1.1);
  transition: all 0.2s linear;
}

#main-box {
  padding-top: 70px;
}
</style>
