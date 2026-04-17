import {getAllFoodItems} from '../services/foodItemService'

import { useEffect, useState} from 'react'


function FoodItems(){
    const [dados,setDados] = useState([])
    useEffect(()=>{
    getAllFoodItems().then(response => {
        console.log(response.data)
        setDados(response.data)
    })
},[])

return <div>{JSON.stringify(dados)}</div>
}

export default FoodItems