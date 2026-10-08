<template>
  <v-chart
    style="width:100%; min-height:650px;"
    :options="chartOption"
    autoresize
  />
</template>

<script>
import {getTypeRate} from "@/api/job";

export default {
  name: 'BaseBarChart',
  data() {
    return {
      chartOption: {},
      d1 :[],
      d2 :[],
      d3 :[],
      d4 :[],
      d5 :[],
      l1 :[]
    };
  },
  async mounted() {
    await getTypeRate().then(res => {
      // console.log(res.data.data)
      this.d1 = res.data.data.datas[0]
      this.d2 = res.data.data.datas[1]
      this.d3 = res.data.data.datas[2]
      this.d4 = res.data.data.datas[3]
      this.d5 = res.data.data.datas[4]
      this.l1 = res.data.data.labels
      console.log(this.l1)
    })
    this.chartOption = this.buildChartOption();
  },
  methods: {
    buildChartOption() {
      const option = {
        color: ['#fec42c', '#80F1BE', '#64B5F6','#455A64','#DD2C00'],
        legend: {
          data: this.l1,
          left: 'center',
          bottom: 10,
          textStyle:{
            fontSize: 20,
            color: '#F1F1F3'
          }
        },
        tooltip: {
          backgroundColor: 'rgba(255,255,255,0.7)',
          formatter: function (param) {
            var value = param.value;
            // prettier-ignore
            return '<div style="border-bottom: 1px solid rgba(255,255,255,.3); font-size: 18px;padding-bottom: 7px;margin-bottom: 7px">'
                + param.seriesName + ' '  + '学历：'
                + value[2]
                + '</div>'
                + '职位：' + param.value[4] + '<br>'
                + '公司：' + param.value[5] + '<br>'
                + '最高月薪：' + param.value[1] + '<br>'
                + '最低月薪：' + param.value[3] + '<br>'
          },
            axisPointer: {
              show: true,
              type: 'cross',
              lineStyle: {
                type: 'dashed',
                width: 1
              }
            }
        },
        // tooltip: {
        //   // trigger: 'axis',
        //   showDelay: 0,
        //   formatter: function (params) {
        //     if (params.value.length > 1) {
        //       return (
        //           params.seriesName +
        //           ' :<br/>' +
        //           params.value[2] + ',最高月薪' +
        //           params.value[1] +
        //           '元'
        //       );
        //     }
        //   },
        //   axisPointer: {
        //     show: true,
        //     type: 'cross',
        //     lineStyle: {
        //       type: 'dashed',
        //       width: 1
        //     }
        //   }
        // },
        xAxis: {
          type: 'value',   //这个分为category类目,value数值,time,时间和log对数,选择的不对可能出现无法对应的x轴问题
          scale: true,
          data: [-1,1,2,3,4,5,6,7,8,9],
          axisLabel: {
            show: true,
            fontSize: 14,
            color: '#F1F1F3',
            formatter: function (number){
              return number + '万元'
            }
          }
        },
        yAxis: {
          scale: true,
          axisLine: {
            lineStyle: {
              color: '#78909C',
            },
          },
          axisLabel: {
            show: true,
            fontSize: 14,
            color: '#F1F1F3'
          },
        },
        series: [
          {
            name : this.l1[0],
            symbolSize: function (dataItem) {
              // console.log(dataItem)
              return dataItem[1] / 6000;
            },
            emphasis: {
              focus: 'series'
            },
            markArea: {
              silent: true,
              itemStyle: {
                color: 'transparent',
                borderWidth: 1,
                borderType: 'dashed'
              },
              data: [
                [
                  {
                    name: '薪酬区间',
                    xAxis: 'min',
                    yAxis: 'min'
                  },
                  {
                    xAxis: 'max',
                    yAxis: 'max'
                  }
                ]
              ]
            },
            data: this.d1,

                // [
              // [2001, 8.04],
              // [2002, 6.95],
              // [2003, 7.58],
              // [2004, 8.81],
              // [1998, 8.33],
              // [1997, 7.66],
              // [1997, 6.81],
              // [1995, 6.33],
              // [1993, 8.96],
              // [1992, 6.82],
              // [1991, 7.2],
              // [1994, 7.2],
              // [2021, 4.23],
              // [1950, 7.83],
              // [1948, 4.47],
              // [2010, 3.33],
              // [1999, 4.96],
              // [2011, 7.24],
              // [2019, 6.26],
              // [2013, 8.84],
              // [1987, 5.82],
              // [1983, 5.68]
            // ],
            type: 'scatter'
          },
          {
            name : this.l1[1],
            symbolSize: function (dataItem) {
              // console.log(dataItem)
              return dataItem[1] / 6000;
            },
            data: this.d2,
            type: 'scatter',
            emphasis: {
              focus: 'series'
            },
          },
          {
            name : this.l1[2],
            symbolSize: function (dataItem) {
              // console.log(dataItem)
              return dataItem[1] / 6000;
            },
            data: this.d3,
            type: 'scatter',
            emphasis: {
              focus: 'series'
            },
          },
          {
            name : this.l1[3],
            symbolSize: function (dataItem) {
              // console.log(dataItem)
              return dataItem[1] / 6000;
            },
            data: this.d4,
            type: 'scatter',
            emphasis: {
              focus: 'series'
            },
          },
          {
            name : this.l1[4],
            symbolSize: function (dataItem) {
              // console.log(dataItem)
              return dataItem[1] / 6000;
            },
            data: this.d5,
            type: 'scatter',
            emphasis: {
              focus: 'series'
            },
          }
        ],
      };
      return option;
    },
  },
};
</script>
