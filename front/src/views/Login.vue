<template>
  <v-app>
  <v-container>60
    <v-row align="center" justify="center" class="mt-8">
      <v-col class="loginContainer" cols="12" sm="10">
        <v-card class="elevation-6 mt-10">
          <v-window v-model="step">
            <v-window-item :value="1">
              <v-row>
                <v-col cols="12" md="6">
                  <v-card-text class="mt-12">
                    <h1 class="text-center">
                      <svg-icon color="lightblue"  :icon-class="appIcon" />
                      招聘数据可视化系统
                    </h1>
                    <v-row align="center" justify="center">
                      <v-col cols="12" sm="8">
                        <v-text-field
                            label="用户名"
                            outlined
                            dense
                            color="blue"
                            autocomplete="false"
                            class="mt-16"
                            v-model="username"
                        />
                        <v-text-field
                            label="密码"
                            outlined
                            dense
                            color="blue"
                            autocomplete="false"
                            type="password"
                            v-model="password"

                        />
                        <v-row>
                          <v-col cols="12" sm="7">
                            <v-checkbox

                                label="记住我"
                                class="mt-n1"
                                color="blue"
                            ></v-checkbox>
                          </v-col>
                        </v-row>
                        <v-btn color="blue" dark block tile @click="login()">登录</v-btn>


                      </v-col>
                    </v-row>
                  </v-card-text>
                </v-col>
                <v-col cols="12" md="6" class="blue rounded-bl-xl">
                  <div style="  text-align: center; padding: 180px 0;">
                    <v-card-text class="white--text">
                      <h2 class="text-center ">还没账号啊?</h2>
                      <h4
                          class="text-center"
                      >Let's 先注册一个<br> 点击下方</h4>
                    </v-card-text>
                    <div class="text-center">
                      <v-btn tile outlined dark @click="step++">注册</v-btn>
                    </div>
                  </div>
                </v-col>
              </v-row>
            </v-window-item>
            <v-window-item :value="2">
              <v-row>
                <v-col cols="12" md="6" class="blue rounded-br-xl">
                  <div style="  text-align: center; padding: 180px 0;">
                    <v-card-text class="white--text">
                      <h3 class="text-center ">已注册?</h3>
                      <h6
                          class="text-center"
                      >回到登录页面<br> 点击下方</h6>
                    </v-card-text>
                    <div class="text-center">
                      <v-btn tile outlined dark @click="step--;">登录</v-btn>
                    </div>
                  </div>
                </v-col>

                <v-col cols="12" md="6">
                  <v-card-text class="mt-12">
                    <h1
                        class="text-center"
                    >注册一个账号</h1>
                    <v-row align="center" justify="center">
                      <v-col cols="12" sm="8">
                        <v-text-field
                                label="昵称"
                                outlined
                                dense
                                color="blue"
                                autocomplete="false"
                                class="mt-4"
                                v-model="realname"
                        />
                        <v-text-field
                            label="用户名"
                            outlined
                            dense
                            color="blue"
                            autocomplete="false"
                            v-model="username"
                        />
                        <v-text-field
                            label="密码"
                            outlined
                            dense
                            color="blue"
                            autocomplete="false"
                            type="password"
                            v-model="password"
                        />
                        <v-row>
                          <v-col cols="12" sm="7">
                            <v-checkbox

                                label="同意"
                                class="mt-n1"
                                color="blue"
                            ></v-checkbox>
                          </v-col>
                        </v-row>
                        <v-btn color="blue" dark block tile @click="register()">注册</v-btn>


                      </v-col>
                    </v-row>
                  </v-card-text>
                </v-col>
              </v-row>
            </v-window-item>
          </v-window>
        </v-card>
      </v-col>

      <div class="videoContain">
        <video loop v-if="showVideo" muted ref="my_video" preload="metadata" class="videoStyle"
               v-on:canplay="canplay">
          <source
              src="../assets/video/login.mp4"
              type="video/mp4"/>
        </video>
      </div>
    </v-row>
  </v-container>
  </v-app>
</template>

<script>

import {login, register} from "../api/user";
import mixin from '../mixins/mixins'

export default {
  mixins: [mixin],
  data: () => ({
    step: 1,
    vedioCanPlay: false,
    showVideo: true,
    username: '',
    password: '',
    realname: '',
  }),
  props: {
    source: String
  },
  mounted: function () {
    let $ = this;
    let myVid = $.$refs.my_video;
    setTimeout(function () {
      myVid.play();
    }, 150);
    myVid.ontimeupdate = function () {
      if (this.currentTime > 15) {
        $.dark = true;
        $.alertType = 'error';
        $.cardBackground = 'background-color: rgba(0,121,255,0.2);';
      } else {
        $.dark = false;
        $.alertType = 'warning';
        $.cardBackground = 'background-color: rgba(0,121,255,0.04);';
      }
    };

  },
  methods: {
    canplay() {
      this.vedioCanPlay = true
    },
    login() {
      if(this.username == "" || this.password == ""){
        this.$snackbar({content: '表单数据未填写完整', top:true, center:true, color:'red',multiLine: true})
        return false
      }

      const loginForm = {"username": this.username, "password": this.password}
      login(loginForm).then(res=>{
        const {data} = res
        if(data.code != 0)
          this.$snackbar({content: data.msg, top:true, center:true, color:'red',multiLine: true})
        else {
          // localStorage.setItem('uid', data.data)
          this.$store.dispatch('setUserInfo', data.data)
          this.$snackbar({content: '登录成功', top:true, center:true, color:'green',multiLine: true})
          this.$router.push('/home')
        }
      })
    },
    register(){
      if(this.username == "" || this.password == "" || this.realname == ""){
        this.$snackbar({content: '表单数据未填写完整', top:true, center:true, color:'red',multiLine: true})
        return false
      }

      const registForm = {"username": this.username, "password": this.password, "realname": this.realname}
      register(registForm).then(res=>{
        const {data} = res
        if(data.code != 0)
          this.$snackbar({content: data.msg, top:true, center:true, color:'red',multiLine: true})
        else {
          this.$snackbar({content: '注册成功', top:true, center:true, color:'green',multiLine: true})
        }
      })
    }
  }


}
</script>
<style scoped>
.v-application .rounded-bl-xl {
  border-bottom-left-radius: 300px !important;
}

.v-application .rounded-br-xl {
  border-bottom-right-radius: 300px !important;
}
</style>
<style lang="stylus">
.loginContainer
  z-index :1;

.videoContain
  display: inline;
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  z-index: 0;

  .videoStyle
    object-fit: fill;
    width: 100%;
    height: 100%;
</style>
