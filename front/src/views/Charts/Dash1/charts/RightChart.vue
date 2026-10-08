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
import { getCityJob } from "../../../../api/job";

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
    await getCityJob().then((res) => {
      this.datas = res.data.data.map((i) => i.value);
      this.labels = res.data.data.map((i) => i.name);
      this.data = res.data.data;
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
            name: "职位数",
            data: this.datas,
            barWidth: "35%",
            type: "bar",
            smooth: true,
            itemStyle: {
              color: function (params) {
                const colorList = [
                  "#F3E5F5",
                  "#E1BEE7",
                  "#CE93D8",
                  "#BA68C8",
                  "#8E24AA",
                  "#6A1B9A",
                  "#4A148C",
                  "#64B5F6",
                  "#42A5F5",
                  "#1E88E5",
                  "#1976D2",
                  "#0D47A1",
                  "#82B1FF",
                ];
                return colorList[params.dataIndex];
              },
              emphasis: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
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
  height: 500px; /* 拉高图表容器 */
  width: 100%;
}

.chart {
  width: 80%; /* 图表宽度 */
  height: 100%; /* 图表高度 */
}
</style>