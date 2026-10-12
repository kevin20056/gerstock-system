from enum import Enum # Enum: Permite definir un conjunto de opciones fijas.
from pydantic import BaseModel, EmailStr # Pydantic: Permite crear modelos y validar datos.
from typing import List, Optional # Typing: Permite especificar tipos de datos como listas y valores opcionales.

class RolEnum(str, Enum):
    ADMINISTRADOR = "Administrador"
    GERENTE = "Gerente"
    COLABORADOR = "Colaborador"

class RolBase(BaseModel):
      id_rol: int
      nombre: RolEnum
      permisos: List[str] = []

class UsuarioBase(BaseModel):
     correo: EmailStr
     nombre: str
     rol: RolEnum

class UsuarioCreate(UsuarioBase):
    contrasena: str

class UsuarioResponse(UsuarioBase):
     id_usuario: int

     class Config:
          from_attributes = True