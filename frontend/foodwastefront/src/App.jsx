import NavBar from "./components/Navbar"
import Layout from "./components/layout"
import FoodItems from "./pages/FoodItems"
import { getAllFoodItems } from "./services/foodItemService"

function App() {

  
    return (
        <Layout>
           <FoodItems />
        </Layout>
    )
}

export default App
