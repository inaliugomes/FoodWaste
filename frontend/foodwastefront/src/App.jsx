
import Layout from "./components/layout"
import { Route , Routes } from "react-router-dom"
import Users from "./pages/Users"
import FoodItemPage from "./pages/FoodItemsPage"



function App() {

  
    return (
        <Layout>
          <Routes>
            <Route path="/" element={<p>Dashboard (em breve)</p>}/>
            <Route path="/food-items" element={<FoodItemPage/>}/>
            <Route path="/users" element={<Users/>}/>
          </Routes>
        </Layout>
    )
}

export default App
