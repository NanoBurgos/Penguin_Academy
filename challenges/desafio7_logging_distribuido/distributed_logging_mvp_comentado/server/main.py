
from fastapi import FastAPI, Header, HTTPException, Depends
"""FastAPI → clase principal para crear la API.
Header → permite leer valores enviados en los headers HTTP (por ejemplo el token).
HTTPException → sirve para devolver errores HTTP controlados (401, 403, etc).
Depends → sistema de inyección de dependencias de FastAPI (para usar funciones como get_db o verify_token automáticamente)."""

from sqlalchemy import create_engine, Column, Integer, String, DateTime
"""Importaciones del ORM SQLAlchemy:
create_engine → crea la conexión con la base de datos.
Column → define una columna de una tabla.
Integer → tipo de dato entero.
String → tipo texto.
DateTime → tipo fecha y hora."""

from sqlalchemy.ext.declarative import declarative_base #"""Permite crear la clase base para los modelos de base de datos. De esta base heredarán todas las tablas."""

from sqlalchemy.orm import sessionmaker, Session
"""sessionmaker → crea la fábrica de sesiones para conectarse a la BD.
Session → tipo de objeto que representa una sesión activa con la base de datos."""

from pydantic import BaseModel 
"""Pydantic es la biblioteca de validación de datos más utilizada para Python"""

from datetime import datetime, timezone #"""Permite trabajar con fechas y horas."""

from typing import Optional, List
"""Tipos opcionales usados en Python:
Optional → campo que puede ser None.
List → lista de elementos."""

DATABASE_URL = "sqlite:///./logs.db" """Define la URL de conexión a la base de datos."""

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
"""Crea el motor de conexión con la base de datos.
Parámetros:
DATABASE_URL → ruta de la base de datos.
check_same_thread=False → permite que SQLite funcione en múltiples threads, necesario para FastAPI."""

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""Crea la fábrica de sesiones.
Opciones:
autocommit=False → los cambios no se guardan automáticamente.
autoflush=False → no sincroniza automáticamente con la BD.
bind=engine → conecta las sesiones al motor creado.
Cada request creará una sesión nueva de base de datos."""

Base = declarative_base() #Crea la clase base del ORM.

VALID_TOKENS = { # Es un diccionario de tokens autorizados.
    "service-a-token": "service-a",
    "service-b-token": "service-b",
    "service-c-token": "service-c"
}

class Log(Base):
    __tablename__ = "logs"  # Esto conecta la clase con la tabla "logs" en la DB
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, nullable=False)
    service = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    message = Column(String, nullable=False)
    received_at = Column(DateTime, default=datetime.now(timezone.utc))

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Distributed Logging MVP")

class LogCreate(BaseModel): #Campos que el cliente puede enviar.
    timestamp: datetime
    service: str
    severity: str
    message: str
"""cómo deben venir los datos en el request
validación automática
serialización a JSON"""

class LogResponse(LogCreate): #Campos que el servidor puede devolver.
    id: int #generado automáticamente por la base de datos.
    received_at: datetime #timestamp que indica cuándo el servidor recibió el log.

    class Config:
        from_attributes = True 
        """Configuración de Pydantic que indica:
Permitir crear el modelo a partir de objetos de SQLAlchemy, no solo diccionarios.
Sin esto, FastAPI no podría convertir db_log (objeto SQLAlchemy) a LogResponse automáticamente."""

def get_db(): #Define una función que entrega una sesión activa de SQLAlchemy a los endpoints.
    db = SessionLocal() #Crea una sesión nueva con la base de datos SQLite.
    try:
        yield db
        """yield entrega la sesión al endpoint que lo necesita.
Esto permite que FastAPI maneje la dependencia automáticamente."""
    
    finally:
        db.close()
        """Garantiza que la sesión se cierre correctamente al terminar.
Evita fugas de conexión y errores de concurrencia."""

def verify_token(authorization: str = Header(...)): # ... 3 Puntos en FAST API significa que es obligatorio
    if not authorization.startswith("Token "):
        raise HTTPException(status_code=401, detail={"error": "Quién sos, bro?"})
    token = authorization.split(" ")[1] #Extrae el token real del header (Token service-a-token → service-a-token).
    if token not in VALID_TOKENS:
        raise HTTPException(status_code=401, detail={"error": "Quién sos, bro?"})
    return VALID_TOKENS[token]

@app.post("/logs", response_model=LogResponse)
def create_log(log: LogCreate, db: Session = Depends(get_db), service_name: str = Depends(verify_token)):
    if log.service != service_name:
        raise HTTPException(status_code=403, detail="Service name does not match token")
    
    db_log = Log(
        """Crea un objeto SQLAlchemy Log.
Representa un registro que se guardará en la base de datos."""
        timestamp=log.timestamp,
        service=log.service,
        severity=log.severity,
        message=log.message
    )
    db.add(db_log) #agrega el objeto a la sesión.
    db.commit()
    db.refresh(db_log)
    return db_log
"""Devuelve el log guardado.
FastAPI lo convierte automáticamente a LogResponse."""

@app.get("/logs", response_model=List[LogResponse]) #Un decorador es una función que modifica otra función o clase sin cambiar su código interno.
def read_logs(
    timestamp_start: Optional[datetime] = None,
    timestamp_end: Optional[datetime] = None,
    received_at_start: Optional[datetime] = None,
    received_at_end: Optional[datetime] = None,
    severity: Optional[str] = None,
    db: Session = Depends(get_db)
):

    query = db.query(Log)

    if timestamp_start:
        query = query.filter(Log.timestamp >= timestamp_start)

    if timestamp_end:
        query = query.filter(Log.timestamp <= timestamp_end)

    if received_at_start:
        query = query.filter(Log.received_at >= received_at_start)

    if received_at_end:
        query = query.filter(Log.received_at <= received_at_end)

    if severity:
        query = query.filter(Log.severity == severity)

    return query.order_by(Log.timestamp.desc()).all()
"""Ordena los logs por timestamp de forma descendente (más recientes primero).
.all() ejecuta la consulta y devuelve una lista de objetos SQLAlchemy.
FastAPI los convierte automáticamente a lista de LogResponse."""
