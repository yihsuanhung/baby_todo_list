import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Todov4 from "../views/Todov4.vue"; // import name可以自己取 但最好跟檔名一樣
import Todo from "../views/Todo.vue"; // import name可以自己取 但最好跟檔名一樣
import Daniel from "../views/Daniel.vue";

Vue.use(VueRouter);

const routes = [
  {
    //第一種import方式，把要import的東西寫在頭
    path: "/",
    name: "Home",
    component: Home
  },
  {
    //第二種import方式，把要import的東西寫在裡面
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/todov4", //自己取，都小寫
    name: "Todov4", //自己取，最好跟檔名一樣
    component: Todov4 // 上面import的名字叫什麼 這邊就要打什麼
  },
  {
    path: "/todo", //自己取，都小寫
    name: "Todo", //自己取，最好跟檔名一樣
    component: Todo // 上面import的名字叫什麼 這邊就要打什麼
  },
  {
    path: "/daniel", //自己取，都小寫
    name: "Daniel", //自己取，最好跟檔名一樣
    component: Daniel // 上面import的名字叫什麼 這邊就要打什麼
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
