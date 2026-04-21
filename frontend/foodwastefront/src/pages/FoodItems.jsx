import { useState,useEffect } from "react"
import FoodItemCard from "../components/FoodItemCard"
import { getAllFoodItems } from "../services/foodItemService"


function FoodItems(){
  
  
  const [data , setData] = useState([])
  const [loading , setLoading] = useState(true)
  const [error , setError] = useState(null)

  useEffect(()=>{
       
    const fetchData = async () => {
        try{
        const response = await getAllFoodItems()
        setData(response.data.items)
    } catch(err){
        setError(err.message)
    } finally {
        setLoading(false)
    }
    };
    fetchData()
    },[])
    
    if (loading) return <p>Loading</p>
    if (error) return  <p>Error:{error}</p>

    return (
        <>
         <ul>
            {
                data.map(
                    item => (
                        <li key = {item.id}>{item.name}</li>
                    )
                )
            }
         </ul>
        </>
    )


}

export default FoodItems