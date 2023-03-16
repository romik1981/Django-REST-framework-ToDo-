import React from 'react'
import { Link } from 'react-router-dom'


const ProjectItem = ({ project, deleteProject }) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.repository}
            </td>
            <td>
                {project.users.join('; ')}
            </td>
            <td><button onClick={() => deleteProject(project.id)} type='button'>Delete</button></td>
        </tr>
    )
}


const ProjectList = ({ projects, deleteProject }) => {
    return (
        <div>
            <table class="projectlist">
                <th>
                    Name
                </th>
                <th>
                    Repository
                </th>
                <th>
                    Users
                </th>
                <th></th>
                {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject} />)}
            </table>
            <Link to='/projects/create'>Create Project</Link>
        </div>
    )
}


export default ProjectList







// import React from 'react'
// import {
//   Link,
//   useParams
// } from "react-router-dom";


// const ProjectListItem = ({item}) => {
//     let link_to = `/project/${item.id}`
//     return (
//         <tr>
//             <td>{item.id}</td>
//             <td>{item.name}</td>
//             <td>{item.repository}</td>
//             <td><Link to={link_to}>Detail</Link></td>
//         </tr>
//     )
// }

// const ProjectList = ({items}) => {
//     //console.log(users)
//     return (
//         <table className="table">
//             <tr>
//                 <th>Id</th>
//                 <th>Name</th>
//                 <th>Repository</th>
//                 <th></th>
//             </tr>
//             {items.map((item) => <ProjectListItem item={item} />)}
//         </table>
//     )
// }

// const ProjectUserItem = ({item}) => {
//     return (
//         <li>
//         {item.username} ({item.email})
//     </li>
//     )
// }

// const ProjectDetail = ({getProject, item}) => {
//     let { id } = useParams();
//     getProject(id)
//     let users = item.users ? item.users : []
//     console.log(id)
//     return (
//         <div>
//             <h1>{item.name}</h1>
//             Repository: <a href={item.repository}>{item.repository}</a>
//             <p></p>
//             Users:
//             <ol>
//             {users.map((user) => <ProjectUserItem item={user} />)}
//             </ol>
//         </div>
//     )
// }

// export {ProjectDetail, ProjectList}
