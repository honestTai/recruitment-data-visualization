import axios from 'axios'

const service =  axios.create({
    baseURL: '/api',
    timeout: 120000,
    // headers : {"Access-Control-Allow-Origin":"*"}
})

export default service
