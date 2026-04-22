import NavBar from "./Navbar"


/* Childen as dynamic content*/
function Layout({children}){

    return (
        <>
        <NavBar />
        <main>
            {children}
        </main>
        </>

    )
}

export default Layout 