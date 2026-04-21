/* Componente tonto
Apenas vai servir para mostar os dados 
*/

function UserCard({name,unique_Code}){

    return (
        <>
        <article>
            <h3>{name}</h3>
            <p>{unique_Code}</p>
        </article>
        </>
    )
}

export default UserCard