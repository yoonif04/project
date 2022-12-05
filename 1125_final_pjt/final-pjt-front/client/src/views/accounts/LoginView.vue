<template>
  <div class="text-bg-light" id="main-box">
    <div class="container">
      <main class="form-signin w-100 m-auto">
        <form @submit.prevent="login">
          <img id="login-img" class="mb-4" src="@/assets/Y & Y (1).png" alt="image" width="72" height="57" />
          <h1 class="h3 mb-3 fw-normal">로그인</h1>

          <div class="form-floating">
            <input
              type="name"
              class="form-control"
              id="floatingInput"
              placeholder="name@example.com"
              v-model="username"
            />
            <label for="floatingInput">name</label>
          </div>
          <div class="form-floating">
            <input
              type="password"
              class="form-control"
              id="floatingPassword"
              placeholder="Password"
              v-model="password"
            />
            <label for="floatingPassword">Password</label>
          </div>

          <div class="checkbox mb-3">
            <label>
              <input type="checkbox" value="remember-me" id="check-remember"/> Remember ID
            </label>
          </div>
          <button class="w-100 btn btn-lg btn-primary" type="submit">
            Sign in
          </button>
          <p class="mt-5 mb-3 text-muted">
            &copy; y&y movie<br />
          </p>
        </form>
      </main>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginView",
  data: function () {
    return {
      username: null,
      password: null,
    };
  },
  methods: {
    login: function () {
      const username = this.username;
      const password = this.password;

      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/token/",
        data: { username, password },
      })
        .then((res) => {
          console.log(res);
          const token = res.data.access;
          localStorage.setItem("jwt", token);
          this.$router.push({ name: "HomeView" });
          this.$emit("login");
          // 유저 이름도 저장
          localStorage.setItem("username", res.data.username);
        })
        .catch(() => {
          alert("다시 입력하세요");
        });

        // remember me 체크 확인 후 
        const rememberTag = document.querySelector('#check-remember')
        console.log(rememberTag.checked)
        if (rememberTag.checked){
          localStorage.setItem('check_username', username)
        } else {
          localStorage.removeItem('check_username')
        }
    },
  },
  mounted(){
    console.log(localStorage.getItem('check_username'))
    // 저장해둔 유저이름이 존재한다면
    if(localStorage.getItem('check_username')){
      this.username = localStorage.getItem('check_username')
      this.isChecked = true
      document.querySelector('#check-remember').checked = true
    } else {
      document.querySelector('#check-remember').checked = false
    }
    console.log(this.isChecked)
  }
};
</script>

<style scoped>
.container {
  width: 300px;
}
#login-img {
  width: 80px;
  height: 80px;
  margin-top: 20px;
  margin-bottom: 0px;
  padding-bottom: 0px;
}
#login-img:hover {
  transform: none;
}
</style>
