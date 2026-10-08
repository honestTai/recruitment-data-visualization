<template>
  <div class="home">
    <div class="white--text font-weight-bold text-h5 d-flex justify-start my-6">
      {{ titles[2] }}
    </div>
    <v-row>
      <v-col cols="12" md="3">
        <v-text-field
            v-model="searchKeyword"
            label="搜索职位"
            outlined
            dense
            clearable
        />
      </v-col>

    </v-row>
    <v-row>
      <v-col cols="12" md="3" sm="6"
             v-for="(item, index) in recs2" :key="index">
        <job-card :item="item"/>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import JobCard from "../components/JobCard";
import { getHot, getUserCF, fetchJobData } from "../api/job"; // 假设 fetchJobData 是爬取数据的 API
import mixin from '../mixins/mixins';

export default {
  mixins: [mixin],
  components: { JobCard },
  name: "Home",
  data: () => ({
    titles: ["最新职位", "热门推荐", "为您推荐"],
    items: [],
    recs: [],
    recs2: [],
    searchKeyword: "", // 搜索关键词
  }),
  async mounted() {
    console.log('当前登录uid:' + this.uid);
    await getHot().then(res => {
      this.items = res.data.data;
      console.log(this.items);
    });
    await getUserCF(this.uid).then(res => {
      this.recs2 = res.data.data.datas;
    });
  },
  methods: {
    async fetchData() {
      console.log("开始爬取数据...");
      await fetchJobData().then(res => {
        console.log("爬取完成:", res.data);
        this.$toast.success("数据爬取成功！");
      }).catch(err => {
        console.error("爬取失败:", err);
        this.$toast.error("数据爬取失败！");
      });
    },
  },
};
</script>

<style scoped>
</style>