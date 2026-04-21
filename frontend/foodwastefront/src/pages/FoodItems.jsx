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
                       < FoodItemCard 
                       key={item.id}
                       name={item.name} 
                       quantity={item.quantity} 
                       weight_in_grams={item.weight_in_grams}
                       category={item.category}
                       created_at={item.created_at} 
                       />
                    )
                )
            }
         </ul>
        </>
    )


}

export default FoodItems