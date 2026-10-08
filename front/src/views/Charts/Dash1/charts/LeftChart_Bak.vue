<template>
  <v-chart
      style="width:100%;"
      :options="chartOption"
      autoresize
  />
</template>

<script>
// import {getChart1} from "../../../../api/job";

export default {
  name: 'BaseLineChart',
  data() {
    return {
      chartOption: {},
      datas: [],
      labels: []
    };
  },
  async mounted() {
    // await getChart1().then(res => {
    //   this.datas = res.data.data.all.map(i => i.value)
    //   this.labels = res.data.data.all.map(i => i.name)
    // })
    this.chartOption = this.buildChartOption();
  },
  methods: {
    buildChartOption() {
      const option = {
        // backgroundColor: '#394056',
        title: [
          // {
          //   text: '【交易笔数分析】',
          //   textStyle: {
          //     fontSize: 12,
          //     color: '#75deef',
          //     fontWeight: 'normal'
          //   },
          //   top: '24%',
          //   left: '20%'
          // },
          // {
          //   text: '【交易金额分析】',
          //   textStyle: {
          //     fontSize: 12,
          //     color: '#75deef',
          //     fontWeight: 'normal'
          //   },
          //   top: '24%',
          //   right: '12%'
          // },
        ],
        grid: [
          {
            show: false,
            left: '2%',
            top: '11%',
            right: '2%',
            bottom: '60%',
            containLabel: true,
          },
          {
            show: false,
            left: '2%',
            top: "55%",
            bottom: '10%',
            right: '2%',
            containLabel: true,
          },
        ],
        legend: {
          type: 'scroll',
          show: true,
          textStyle: {
            fontSize: 10,
            color: '#ECEFF1',
          },
        },
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'line',
          },
          // formatter: (params) =>{
          //   console.log(params)
          //   return params
          // }
        },
        xAxis: [{
          type: 'category',
          // data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
          data: this.labels,
          axisLine: {
            lineStyle: {
              color: '#78909C',
            },
          },
        },
          {
            gridIndex: 1,
            type: 'category',
            // data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            data: this.labels,
            axisLine: {
              lineStyle: {
                color: '#78909C',
              },
            },
          }
        ],
        yAxis: [{
          type: 'value',
          axisLine: {
            lineStyle: {
              color: '#78909C',
            },
          },
        },
          {
            gridIndex: 1,
            type: 'value',
            axisLine: {
              lineStyle: {
                color: '#78909C',
              },
            },
          }

        ],
        series: [
          {
            name: '所有类型',
            data: [900, 667, 1232, 1058, 760, 1720, 1590],
            type: 'line',
            smooth: true,
            itemStyle: {
              color: '#B388FF',
            },
          },
          {
            name: '所有类型',
            type: 'pie',
            radius: ['20%', '30%'],
            center: ['50%', '70%'],
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            itemStyle: {
              color: function (params) {
                var colorList = ['#F3E5F5', '#E1BEE7', '#CE93D8', '#BA68C8', '#8E24AA','#6A1B9A','#4A148C'];
                return colorList[params.dataIndex];
              },
              emphasis: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              { value: 1048, name: 'Search Engine' },
              { value: 735, name: 'Direct' },
              { value: 580, name: 'Email' },
              { value: 484, name: 'Union Ads' },
              { value: 300, name: 'Video Ads' }
            ],
            xAxisIndex: 1,
            yAxisIndex: 1,
          }
        ],
      };
      return option;
    },
  }
};
</script>
<style>
/**
 * 默认尺寸为 600px×400px，如果想让图表响应尺寸变化，可以像下面这样
 * 把尺寸设为百分比值（同时请记得为容器设置尺寸）。
 */
</style>
