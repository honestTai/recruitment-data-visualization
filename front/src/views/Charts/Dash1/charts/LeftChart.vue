<template>
  <div class="chart-container">
    <v-chart
        class="chart"
        :options="chartOption"
        autoresize
    />
  </div>
</template>

<script>
import { getCityJob2 } from "../../../../api/job";

export default {
  name: "BaseLineChart",
  data() {
    return {
      chartOption: {},
      datas: [],
      labels: [],
      data: [],
    };
  },
  async mounted() {
    await getCityJob2().then((res) => {
      this.datas = res.data.data.map((i) => i.value);
      this.labels = res.data.data.map((i) => i.name);
      this.data = res.data.data;
      console.log(this.data);
    });
    this.chartOption = this.buildChartOption();
  },
  methods: {
    buildChartOption() {
      const option = {
        grid: {
          left: "2%",
          right: "2%",
          top: "10%",
          bottom: "10%",
          containLabel: true,
        },
        xAxis: {
          type: "category",
          data: this.labels,
          axisLabel: {
            interval: 0,
            rotate: 40,
          },
          axisLine: {
            lineStyle: {
              color: "#78909C",
            },
          },
        },
        yAxis: {
          type: "value",
          axisLine: {
            lineStyle: {
              color: "#78909C",
            },
          },
        },
        series: [
          {
            name: "所有类型",
            data: this.datas,
            type: "line",
            smooth: true,
            itemStyle: {
              color: "#B388FF",
            },
          },
        ],
      };
      return option;
    },
  },
};
</script>

<style scoped>
.chart-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 500px; /* 拉高图表 */
  width: 100%;
}

.chart {
  width: 80%; /* 图表宽度 */
  height: 100%; /* 图表高度 */
}
</style>