import React, { useState, useEffect } from 'react';


function ListAlunos() {
    const [alunos, setAlunos] = useState([])

    useEffect(async() =>{
        const response = await fetch('http://localhost:8000/alunos/')
        const data = await response.json();

        setAlunos(data)

    }, []);

return (
    <ul>
        {alunos.map(aluno => (
            <li key={aluno.id}> {aluno.nome} </li>
        ))}
        
    </ul>
);

}

export default ListAlunos