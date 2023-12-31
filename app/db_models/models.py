import uuid
from sqlalchemy import Column, String, ForeignKey, Float, Enum, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import func
from .database import Base
from ..schemas.item_schemas import ItemStatus


class Item(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)
    rate = Column(Float, nullable=False)
    status = Column(Enum(ItemStatus), nullable=False, default=ItemStatus.AVAILABLE)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True, onupdate=func.now())

    # Define one-to-one relationship with Contract
    contract = relationship('Contract', back_populates='item', uselist=False)


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    start_date = Column(TIMESTAMP(timezone=True), nullable=True)
    end_date = Column(TIMESTAMP(timezone=True), nullable=True)
    terms = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True, onupdate=func.now())

    # Define the back reference for the relationship
    item_id = Column(UUID(as_uuid=True), ForeignKey(Item.id), unique=True, nullable=False)
    item = relationship('Item', back_populates='contract')
    tenant_id = Column(UUID(as_uuid=True), ForeignKey('tenants.id'), unique=True, nullable=False)


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    address_1 = Column(String, nullable=False)
    address_2 = Column(String, nullable=False)
    phone_1 = Column(String, nullable=False)
    phone_2 = Column(String, nullable=False)
    CNIC = Column(String(length=15), nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True, onupdate=func.now())


class TenantIn(Base):
    __tablename__ = "tenants_in"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    details = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True, onupdate=func.now())

    # Define the back reference for the relationship
    contract_id = Column(UUID(as_uuid=True), ForeignKey('contracts.id'), unique=True, nullable=False)


class TenantOut(Base):
    __tablename__ = "tenants_out"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    details = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True, onupdate=func.now())

    # Define the back reference for the relationship
    contract_id = Column(UUID(as_uuid=True), ForeignKey('contracts.id'), unique=True, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True, nullable=False)
    username = Column(String(255), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
