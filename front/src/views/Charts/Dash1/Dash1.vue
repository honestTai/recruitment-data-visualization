<template>
  <v-container grid-list-lg pa-0>
    <v-layout wrap>
      <v-flex sm6 xs12 md6 lg3 v-for="item in panels" :key="item.name">
        <v-card class="ma-3">
          <v-list-item>
            <v-list-item-avatar tile class="mt-n7">
              <v-sheet :color="item.iconColor" width="43" height="45" elevation="10">
                <v-icon dark large>{{ item.icon }}</v-icon>
              </v-sheet>
            </v-list-item-avatar>
            <v-list-item-content>
              <div class="text-center text-h5">{{ item.name }}</div>
              <v-list-item-title class="headline mb-1 text-center">
<!--                {{ item.value }}-->
                <countTo :startVal='0' :endVal='item.value' :duration='3000'></countTo>
              </v-list-item-title>
              <div>
                <v-divider></v-divider>
              </div>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-flex>
      <!-- -->
      <!-- 地图单独 -->
      <!-- 地图单独 -->
      <v-flex xs12 lg12>
        <v-basic-card
            title="职位数量分布"
            toolbar-height="56"
            class="full-height-card"
        >
          <template slot="card-content">
            <data-map
                ref="dataMap"
                title=""
                :list="mapDataList"
            />
          </template>
        </v-basic-card>
      </v-flex>

      <!-- 职位省份分析与职位城市分析 -->
      <v-flex xs12 lg6>
        <v-basic-card
            title="职位城市分析"
            toolbar-height="56"
        >
          <template slot="card-content">
            <left-chart />
          </template>
        </v-basic-card>

      </v-flex>
      <v-flex xs12 lg6>
      <v-basic-card
          title="职位省份分析"
          toolbar-height="56"
          class="mt-4"
      >
        <template slot="card-content">
          <right-chart />
        </template>
      </v-basic-card>
      </v-flex>
      <!-- -->

      <!-- 第二行 -->
      <v-flex xs12 lg6>
        <v-basic-card
            title="招聘单位类型"
            toolbar-height="56"
        >
          <template slot="card-content">
            <bar-base-chart />
          </template>
        </v-basic-card>
      </v-flex>
      <v-flex
          xs12
          lg6
      >
        <v-basic-card
            title="岗位学历需求"
            toolbar-height="56"
        >
          <template slot="card-content">
            <bar-base-chart2 />
          </template>
        </v-basic-card>
      </v-flex>
      <v-flex
          xs12
          lg6
      >
        <v-basic-card
            title="求职关键词"
            toolbar-height="56"
        >
          <template slot="card-content">
            <word-cloud/>
          </template>
        </v-basic-card>
      </v-flex>
      <v-flex
          xs12
          lg6
      >
        <v-basic-card
            title="城市薪酬"
            toolbar-height="56"
        >
          <template slot="card-content">
            <dot-chart/>
          </template>
        </v-basic-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import DataMap from "@/components/DataMap";
import LeftChart from "./charts/LeftChart";
import RightChart from "./charts/RightChart"
import BarBaseChart from "../Dash1/charts/BarBaseChart";
import BarBaseChart2 from "../Dash1/charts/BarBaseChart2";
import {getCityJob, getPanel} from "../../../api/job";
import countTo from 'vue-count-to';
import DotChart from "../Dash4/DotChart.vue";
import WordCloud from "../Dash3/WordCloud.vue";

export default {
  name: "Dash1",
  components: {
    WordCloud,
    DotChart,
    DataMap, LeftChart, RightChart, BarBaseChart, BarBaseChart2,
    countTo
  },
  async mounted() {
    await getPanel().then(res => {
      // console.log(res.data.data)
      this.panels[0].value = res.data.data.data1
      this.panels[1].value = res.data.data.data2
      this.panels[2].value = res.data.data.data3
      this.panels[3].value = res.data.data.data4
    })

    await getCityJob().then(res => {
      console.log(res)
      this.mapDataList = res.data.data
    })
  },
  data: () => ({
    mapDataList: [],
    panels: [{
      'iconColor': 'indigo',
      'icon': 'movie',
      'name': '职位数',
      'value': 0
    }, {
      'iconColor': 'deep-purple',
      'icon': 'subscriptions',
      'name': '城市数',
      'value': 0
    }, {
      'iconColor': 'blue',
      'icon': 'star',
      'name': '公司数',
      'value': 0
    }, {
      'iconColor': 'teal darken-1',
      'icon': 'folder_shared',
      'name': '职位类型',
      'value': 0
    }],
  })
}
</script>

<style scoped>
.map-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.main-map-chart {
  width: 100%;
  height: 100%;
}
</style>
