import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';

const columns = [
    { field: 'id', headerName: 'ID' },
    { field: 'nome', headerName: 'Nome', width: 250 },
    { field: 'rg', headerName: 'RG', width: 150 },
    { field: 'cpf', headerName: 'CPF', width: 150 },
    { field: 'data_nascimento', headerName: 'Nascimento', width: 100 }
  ]


function ListAlunos() {
    const [alunos, setAlunos] = useState([])

    useEffect(async() =>{
        const response = await fetch('http://localhost:8000/alunos/')
        const data = await response.json();

        setAlunos(data)

    }, []);

return (

    <div style={{ height: 600, width: '100%' }}>
      <DataGrid
        rows={alunos}
        columns={columns}
        pageSize={20}
        checkboxSelection
      />
    </div>
);

}

export default ListAlunos