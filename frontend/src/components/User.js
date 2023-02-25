import React from 'react'


const UserItem = ({ user }) => {
    return (
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}


const UserList = ({ users }) => {
    return (
        <table>
            <th>
                Username
            </th>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Email
            </th>
            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}


export default UserList;





// import React from 'react'


// const UserItem = ({user}) => {
//     return (
//         <tr>
//             <td>{user.username}</td>
//             <td>{user.firstName}</td>
//             <td>{user.lastName}</td>
//             <td>{user.email}</td>
//         </tr>
//     )
// }

// const UserList = ({users}) => {
//     return (
//         <table className="table">
//             <tr>
//                 <th>Login</th>
//                 <th>First Name</th>
//                 <th>Last Name</th>
//                 <th>Email</th>
//             </tr>
//             {users.map((user) => <UserItem user={user} />)}
//         </table>
//     )
// }

// export default UserList
