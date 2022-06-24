from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Enum, Float, Date, DateTime, func
from sqlalchemy.orm import declarative_base, relationship, validates
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    idt_user      = Column(Integer, primary_key=True, autoincrement=True)
    des_login     = Column(String(40), unique=True,nullable=False)
    des_password  = Column(String(100), nullable=False)
    ind_status    = Column(Boolean, default=True, server_default='t')
    transactions  = relationship('Transactions', backref='user', lazy='subquery')    

class Transactions(Base):
    __tablename__      = 'transactions'
    cod_transaction    = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cod_ticker         = Column(String(20), nullable=False)
    des_broker         = Column(String(50), nullable=False)
    type_transaction   = Column(Enum('COMPRA', 'VENDA', name='enum_type_transaction'), nullable=False)
    num_amount         = Column(Integer, nullable=False)
    num_price_cost     = Column(Float, default=0, nullable=False)
    num_cost_operation = Column(Float, default=0, nullable=False)
    idt_user           = Column(Integer, ForeignKey('user.idt_user'), nullable=False)
    dat_transaction    = Column(Date, nullable=False)
    dat_created        = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    dat_modified       = Column(DateTime(timezone=True), nullable=False,server_default=func.now(),  onupdate=func.utc_timestamp())
    
    @validates('cod_ticker')
    def convert_upper(self, key, value):
        return value.upper()