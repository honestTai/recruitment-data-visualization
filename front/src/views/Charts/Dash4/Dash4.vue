<template>
  <v-container
      grid-list-lg
      pa-0
  >
    <v-layout wrap>
      <v-flex
          xs12
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
import 'echarts-wordcloud';
import DotChart from "./DotChart";

export default {
  name: 'VBarIndex',
  components: {
    DotChart
  },
};
</script>
