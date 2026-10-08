<template>
  <v-card
      :loading="loading"
      class="mx-auto my-12"
      max-width="374"
  >
    <template slot="progress">
      <v-progress-linear
          color="light-green"
          height="10"
          indeterminate
      ></v-progress-linear>
    </template>

    <v-img
        height="330"
        :src="doubanImg(item.company_logo)"
    ></v-img>

    <v-card-title>{{item.position_name}}
      <span class="ml-3" style="font-size: 2px;"></span>
    </v-card-title>

    <v-card-text>
      <v-row
          align="center"
          class="mx-0"
      >
        <div class="grey--text ms-4">
          企业： {{item.company_name}} · {{item.city}}
        </div>
        <div class="grey--text ms-4">
          薪酬： {{item.salary0}} - {{item.salary1}}元
        </div>
        <div class="grey--text ms-4">
          企业性质：{{item.coattr}}·{{item.nation}}
        </div>
        <div class="grey--text ms-4">
          学历要求：{{item.degree}}
        </div>
        <div class="grey--text ms-4">
          公司规模：{{item.cosize0}} - {{item.cosize1}}
        </div>
      </v-row>

      <div>{{item.intro}}</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>公司福利</v-card-title>

    <v-card-text>
      <v-chip-group
          v-model="selection"
          active-class="deep-purple accent-4 white--text"
          column
      >
        <div v-if="item.welfare == null">
          <v-chip>暂无福利</v-chip>
        </div>
        <div v-else>
          <v-chip v-for="(i,idx) in item.welfare.split(',')" :key="idx">{{i}}</v-chip>
        </div>
<!--        <v-chip v-for="(i,idx) in item.welfare.split(',')" :key="idx">{{i}}</v-chip>-->
      </v-chip-group>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>您的评分</v-card-title>

    <v-card-text>
      <v-row align="center" justify="center">
        <v-rating
            v-model="userRating"
            color="amber"
            half-increments
            size="24"
            @input="submitRating"
        ></v-rating>
        <div class="ms-3">您的评分：{{ userRating }}</div>
      </v-row>
    </v-card-text>

    <v-card-actions>
      <v-btn
          color="deep-purple lighten-2"
          text
          @click="reserve(item.company_url)">
        公司详情
      </v-btn>
      <v-btn
          color="deep-purple accent-2"
          text
          @click="reserve(item.url)">
        职位详情
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import {getRating, submitRatingAPI} from "../api/job"; // 假设接口定义在 job.js 中

export default {
  name: "job-card",
  props: {
    item: Object,
    cardTitle: String,
  },
  data: () => ({
    loading: false,
    selection: -1,
    userRating: 0, // 用户评分
  }),
  async mounted() {
    await this.fetchUserRating();
  },
  methods: {
    async fetchUserRating() {
      try {
        const response = await getRating({
          jobId: this.item.id, // 职位主键
          userId: localStorage.getItem("uid"), // 用户主键
        });
        console.log(response)
        this.userRating = response.data.data.score || 0; // 设置评分，默认为 0
      } catch (error) {
        console.error("获取用户评分失败：", error);
      }
    },
    doubanImg(src) {
      let trueSrc = "";
      if (src != null && src.startsWith("http://localhost:8080"))
        trueSrc = src;
      else if (src != null && src != "")
        trueSrc = "https://images.weserv.nl/?url=" + src;
      else trueSrc = require("@/assets/nologo.png");
      return trueSrc;
    },
    reserve(url) {
      this.loading = true;
      setTimeout(() => {
        this.loading = false;
        window.open(url);
      }, 2000);
    },
    submitRating(rating) {
      // 调用接口提交评分
      submitRatingAPI({
        jobId: this.item.id, // 职位主键
        userId: localStorage.getItem("uid"), // 用户主键
        rating: rating, // 用户评分
      })
          .then((response) => {
            console.log("评分提交成功：", response.data);
            this.$snackbar({
              content: "评分提交成功！",
              top: true,
              center: true,
              color: "green",
              multiLine: true,
            });
            this.fetchUserRating()
          })
          .catch((error) => {
            console.error("评分提交失败：", error);
            this.$snackbar({
              content: "评分提交失败，请稍后重试。",
              top: true,
              center: true,
              color: "red",
              multiLine: true,
            });
          });
    },
  },
};
</script>

<style scoped>
</style>