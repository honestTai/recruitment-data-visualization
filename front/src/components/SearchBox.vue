<template>
  <v-autocomplete
      outlined
      rounded
      :loading="loading"
      dense
      clearable
      :menu-props="{ contentClass: 'transparent-scroll' }"
      :items="searchItems"
      item-text="title"
      color="#4edf93"
      :search-input.sync="searchTerm"
      no-data-text="尝试输入职位名..."
      placeholder="输入关键词"
  >
    <template #prepend-inner>
      <v-icon size="18" class="mt-1 mr-2">mdi-magnify</v-icon>
    </template>
    <template #append>
      <v-icon @click="voiceSearch" size="21"></v-icon>
    </template>

    <template #item="{item}" class="mt-12">
      <v-list-item two-line :to="`/search?q=${item.title}`">
        <v-list-item-content class="text-left">
          <v-list-item-title>{{ item.title }}</v-list-item-title>
          <v-list-item-subtitle>{{ item.type }}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </template>
  </v-autocomplete>
</template>

<script>
export default {
  name: "search-box",
  data: () => ({
    searchTerm: "",
    loading: false,
    searchItems: [],
  }),
  watch: {
    searchTerm(newValue) {
      this.loading = true;
      this.$emit("onSearch", newValue); // 通知父组件查询
      this.loading = false;
    },
  },
  methods: {
    voiceSearch() {
      this.$emit("onVoiceSearch");
    },
  },
};
</script>

<style>
.transparent-scroll {
  scrollbar-width: thin;
  scrollbar-color: transparent;
}
.transparent-scroll::-webkit-scrollbar {
  width: 6px;
  background-color: transparent;
}
.transparent-scroll::-webkit-scrollbar-thumb {
  background: #d8dcde;
  border-radius: 4.5px;
}
.transparent-scroll::-webkit-scrollbar-track {
  background-color: transparent;
}
</style>