from fastapi import APIRouter, HTTPException
from src.models.user_models import UsuarioCreate, UsuarioResponse, RolEnum

router = APIRouter(prefix="/usuarios", tags=["Usuarios y Roles"])

usuarios_db = []

@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate):
    nuevo_id = len(usuarios_db) + 1

    usuario_guardado = UsuarioResponse(
        id_usuario=nuevo_id,
        correo=usuario.correo,
        rol=usuario.rol
    )

    usuarios_db.append(usuario_guardado)

    return usuario_guardado

@router.get("/")
def listar_usuarios():
    return usuarios_db