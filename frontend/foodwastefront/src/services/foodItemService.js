import axios from 'axios'

const API_URL = 'http://localhost:8000'

export function getAllFoodItems(){

    return axios.get(`${API_URL}/food_item`)
}

export function createdFoodItem(data){

    return axios.post(`${API_URL}/food_item`, data)
}

export default getAllFoodItems

