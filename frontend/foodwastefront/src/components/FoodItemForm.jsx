
function FoodItemForm(){

    return ( 
       <div>
        <form >
            <label htmlFor="name">Nome</label><br />
            <select name="name" id="name">
                <option value="Lechuga">Lechuga</option>
                <option value="Tomate">Tomate</option>
                <option value="Cebolla">Cebolla</option>
                <option value="Arroz">Arroz</option>
                <option value="Alubias">Alubias</option>
                <option value="Tiras">Tiras</option>
                <option value="Pollo">Pollo</option>
            </select><br />

            <label htmlFor="quantity">Quantidad</label><br />
            <input type="number" id="quantity" name="quantity"/><br/>

            <label htmlFor="weight_in_grams">Peso</label><br />
            <input type="number" id="weight_in_grams" name="weight_in_grams"/><br/>
            
            <label htmlFor="category">Categoria</label><br />
            <select name="category" id="category">
                <option value="Verdura">Verdura</option>
                <option value="Pollo">Pollo</option>
                <option value="Organico">Organico</option>
            </select><br />

            <label htmlFor="user_id">User ID</label><br />
            <input type="number" id="user_id" name="user_id" /><br />

            <button type="submit">Añadir</button>
        </form>
       </div>
    )

}

export default FoodItemForm