import React from "react";
import { Routes, Route } from "react-router-dom";
import CursoList from "./pages/Curso/List";
import AlunoList from "./pages/Aluno/List"
import Home from "./pages/Home/Home"

export function Router() {
    return (
    
    <Routes>

        <Route path="/" element={<Home />}></Route>

        <Route path="/curso/list" element={<CursoList />}></Route>
        
        <Route path="/aluno/list" element={<AlunoList />}></Route>

    </Routes>

    );  

}
  
export default Router;