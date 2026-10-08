import request from '@/api/request'

const base = '/job'

export function getWordCut() {
  return request({
    url: base + '/getWordCut',
    method: 'get',
  })
}

export function get(data){
  return request({
    url: base + '/get',
    method: 'get',
    params: data
  })
}

export function getHot() {
  return request({
    url: base + '/getHot',
    method: 'get',
  })
}

export function getUserCF(userId) {
  return request({
    url: base + '/getRecomendation',
    method: 'get',
    params: {'userId': userId}
  })
}

export function getItemCF(userId) {
  return request({
    url: base + '/getRecomendation',
    method: 'get',
    params: {'userId': userId}
  })
}

export function getChart1() {
  return request({
    url: base + '/getChart1',
    method: 'get',
  })
}


export function getAreaChart() {
  return request({
    url: base + '/getAreaChart',
    method: 'get',
  })
}

export function getChart2() {
  return request({
    url: base + '/getChart2',
    method: 'get',
  })
}


export function getChart3() {
  return request({
    url: base + '/getChart3',
    method: 'get',
  })
}

export function getNationRank() {
  return request({
    url: base + '/getNationRank',
    method: 'get',
  })
}

export function getMapData() {
  return request({
    url: base + '/getMapData',
    method: 'get',
  })
}

export function getTypeRate() {
  return request({
    url: base + '/getTypeRate',
    method: 'get',
  })
}


export function getTimeLine() {
  return request({
    url: base + '/getTimeLine',
    method: 'get',
  })
}

// 获取统计数字
export function getPanel() {
  return request({
    url: base + '/getPanel',
    method: 'get',
  })
}

// 按照省份分组统计
export function getCityJob() {
  return request({
    url: base + '/getCityJob',
    method: 'get',
  })
}

// 按照城市分组统计
export function getCityJob2() {
  return request({
    url: base + '/getCityJob2',
    method: 'get',
  })
}

// 按照公司类型分组统计
export function getTypeRank() {
  return request({
    url: base + '/getTypeRank',
    method: 'get',
  })
}
// 按照学历需求类型分组统计
export function getDegreeRank() {
  return request({
    url: base + '/getDegreeRank',
    method: 'get',
  })
}

export function getRating(params) {
  return request({
    url: base + '/getRating',
    method: 'get',
    params,
  });
}

export function submitRatingAPI(params) {
  return request({
    url: base + '/rate',
    method: 'get',
    params,
  });
}
export function fetchJobData() {
  return request({
    url: base + '/crawl',
    method: 'get'
  });
}

