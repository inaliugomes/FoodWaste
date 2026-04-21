import axios from 'axios'

const API_URL = 'http://localhost:8000'

export function getAllUser(){

    return axios.get(`${API_URL}/user`)
}

