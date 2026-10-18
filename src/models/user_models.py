from enum import Enum # Enum: Permite definir un conjunto de opciones fijas.
from pydantic import BaseModel, EmailStr # Pydantic: Permite crear modelos y validar datos.
from typing import List, Optional # Typing: Permite especificar tipos de datos como listas y valores opcionales.

class RolEnum(str, Enum):
    ADMINISTRADOR = "Administrador"
    GERENTE = "Gerente"
    COLABORADOR = "Colaborador"

class Permiso(BaseModel):
    id_permiso: int
    nombre: str

class UsuarioBase(BaseModel):
    correo: EmailStr
    rol: RolEnum

class UsuarioCreate(UsuarioBase):
    contrasena: str

class UsuarioResponse(UsuarioBase):
    id_usuario: int
    
    class Config:
        from_attributes = True