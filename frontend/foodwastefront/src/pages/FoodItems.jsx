import FoodItemCard from "../components/FoodItemCard"


function FoodItems({items}){

    return (
        <>
         <ul>
            {
                items.map(
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