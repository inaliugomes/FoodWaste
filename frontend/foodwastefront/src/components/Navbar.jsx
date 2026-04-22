
import { Link } from "react-router-dom"

function NavBar(){

    return (

    <nav >
        
        <div>
            <Link to={"/"}> Meu Site </Link>
        </div>
        <div>
            <ul>
            <li><Link to="/food-items">Comida</Link>
            </li>
            <li><Link to="/users">Usuario</Link>
            </li>
            <li><Link to={"/"}>Dashboard</Link></li>
           
        </ul>
        </div>
        
    </nav>
    )
}

export default NavBar