function UserForm(){

    return (
        <div>
            <form >
                <label htmlFor="name">Nome</label><br />
                <input type="text"name="name" id="name" /><br />

                <label htmlFor="unique_Code">Identificador Unico</label><br />
                <input type="number"name="unique_Code" id="unique_Code" /><br />

            </form>
        </div>
    )
   
}

export default UserForm