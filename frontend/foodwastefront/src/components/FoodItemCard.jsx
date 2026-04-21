function FoodItemCard({name,quantity,weight_in_grams,category,created_at}){

    return (
        
        <article>
        <h3>{name}</h3>
        <p>{quantity}</p>
        <p>{weight_in_grams}g</p>
        <p>{category}</p>
        <p>{new Date(created_at).toLocaleDateString()}</p>
        </article>
    )
}

export default FoodItemCard