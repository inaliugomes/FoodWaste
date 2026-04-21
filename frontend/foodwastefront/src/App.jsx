import NavBar from "./components/Navbar"
import Layout from "./components/layout"
import FoodItems from "./pages/FoodItems"
import FoodItemForm from "./components/FoodItemForm"
import { getAllFoodItems } from "./services/foodItemService"

function App() {

  
    return (
        <Layout>
           <FoodItems />
           <FoodItemForm/>
        </Layout>
    )
}

export default App
