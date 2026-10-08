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
            title="求职关键词"
            toolbar-height="56"
        >
          <template slot="card-content" >
            <word-cloud/>
          </template>
        </v-basic-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>
import 'echarts-wordcloud';
import WordCloud from "./WordCloud";

export default {
  name: 'VBarIndex',
  components: {
    WordCloud
  },
};
</script>
