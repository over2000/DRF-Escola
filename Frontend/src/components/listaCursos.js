import React, { useState, useEffect } from 'react';


export default function ListaCursos() {
    const [cursos, setCursos] = useState([])

    useEffect(async() =>{
        const response = await fetch('http://localhost:8000/cursos/')
        const data = await response.json();

        setCursos(data)

    }, []);

return (
    <ul>
        {cursos.map(curso => (
            <li key={curso.id}> {curso.descricao} </li>
        ))}
        
    </ul>
);

}


// class ListaCursos extends Component {
//     state = {
//         data: [],
//         loaded: false
//     }

//     componentDidMount() {
//         fetch("http://localhost:8000/cursos/")
//           .then(response => {
//             if (response.status > 400) {
//             // Código do comportamento em caso de problema na req
//             }
//             return response.json();
//           })
//           .then(data => {
//             this.setState(() => {
//               return {
//                 data,
//                 loaded: true
//               };
//             });
//           });
//       }
    
//       render() {
//         return (
//             <div>
//             {this.state.data.map(curso => {
//               return (
//                 <h2 key={curso.id} className='App-table'>
//                   {curso.descricao}
//                 </h2>
//               );
//             })}
//           </div>
//         );
//       }
//     }

// export default ListaCursos;

