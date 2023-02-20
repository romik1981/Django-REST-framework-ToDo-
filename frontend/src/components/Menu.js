// import React from 'react'


// const Menu = () => {
//     return (
//         <div>
//             <p>
//                 MENU
//             </p>
//         </div>

//     )
// }

// export default Menu;



import React from 'react'
import { Link } from 'react-router-dom'


const MenuItem = ({ item }) => {
    return (
        <li><Link to={item.link}>{item.title}</Link></li>
    )
}

const MenuList = ({ menu }) => {
    return (
        <ul class="menu">
            {menu.map((item) => <MenuItem item={item} />)}
        </ul>
    )
}

export default MenuList;
