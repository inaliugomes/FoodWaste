import { useEffect, useState } from "react";
import FoodItems from "./FoodItems";
import { getAllFoodItems} from "../services/foodItemService";
import FoodItemForm from "../components/FoodItemForm";


function FoodItemPage(){

        
    const [data , setData] = useState([])
    const [loading , setLoading] = useState(true)
    const [error , setError] = useState(null)

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
  useEffect(()=>{
    fetchData()
    },[])
    
    if (loading) return <p>Loading</p>
    if (error) return  <p>Error:{error}</p>

    return (
        <>
        <FoodItems items={data}/>
        <FoodItemForm onSuccess={fetchData}/>
        </>
    )

}


export default FoodItemPage