import axios from 'axios'

const API_URL = 'http://localhost:8000'

/*Use of params since our programing need some filter*/
export function getAllFoodItems(params = {}) {
    return axios.get(`${API_URL}/food_item`, { params })
}
