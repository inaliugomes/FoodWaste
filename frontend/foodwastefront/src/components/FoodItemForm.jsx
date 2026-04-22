import { useState } from "react"
import { postFoodItem } from "../services/foodItemService"

function FoodItemForm(){

    const [formData,setFormData] = useState({"name":"",
        "quantity":"",
        "weight_in_grams":"",
        "category":"",
        "user_id":""})

    return ( 
       <div>
        <form onSubmit={
            async e => {
                e.preventDefault()
                const payload = {
                    ...formData,
                    quantity:Number(formData.quantity),
                    weight_in_grams:Number(formData.weight_in_grams),
                    user_id:Number(formData.user_id)
                }
                try {
                    await postFoodItem(payload)
                    console.log("Criado com successo")
                }catch(err) {
                    console.error(err)
                }
            }
        }>
            <label htmlFor="name">Nome</label><br />
            <select name="name"
             id="name" 
             value={formData.name}
             onChange={
                e => setFormData(
                    prev =>({
                        ...prev,
                        [e.target.name]: e.target.value
                    })
                )
             }
             >
                <option value="Lechuga">Lechuga</option>
                <option value="Tomate">Tomate</option>
                <option value="Cebolla">Cebolla</option>
                <option value="Arroz">Arroz</option>
                <option value="Alubias">Alubias</option>
                <option value="Tiras">Tiras</option>
                <option value="Pollo">Pollo</option>
            </select><br />

            <label htmlFor="quantity">Quantidad</label><br />
            <input type="number" 
            id="quantity" 
            name="quantity" 
            value={formData.quantity}
            onChange={
                e => setFormData(
                    prev => ({
                        ...prev,
                        [e.target.name]: e.target.value
                    })
                )
            }
            
            /><br/>

            <label htmlFor="weight_in_grams">Peso</label><br />
            <input type="number" 
            id="weight_in_grams" 
            name="weight_in_grams"
            value={formData.weight_in_grams}
            onChange={
                e => setFormData(
                    prev => ({
                        ...prev,
                        [e.target.name]: e.target.value
                    })
                )
            }
            
            
            /><br/>
            
            <label htmlFor="category">Categoria</label><br />
            <select name="category" id="category"
               value={formData.category}
            onChange={
                e => setFormData(
                    prev => ({
                        ...prev,
                        [e.target.name]: e.target.value
                    })
                )
            }
            
            >
                <option value="Verdura">Verdura</option>
                <option value="Pollo">Pollo</option>
                <option value="Organico">Organico</option>
            </select><br />

            <label htmlFor="user_id">User ID</label><br />
            <input type="number" id="user_id" name="user_id"
             value={formData.user_id}
            onChange={
                e => setFormData(
                    prev => ({
                        ...prev,
                        [e.target.name]: e.target.value
                    })
                )
            }
            /><br />

            <button type="submit">Añadir</button>
        </form>
       </div>
    )

}

export default FoodItemForm