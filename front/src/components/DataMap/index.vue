<template>
  <div
    class="main-map-chart"
    ref="dataMap"
    style="width: 100%; height: 100%; height:600px;"
   />
</template>
<script>
import '@/assets/js/china'
let chart = null
import echarts from "echarts/lib/echarts";

export default {
  props: {
    title: String,
    list: Array
  },
  data () {
    return {
      config: {}
    }
  },
  mounted() {
    this.initChart()
  },
  methods: {
    initChart () {
      if (null != chart && undefined != chart) {
        chart.dispose()
      }
      chart = echarts.init(this.$refs.dataMap)
      this.setOptions()
    },
    setOptions() {
      let option = {
        tooltip: {
          triggerOn: 'click',
          formatter: function (e) {
            return 0.5 == e.value ? e.name + '：有疑似病例' : e.seriesName + '<br />' + e.name + '：' + e.value;
          },
        },
        title: {
          text: this.title,
          top: 50,
          left: 'center',
          textStyle: {
            fontWeight: 'bolder',
            fontSize: 24,
            color: '#BCBCBF'
          }
        },
        visualMap: {
          min: 0,
          max: 1000,
          left: 26,
          bottom: 40,
          showLabel: !0,
          textStyle: {
            color: 'rgba(255,255,255,0.7)'
          },
          // 图例
          pieces: [
            {
              gt: 25000,
              label: '> 25000 岗位',
              color: '#5D0773',
            },
            {
              gte: 20000,
              lte: 25000,
              label: '20000 - 25000 岗位',
              color: '#26254F',
            },
            {
              gte: 10000,
              lt: 20000,
              label: '10000 - 20000 岗位',
              color: '#2D2D83',
            },
            {
              gt: 5000,
              lt: 10000,
              label: '5000 - 10000 岗位',
              color: '#2B4AD0',
            },
            {
              gt: 0,
              lt: 5000,
              label: '< 5000 岗位',
              color: '#394064'
            },
          ],
          show: !0,
        },
        geo: {
          map: 'china',
          roam: true, // 开启缩放和平移
          scaleLimit: {
            min: 1, // 最小缩放
            max: 3, // 最大缩放
          },
          zoom: 1.23, // 当前视角的缩放比例
          top: 50,
          label: {
            normal: {
              show: !0,
              fontSize: '14',
              color: 'rgba(255,255,255,0.7)',
            },
          },
          itemStyle: {
            normal: {
              // color: '#FFF',
              areaColor: '#323c48',
              shadowBlur: 10,
              shadowColor: 'rgba(0, 0, 0, 0.5)',// 外发光
              borderColor: 'rgba(0, 0, 0, 0.2)',
            },
            emphasis: {
              // color: '#FFF',
              areaColor: '#18FFFF', // 悬浮区背景，就是鼠标移到区域上变的颜色
              // areaColor: '#2a333d',
              shadowOffsetX: 0,
              shadowOffsetY: 0,
              borderWidth: 0,
            },
          }
        },
        series: [
          {
            name: '岗位数量',
            type: 'map',
            geoIndex: 0,
            data: this.list
          }
        ],
      }
      chart.setOption(option)
    }
  },
  watch: {
    list: {
      handler (newValue, oldValue) {
        if (oldValue != newValue) {
          this.setOptions()
        }
      },
      deep: true
    }
  }
}
</script>
