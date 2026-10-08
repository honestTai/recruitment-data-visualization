import {mapState} from "vuex";

let mixin =  {
  data: ()=>({
    appName : '招聘',
    appIcon : 'job'
  }),
  created() {
  },
  mounted() {},
  methods: {
    serverImg(url){
      return "http://localhost:8080/file/download/" + url
    }
  },
  //直接把mapState mixin进去
  computed: {
    ...mapState(['uid','avatar']),
  },
};
export default mixin;
