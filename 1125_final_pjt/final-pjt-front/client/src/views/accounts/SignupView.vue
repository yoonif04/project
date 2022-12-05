<template>
  <div class="text-bg-light" id="main-box">
    <div class="container">
      <main class="form-signin w-100 m-auto">
        <form @submit.prevent="signup">
          <img id="signup-img" class="mb-4" src="@/assets/Y & Y (1).png" alt="image" width="72" height="57" />
          <h1 class="h3 mb-3 fw-normal">회원가입</h1>

          <div class="form-floating">
            <input
              type="name"
              class="form-control"
              placeholder="name"
              v-model.trim="username"
              @input="checkDuplicated"
            />
            <label for="floatingInput">username</label>
            <div
              v-if="isDuplicated_username"
              :class="{ 'text-red': isDuplicated_username }"
            >
              <p>이미 사용중인 아이디입니다.</p>
            </div>
            <div
              v-else-if="!isDuplicated_username && username"
              :class="{ 'text-green': !isDuplicated_username }"
            >
              <p>사용 가능한 아이디입니다.</p>
            </div>
          </div>

          <div class="form-floating">
            <input
              type="password"
              class="form-control"
              placeholder="Password"
              v-model="password1"
            />
            <label for="floatingPassword">Password</label>
          </div>

          <div class="form-floating">
            <input
              type="password"
              class="form-control"
              placeholder="Password"
              v-model="password2"
            />
            <label for="floatingPassword">password confirm</label>
          </div>

          <div class="form-floating">
            <input
              type="email"
              class="form-control"
              placeholder="name@example.com"
              v-model.trim="email"
              @input="checkDuplicated"
            />
            <label for="floatingPassword">Email</label>
            <div
              v-if="isDuplicated_email"
              :class="{ 'text-red': isDuplicated_email }"
            >
              <p>이미 사용중인 이메일입니다.</p>
            </div>
            <div
              v-else-if="!isDuplicated_email && email"
              :class="{ 'text-green': !isDuplicated_email }"
            >
              <p>사용 가능한 이메일입니다.</p>
            </div>
          </div>

          <!-- <div class="checkbox mb-3">
            <label>
              <input type="checkbox" value="remember-me" /> Remember me
            </label>
          </div> -->
          <button class="w-100 btn btn-lg btn-primary" type="submit">
            Sign up
          </button>
          <p class="mt-5 mb-3 text-muted">&copy; y&y movie</p>
        </form>
      </main>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SingupView",
  data: function () {
    return {
      username: null,
      password1: null,
      password2: null,
      email: null,
      isDuplicated_username: false,
      isDuplicated_email: false,
      isPossible: false,
    };
  },
  methods: {
    checkDuplicated() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/accounts/user_list/",
      }).then((res) => {
        const usernames = res.data.map((user) => user.username);
        const emails = res.data.map((user) => user.email);
        console.log(usernames, emails);
        if (this.username && usernames.includes(this.username)) {
          this.isDuplicated_username = true;
        } else {
          this.isDuplicated_username = false;
        }

        if (this.email && emails.includes(this.email)) {
          this.isDuplicated_email = true;
        } else {
          this.isDuplicated_email = false;
        }

        if (this.isDuplicated_username | this.isDuplicated_email) {
          return;
        }
        this.isPossible = true;
      });
    },
    signup: function () {
      const username = this.username;
      const password = this.password1;
      const passwordConfirm = this.password2;
      const email = this.email;

      if (!this.isPossible) {
        alert("다시 입력하세요");
        return;
      }

      axios({
        method: "POST",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: { username, password, passwordConfirm, email },
      })
        .then(() => {
          this.$router.push({ name: "LoginView" });
        })
        .catch(() => {
          alert("다시 입력하세요");
        });
    },
  },
};
</script>

<style scoped>
.container {
  width: 300px;
}
.text-red {
  color: red;
}
.text-green {
  color: green;
}
#signup-img {
  width: 80px;
  height: 80px;
  margin-top: 20px;
  margin-bottom: 0px;
  padding-bottom: 0px;
}
#signup-img:hover {
  transform: none;
}
</style>

