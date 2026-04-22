
import Layout from "./components/layout"
import FoodItems from "./pages/FoodItems"
import FoodItemForm from "./components/FoodItemForm"
import { Route , Routes } from "react-router-dom"
import Users from "./pages/Users"



function App() {

  
    return (
        <Layout>
          <Routes>
            <Route path="/" element={<p>Dashboard (em breve)</p>}/>
            <Route path="/food-items" element={
                <>
                <FoodItems />
                <FoodItemForm/>
                </>
            }/>
            <Route path="/users" element={<Users/>}/>
          </Routes>
        </Layout>
    )
}

export default App
