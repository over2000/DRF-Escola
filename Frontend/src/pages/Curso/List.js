import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';

const columns = [
    { field: 'id', headerName: 'ID' },
    { field: 'codigo_curso', headerName: 'Código', width: 100 },
    { field: 'descricao', headerName: 'Descrição', width: 250 },
    { field: 'nivel', headerName: 'Nível', width: 100 }
  ]

function ListCursos() {
    const [cursos, setCursos] = useState([])

    useEffect(async() =>{
        const response = await fetch('http://localhost:8000/cursos/')
        const data = await response.json();

        setCursos(data)

    }, []);

return (

    <div style={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={cursos}
        columns={columns}
        pageSize={12}
        checkboxSelection
      />
    </div>
);

}

export default ListCursos