import React from "react";
import { Link } from "react-router-dom";


function Home() {

return (

    <div>
  
        <h3><Link to="/curso/list">Lista de Cursos</Link></h3>
    
        <h3><Link to="/aluno/list">Lista de Alunos</Link></h3>
        
    </div>
    );

}

export default Home