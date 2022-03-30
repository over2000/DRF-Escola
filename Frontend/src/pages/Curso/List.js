import React, { useState, useEffect } from 'react';


function ListCursos() {
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

export default ListCursos