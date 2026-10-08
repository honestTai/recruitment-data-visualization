<template>
  <div class="home">
    <v-row>
      <v-col md="3" cols="12">
        <v-text-field
          v-model="keyword"
          label="搜索职位"
          outlined
          dense
          clearable
          @input="handleSearch"
        />
      </v-col>
      <v-btn color="primary" class="mt-4" @click="getData">
        爬取数据
      </v-btn>
    </v-row>

    <v-row>
      <v-col cols="12" md="3" sm="6"
             v-for="(item, index) in paginatedItems" :key="index">
        <job-card :item="item"/>
      </v-col>
    </v-row>
    <v-row justify="center" class="mt-4">
      <v-pagination
          v-model="currentPage"
          :length="totalPages"
          :total-visible="5"
          @input="fetchData"
      />
    </v-row>
    <v-row justify="center" class="mt-2">
      <div>当前页：{{ currentPage }} / 总页数：{{ totalPages }}</div>
    </v-row>
  </div>
</template>

<script>
import JobCard from "../components/JobCard";
import {fetchJobData, get} from "../api/job";

export default {
  components: { JobCard },
  name: "Home",
  data: () => ({
    items: [],
    currentPage: 1,
    itemsPerPage: 10,
    totalItems: 0,
    keyword: "", // 搜索关键词
  }),
  computed: {
    totalPages() {
      return Math.ceil(this.totalItems / this.itemsPerPage);
    },
    paginatedItems() {
      return this.items;
    },
  },
  async mounted() {
    await this.fetchData();
  },
  methods: {
    async fetchData() {
      const params = {
        page: this.currentPage,
        pageSize: this.itemsPerPage,
      };
      if (this.keyword) {
        params.keyword = this.keyword; // 如果 keyword 有值，添加到参数中
      }
      await get(params).then((res) => {
        this.items = res.data.data.items;
        this.totalItems = res.data.data.total;
      });
    },
    handleSearch() {
      this.currentPage = 1; // 重置到第一页
      this.fetchData(); // 重新获取数据
    },
    async getData() {
      console.log("开始爬取数据...");
      await fetchJobData().then(res => {
        console.log("爬取完成:", res.data);
        this.$snackbar({content: '数据爬取中', top:true, center:true, color:'green',multiLine: true})
        // this.$Message.success("数据爬取成功！");
      }).catch(err => {
        console.error("爬取失败:", err);
        this.$snackbar({content: '数据爬取失败！', top:true, center:true, color:'green',multiLine: true})
        // this.$Message.error("数据爬取失败！");
      });
    },
  },
};
</script>

<style scoped>
</style>