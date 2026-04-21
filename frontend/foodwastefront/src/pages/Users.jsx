import { useEffect, useState } from "react";
import { getAllUser } from "../services/userService";
import UserCard from "../components/UserCard";

function Users(){

    const [data , setData] = useState([])
    const [loading,setLoading] = useState(true)
    const [error,setError] = useState(null)

    useEffect( ()=>{

        const fetchData = async () =>{

            try {
                const response = await getAllUser()
                setData(response.data.users)

            }catch(err){
                setError(err.message)
            } finally{
                setLoading(false)
            }
        }
        fetchData()
    },[])

    if (loading)  return <p>Loading</p>
    if (error) return <p>Error:{error}</p>

    return (
        <>
        <ul>
            {
                data.map(
                    user => (
                        <UserCard key={user.id}
                        name={user.name}
                        unique_Code={user.unique_Code}
                        />
                    )
                )
            }
        </ul>
        </>
    )


}
export default Users