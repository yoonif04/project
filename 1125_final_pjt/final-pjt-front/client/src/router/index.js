import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/movielist/HomeView'
import MovieDetailView from '@/views/movielist/MovieDetailView'
import LikedView from '@/views/movielist/LikedView'
import SearchView from '@/views/movielist/SearchView'

import LoginView from '@/views/accounts/LoginView'
import SignupView from '@/views/accounts/SignupView'
import ProfileView from '@/views/accounts/ProfileView'

import RandomView from '@/views/recommends/RandomView'
import GenresView from '@/views/recommends/GenresView'
import ClassicListView from '@/views/recommends/ClassicListView'
import VoteavgView from '@/views/recommends/VoteavgView'

import NotFound404 from '@/views/NotFound404'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
    {
    path: '/accounts/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/accounts/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/accounts/profile/:username',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/movies/likedmovie/:username',
    name: 'LikedView',
    component: LikedView
  },
  {
    path: '/movies/search/:keyword',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/movies/random',
    name: 'RandomView',
    component: RandomView
  },
  {
    path: '/movies/genres',
    name: 'GenresView',
    component: GenresView
  },
  {
    path: '/movies/classiclist',
    name: 'ClassicListView',
    component: ClassicListView
  },
  {
    path: '/movies/voteavg',
    name: 'VoteavgView',
    component: VoteavgView
  },
  {
    path: '/movies/:movie_pk',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  }
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
