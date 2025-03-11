from typing import List, Optional

from sqlalchemy import ARRAY, BigInteger, Boolean, Column, Date, DateTime, Double, Enum, ForeignKeyConstraint, Index, Integer, JSON, LargeBinary, Numeric, PrimaryKeyConstraint, SmallInteger, String, Table, Text, UniqueConstraint, Uuid, text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
import uuid

class Base(DeclarativeBase):
    pass


class AdminEventEntity(Base):
    __tablename__ = 'admin_event_entity'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='constraint_admin_event_entity'),
        Index('idx_admin_event_time', 'realm_id', 'admin_event_time')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    admin_event_time: Mapped[Optional[int]] = mapped_column(BigInteger)
    realm_id: Mapped[Optional[str]] = mapped_column(String(255))
    operation_type: Mapped[Optional[str]] = mapped_column(String(255))
    auth_realm_id: Mapped[Optional[str]] = mapped_column(String(255))
    auth_client_id: Mapped[Optional[str]] = mapped_column(String(255))
    auth_user_id: Mapped[Optional[str]] = mapped_column(String(255))
    ip_address: Mapped[Optional[str]] = mapped_column(String(255))
    resource_path: Mapped[Optional[str]] = mapped_column(String(2550))
    representation: Mapped[Optional[str]] = mapped_column(Text)
    error: Mapped[Optional[str]] = mapped_column(String(255))
    resource_type: Mapped[Optional[str]] = mapped_column(String(64))
    details_json: Mapped[Optional[str]] = mapped_column(Text)


class AuthenticatorConfigEntry(Base):
    __tablename__ = 'authenticator_config_entry'
    __table_args__ = (
        PrimaryKeyConstraint('authenticator_id', 'name', name='constraint_auth_cfg_pk'),
    )

    authenticator_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[Optional[str]] = mapped_column(Text)


class BrandFavoriteInfluencer(Base):
    __tablename__ = 'brand_favorite_influencer'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='brand_favorite_influencer_pkey'),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    influencer_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)


class BrokerLink(Base):
    __tablename__ = 'broker_link'
    __table_args__ = (
        PrimaryKeyConstraint('identity_provider', 'user_id', name='constr_broker_link_pk'),
    )

    identity_provider: Mapped[str] = mapped_column(String(255), primary_key=True)
    realm_id: Mapped[str] = mapped_column(String(36))
    user_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    storage_provider_id: Mapped[Optional[str]] = mapped_column(String(255))
    broker_user_id: Mapped[Optional[str]] = mapped_column(String(255))
    broker_username: Mapped[Optional[str]] = mapped_column(String(255))
    token: Mapped[Optional[str]] = mapped_column(Text)


class Campaign(Base):
    __tablename__ = 'campaign'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='campaign_pkey'),
        Index('idx_campaign_application_deadline', 'application_deadline'),
        Index('idx_campaign_brand_id', 'brand_id'),
        Index('idx_campaign_budget_per_influencer', 'budget_per_influencer'),
        Index('idx_campaign_budget_total', 'budget_total'),
        Index('idx_campaign_campaign_category', 'campaign_category'),
        Index('idx_campaign_campaign_type', 'campaign_type'),
        Index('idx_campaign_end_date', 'end_date'),
        Index('idx_campaign_max_influencers', 'max_influencers'),
        Index('idx_campaign_min_influencers', 'min_influencers'),
        Index('idx_campaign_start_date', 'start_date'),
        Index('idx_campaign_status', 'status'),
        Index('idx_campaign_visibility', 'visibility')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    briefing: Mapped[dict] = mapped_column(JSONB)
    campaign_type: Mapped[str] = mapped_column(String(50))
    campaign_category: Mapped[str] = mapped_column(String(50))
    budget_total: Mapped[decimal.Decimal] = mapped_column(Numeric(12, 2))
    budget_per_influencer: Mapped[decimal.Decimal] = mapped_column(Numeric(12, 2))
    min_influencers: Mapped[int] = mapped_column(Integer)
    max_influencers: Mapped[int] = mapped_column(Integer)
    start_date: Mapped[int] = mapped_column(Integer)
    end_date: Mapped[int] = mapped_column(Integer)
    url_call_to_action: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(Enum('DRAFT', 'PENDING_APPROVAL', 'ACTIVE', 'PAUSED', 'COMPLETED', 'CANCELLED', name='campaignstatus'))
    visibility: Mapped[str] = mapped_column(Enum('PRIVATE', 'PUBLIC', 'INVITED', name='campaignvisibility'))
    created_by: Mapped[uuid.UUID] = mapped_column(Uuid)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    application_deadline: Mapped[Optional[int]] = mapped_column(Integer)
    profile_image_url: Mapped[Optional[str]] = mapped_column(Text)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    campaign_activity_log: Mapped[List['CampaignActivityLog']] = relationship('CampaignActivityLog', back_populates='campaign')
    campaign_chat: Mapped[List['CampaignChat']] = relationship('CampaignChat', back_populates='campaign')
    campaign_deliverable_template: Mapped[List['CampaignDeliverableTemplate']] = relationship('CampaignDeliverableTemplate', back_populates='campaign')
    campaign_invite: Mapped[List['CampaignInvite']] = relationship('CampaignInvite', back_populates='campaign')
    campaign_match: Mapped[List['CampaignMatch']] = relationship('CampaignMatch', back_populates='campaign')
    campaign_material: Mapped[List['CampaignMaterial']] = relationship('CampaignMaterial', back_populates='campaign')
    campaign_requirement: Mapped[List['CampaignRequirement']] = relationship('CampaignRequirement', back_populates='campaign')
    campaign_targeting: Mapped[List['CampaignTargeting']] = relationship('CampaignTargeting', back_populates='campaign')
    contracted_campaign: Mapped[List['ContractedCampaign']] = relationship('ContractedCampaign', back_populates='campaign')


class CartEntity(Base):
    __tablename__ = 'cart_entity'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='cart_entity_pkey'),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    status: Mapped[str] = mapped_column(Enum('ACTIVE', 'INACTIVE', 'COMPLETED', 'CANCELLED', name='cartstatus'))
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    session_id: Mapped[Optional[str]] = mapped_column(String)
    type: Mapped[Optional[str]] = mapped_column(String)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class Client(Base):
    __tablename__ = 'client'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='constraint_7'),
        UniqueConstraint('realm_id', 'client_id', name='uk_b71cjlbenv945rb6gcon438at'),
        Index('idx_client_id', 'client_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    enabled: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    full_scope_allowed: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    public_client: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    bearer_only: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    surrogate_auth_required: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    frontchannel_logout: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    consent_required: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    service_accounts_enabled: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    standard_flow_enabled: Mapped[bool] = mapped_column(Boolean, server_default=text('true'))
    implicit_flow_enabled: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    direct_access_grants_enabled: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    always_display_in_console: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    client_id: Mapped[Optional[str]] = mapped_column(String(255))
    not_before: Mapped[Optional[int]] = mapped_column(Integer)
    secret: Mapped[Optional[str]] = mapped_column(String(255))
    base_url: Mapped[Optional[str]] = mapped_column(String(255))
    management_url: Mapped[Optional[str]] = mapped_column(String(255))
    realm_id: Mapped[Optional[str]] = mapped_column(String(36))
    protocol: Mapped[Optional[str]] = mapped_column(String(255))
    node_rereg_timeout: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    name: Mapped[Optional[str]] = mapped_column(String(255))
    client_authenticator_type: Mapped[Optional[str]] = mapped_column(String(255))
    root_url: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    registration_token: Mapped[Optional[str]] = mapped_column(String(255))

    client_attributes: Mapped[List['ClientAttributes']] = relationship('ClientAttributes', back_populates='client')
    client_node_registrations: Mapped[List['ClientNodeRegistrations']] = relationship('ClientNodeRegistrations', back_populates='client')
    protocol_mapper: Mapped[List['ProtocolMapper']] = relationship('ProtocolMapper', back_populates='client')
    redirect_uris: Mapped[List['RedirectUris']] = relationship('RedirectUris', back_populates='client')
    scope_mapping: Mapped[List['ScopeMapping']] = relationship('ScopeMapping', back_populates='client')
    web_origins: Mapped[List['WebOrigins']] = relationship('WebOrigins', back_populates='client')


class ClientAuthFlowBindings(Base):
    __tablename__ = 'client_auth_flow_bindings'
    __table_args__ = (
        PrimaryKeyConstraint('client_id', 'binding_name', name='c_cli_flow_bind'),
    )

    client_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    binding_name: Mapped[str] = mapped_column(String(255), primary_key=True)
    flow_id: Mapped[Optional[str]] = mapped_column(String(36))


class ClientScope(Base):
    __tablename__ = 'client_scope'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_cli_template'),
        UniqueConstraint('realm_id', 'name', name='uk_cli_scope'),
        Index('idx_realm_clscope', 'realm_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    realm_id: Mapped[Optional[str]] = mapped_column(String(36))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    protocol: Mapped[Optional[str]] = mapped_column(String(255))

    client_scope_attributes: Mapped[List['ClientScopeAttributes']] = relationship('ClientScopeAttributes', back_populates='scope')
    client_scope_role_mapping: Mapped[List['ClientScopeRoleMapping']] = relationship('ClientScopeRoleMapping', back_populates='scope')
    protocol_mapper: Mapped[List['ProtocolMapper']] = relationship('ProtocolMapper', back_populates='client_scope')


class ClientScopeClient(Base):
    __tablename__ = 'client_scope_client'
    __table_args__ = (
        PrimaryKeyConstraint('client_id', 'scope_id', name='c_cli_scope_bind'),
        Index('idx_cl_clscope', 'scope_id'),
        Index('idx_clscope_cl', 'client_id')
    )

    client_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    scope_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    default_scope: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))


t_databasechangelog = Table(
    'databasechangelog', Base.metadata,
    Column('id', String(255), nullable=False),
    Column('author', String(255), nullable=False),
    Column('filename', String(255), nullable=False),
    Column('dateexecuted', DateTime, nullable=False),
    Column('orderexecuted', Integer, nullable=False),
    Column('exectype', String(10), nullable=False),
    Column('md5sum', String(35)),
    Column('description', String(255)),
    Column('comments', String(255)),
    Column('tag', String(255)),
    Column('liquibase', String(20)),
    Column('contexts', String(255)),
    Column('labels', String(255)),
    Column('deployment_id', String(10))
)


class Databasechangeloglock(Base):
    __tablename__ = 'databasechangeloglock'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='databasechangeloglock_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    locked: Mapped[bool] = mapped_column(Boolean)
    lockgranted: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    lockedby: Mapped[Optional[str]] = mapped_column(String(255))


class EventEntity(Base):
    __tablename__ = 'event_entity'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='constraint_4'),
        Index('idx_event_time', 'realm_id', 'event_time')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    client_id: Mapped[Optional[str]] = mapped_column(String(255))
    details_json: Mapped[Optional[str]] = mapped_column(String(2550))
    error: Mapped[Optional[str]] = mapped_column(String(255))
    ip_address: Mapped[Optional[str]] = mapped_column(String(255))
    realm_id: Mapped[Optional[str]] = mapped_column(String(255))
    session_id: Mapped[Optional[str]] = mapped_column(String(255))
    event_time: Mapped[Optional[int]] = mapped_column(BigInteger)
    type: Mapped[Optional[str]] = mapped_column(String(255))
    user_id: Mapped[Optional[str]] = mapped_column(String(255))
    details_json_long_value: Mapped[Optional[str]] = mapped_column(Text)


class FedUserAttribute(Base):
    __tablename__ = 'fed_user_attribute'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='constr_fed_user_attr_pk'),
        Index('fed_user_attr_long_values', 'long_value_hash', 'name'),
        Index('fed_user_attr_long_values_lower_case', 'long_value_hash_lower_case', 'name'),
        Index('idx_fu_attribute', 'user_id', 'realm_id', 'name')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[str] = mapped_column(String(255))
    realm_id: Mapped[str] = mapped_column(String(36))
    storage_provider_id: Mapped[Optional[str]] = mapped_column(String(36))
    value: Mapped[Optional[str]] = mapped_column(String(2024))
    long_value_hash: Mapped[Optional[bytes]] = mapped_column(LargeBinary)
    long_value_hash_lower_case: Mapped[Optional[bytes]] = mapped_column(LargeBinary)
    long_value: Mapped[Optional[str]] = mapped_column(Text)


class FedUserConsent(Base):
    __tablename__ = 'fed_user_consent'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='constr_fed_user_consent_pk'),
        Index('idx_fu_cnsnt_ext', 'user_id', 'client_storage_provider', 'external_client_id'),
        Index('idx_fu_consent', 'user_id', 'client_id'),
        Index('idx_fu_consent_ru', 'realm_id', 'user_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(255))
    realm_id: Mapped[str] = mapped_column(String(36))
    client_id: Mapped[Optional[str]] = mapped_column(String(255))
    storage_provider_id: Mapped[Optional[str]] = mapped_column(String(36))
    created_date: Mapped[Optional[int]] = mapped_column(BigInteger)
    last_updated_date: Mapped[Optional[int]] = mapped_column(BigInteger)
    client_storage_provider: Mapped[Optional[str]] = mapped_column(String(36))
    external_client_id: Mapped[Optional[str]] = mapped_column(String(255))


class FedUserConsentClScope(Base):
    __tablename__ = 'fed_user_consent_cl_scope'
    __table_args__ = (
        PrimaryKeyConstraint('user_consent_id', 'scope_id', name='constraint_fgrntcsnt_clsc_pm'),
    )

    user_consent_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    scope_id: Mapped[str] = mapped_column(String(36), primary_key=True)


class FedUserCredential(Base):
    __tablename__ = 'fed_user_credential'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='constr_fed_user_cred_pk'),
        Index('idx_fu_credential', 'user_id', 'type'),
        Index('idx_fu_credential_ru', 'realm_id', 'user_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(255))
    realm_id: Mapped[str] = mapped_column(String(36))
    salt: Mapped[Optional[bytes]] = mapped_column(LargeBinary)
    type: Mapped[Optional[str]] = mapped_column(String(255))
    created_date: Mapped[Optional[int]] = mapped_column(BigInteger)
    storage_provider_id: Mapped[Optional[str]] = mapped_column(String(36))
    user_label: Mapped[Optional[str]] = mapped_column(String(255))
    secret_data: Mapped[Optional[str]] = mapped_column(Text)
    credential_data: Mapped[Optional[str]] = mapped_column(Text)
    priority: Mapped[Optional[int]] = mapped_column(Integer)


class FedUserGroupMembership(Base):
    __tablename__ = 'fed_user_group_membership'
    __table_args__ = (
        PrimaryKeyConstraint('group_id', 'user_id', name='constr_fed_user_group'),
        Index('idx_fu_group_membership', 'user_id', 'group_id'),
        Index('idx_fu_group_membership_ru', 'realm_id', 'user_id')
    )

    group_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    realm_id: Mapped[str] = mapped_column(String(36))
    storage_provider_id: Mapped[Optional[str]] = mapped_column(String(36))


class FedUserRequiredAction(Base):
    __tablename__ = 'fed_user_required_action'
    __table_args__ = (
        PrimaryKeyConstraint('required_action', 'user_id', name='constr_fed_required_action'),
        Index('idx_fu_required_action', 'user_id', 'required_action'),
        Index('idx_fu_required_action_ru', 'realm_id', 'user_id')
    )

    required_action: Mapped[str] = mapped_column(String(255), primary_key=True, server_default=text("' '::character varying"))
    user_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    realm_id: Mapped[str] = mapped_column(String(36))
    storage_provider_id: Mapped[Optional[str]] = mapped_column(String(36))


class FedUserRoleMapping(Base):
    __tablename__ = 'fed_user_role_mapping'
    __table_args__ = (
        PrimaryKeyConstraint('role_id', 'user_id', name='constr_fed_user_role'),
        Index('idx_fu_role_mapping', 'user_id', 'role_id'),
        Index('idx_fu_role_mapping_ru', 'realm_id', 'user_id')
    )

    role_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    realm_id: Mapped[str] = mapped_column(String(36))
    storage_provider_id: Mapped[Optional[str]] = mapped_column(String(36))


class FederatedUser(Base):
    __tablename__ = 'federated_user'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='constr_federated_user'),
    )

    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    realm_id: Mapped[str] = mapped_column(String(36))
    storage_provider_id: Mapped[Optional[str]] = mapped_column(String(255))


class GoalSetting(Base):
    __tablename__ = 'goal_setting'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='goal_setting_pkey'),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    goal_type: Mapped[str] = mapped_column(Enum('SALES', 'CAMPAIGNS', 'CONTENT', name='goalsettingstype'))
    min_value: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    description: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)


class InfluencerAuthorization(Base):
    __tablename__ = 'influencer_authorization'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='influencer_authorization_pkey'),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    influencer_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    is_active: Mapped[bool] = mapped_column(Boolean)
    status: Mapped[str] = mapped_column(Enum('PENDING', 'ACCEPTED', 'REJECTED', name='authorizationstatus'))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class JobConfig(Base):
    __tablename__ = 'job_config'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='job_config_pkey'),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    type: Mapped[str] = mapped_column(Enum('GOAL_VERIFICATION', 'REACTIVATION_MONITOR', name='jobconfigstype'))
    duration: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class KeycloakGroup(Base):
    __tablename__ = 'keycloak_group'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='constraint_group'),
        UniqueConstraint('realm_id', 'parent_group', 'name', name='sibling_names')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    parent_group: Mapped[str] = mapped_column(String(36))
    type: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    name: Mapped[Optional[str]] = mapped_column(String(255))
    realm_id: Mapped[Optional[str]] = mapped_column(String(36))

    group_attribute: Mapped[List['GroupAttribute']] = relationship('GroupAttribute', back_populates='group')
    group_role_mapping: Mapped[List['GroupRoleMapping']] = relationship('GroupRoleMapping', back_populates='group')


class Links(Base):
    __tablename__ = 'links'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='links_pkey'),
        Index('ix_links_id', 'id')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    type: Mapped[str] = mapped_column(Enum('INFLUENCER', 'BRAND', 'CLIENT', name='urltype'))
    base_id: Mapped[str] = mapped_column(String)
    comp_id: Mapped[str] = mapped_column(String)
    target_id: Mapped[str] = mapped_column(String)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)


class MigrationModel(Base):
    __tablename__ = 'migration_model'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='constraint_migmod'),
        Index('idx_update_time', 'update_time')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    update_time: Mapped[int] = mapped_column(BigInteger, server_default=text('0'))
    version: Mapped[Optional[str]] = mapped_column(String(36))


class Offer(Base):
    __tablename__ = 'offer'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='offer_pkey'),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    product_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    title: Mapped[str] = mapped_column(String)
    full_title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    full_price: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    is_promotion: Mapped[bool] = mapped_column(Boolean)
    sku: Mapped[str] = mapped_column(String)
    ref: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String)
    is_highlighted: Mapped[bool] = mapped_column(Boolean)
    is_active: Mapped[bool] = mapped_column(Boolean)
    category: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    cash_price: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    discount_percentage: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(3, 0))
    discount_value: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    cash_discount_percentage: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(3, 0))
    promotional_price: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    short_url: Mapped[Optional[str]] = mapped_column(String)
    tracking_code: Mapped[Optional[str]] = mapped_column(String)
    subcategory: Mapped[Optional[str]] = mapped_column(String)
    subsubcategory: Mapped[Optional[str]] = mapped_column(String)
    size: Mapped[Optional[str]] = mapped_column(String)
    color: Mapped[Optional[str]] = mapped_column(String)
    weight: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    length: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    width: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    height: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    image1: Mapped[Optional[str]] = mapped_column(String)
    image2: Mapped[Optional[str]] = mapped_column(String)
    image3: Mapped[Optional[str]] = mapped_column(String)
    image4: Mapped[Optional[str]] = mapped_column(String)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    offer_influencer: Mapped[List['OfferInfluencer']] = relationship('OfferInfluencer', back_populates='offer')


class OfflineClientSession(Base):
    __tablename__ = 'offline_client_session'
    __table_args__ = (
        PrimaryKeyConstraint('user_session_id', 'client_id', 'client_storage_provider', 'external_client_id', 'offline_flag', name='constraint_offl_cl_ses_pk3'),
    )

    user_session_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    client_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    offline_flag: Mapped[str] = mapped_column(String(4), primary_key=True)
    client_storage_provider: Mapped[str] = mapped_column(String(36), primary_key=True, server_default=text("'local'::character varying"))
    external_client_id: Mapped[str] = mapped_column(String(255), primary_key=True, server_default=text("'local'::character varying"))
    timestamp: Mapped[Optional[int]] = mapped_column(Integer)
    data: Mapped[Optional[str]] = mapped_column(Text)
    version: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))


class OfflineUserSession(Base):
    __tablename__ = 'offline_user_session'
    __table_args__ = (
        PrimaryKeyConstraint('user_session_id', 'offline_flag', name='constraint_offl_us_ses_pk2'),
        Index('idx_offline_uss_by_broker_session_id', 'broker_session_id', 'realm_id'),
        Index('idx_offline_uss_by_last_session_refresh', 'realm_id', 'offline_flag', 'last_session_refresh'),
        Index('idx_offline_uss_by_user', 'user_id', 'realm_id', 'offline_flag')
    )

    user_session_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(255))
    realm_id: Mapped[str] = mapped_column(String(36))
    created_on: Mapped[int] = mapped_column(Integer)
    offline_flag: Mapped[str] = mapped_column(String(4), primary_key=True)
    last_session_refresh: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    data: Mapped[Optional[str]] = mapped_column(Text)
    broker_session_id: Mapped[Optional[str]] = mapped_column(String(1024))
    version: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))


class Orders(Base):
    __tablename__ = 'orders'
    __table_args__ = (
        PrimaryKeyConstraint('order_id', name='orders_pkey'),
    )

    order_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    address_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    order_number: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    customer_name: Mapped[str] = mapped_column(String)
    customer_email: Mapped[str] = mapped_column(String)
    delivery_address: Mapped[str] = mapped_column(String)
    delivery_city: Mapped[str] = mapped_column(String)
    delivery_state: Mapped[str] = mapped_column(String)
    delivery_postal_code: Mapped[str] = mapped_column(String)
    payment_method: Mapped[str] = mapped_column(String)
    sub_total: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    shipping_cost: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    discount_amount: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    gift_card_amount: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    total_amount: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    customer_phone: Mapped[Optional[str]] = mapped_column(String)
    payment_status: Mapped[Optional[str]] = mapped_column(String)
    card_last_digits: Mapped[Optional[str]] = mapped_column(String)
    installments: Mapped[Optional[int]] = mapped_column(Integer)
    gift_card_code: Mapped[Optional[str]] = mapped_column(String)
    notes: Mapped[Optional[str]] = mapped_column(String)
    payment_id: Mapped[Optional[str]] = mapped_column(String)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    order_brands: Mapped[List['OrderBrands']] = relationship('OrderBrands', back_populates='order')
    order_items: Mapped[List['OrderItems']] = relationship('OrderItems', back_populates='order')


class Org(Base):
    __tablename__ = 'org'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='ORG_pkey'),
        UniqueConstraint('group_id', name='uk_org_group'),
        UniqueConstraint('realm_id', 'alias', name='uk_org_alias'),
        UniqueConstraint('realm_id', 'name', name='uk_org_name')
    )

    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    enabled: Mapped[bool] = mapped_column(Boolean)
    realm_id: Mapped[str] = mapped_column(String(255))
    group_id: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    alias: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(String(4000))
    redirect_url: Mapped[Optional[str]] = mapped_column(String(2048))


class OrgDomain(Base):
    __tablename__ = 'org_domain'
    __table_args__ = (
        PrimaryKeyConstraint('id', 'name', name='ORG_DOMAIN_pkey'),
        Index('idx_org_domain_org_id', 'org_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    verified: Mapped[bool] = mapped_column(Boolean)
    org_id: Mapped[str] = mapped_column(String(255))


class Products(Base):
    __tablename__ = 'products'
    __table_args__ = (
        PrimaryKeyConstraint('product_id', name='products_pkey'),
    )

    product_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    brand_ambassador_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    title: Mapped[str] = mapped_column(String)
    status: Mapped[bool] = mapped_column(Boolean)
    brand_name: Mapped[str] = mapped_column(String)
    full_price: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    is_promotion: Mapped[bool] = mapped_column(Boolean)
    cash_price: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    sku: Mapped[str] = mapped_column(String)
    ref: Mapped[str] = mapped_column(String)
    quantity: Mapped[int] = mapped_column(Integer)
    min_quantity: Mapped[int] = mapped_column(Integer)
    max_quantity: Mapped[int] = mapped_column(Integer)
    category: Mapped[str] = mapped_column(String)
    ncm: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    description: Mapped[Optional[str]] = mapped_column(String)
    discount_percentage: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(3, 0))
    discount_value: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    promotional_price: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    cash_discount_percentage: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(3, 0))
    specification: Mapped[Optional[dict]] = mapped_column(JSON)
    height: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    width: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    length: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    weight: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    color: Mapped[Optional[str]] = mapped_column(String)
    size: Mapped[Optional[str]] = mapped_column(String)
    subcategory: Mapped[Optional[str]] = mapped_column(String)
    subsubcategory: Mapped[Optional[str]] = mapped_column(String)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    favorite_products: Mapped[List['FavoriteProducts']] = relationship('FavoriteProducts', back_populates='product')
    media: Mapped[List['Media']] = relationship('Media', back_populates='product')


class Realm(Base):
    __tablename__ = 'realm'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='constraint_4a'),
        UniqueConstraint('name', name='uk_orvsdmla56612eaefiq6wl5oi'),
        Index('idx_realm_master_adm_cli', 'master_admin_client')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    enabled: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    events_enabled: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    registration_allowed: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    remember_me: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    reset_password_allowed: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    social: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    update_profile_on_soc_login: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    verify_email: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    internationalization_enabled: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    reg_email_as_username: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    admin_events_enabled: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    admin_events_details_enabled: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    edit_username_allowed: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    revoke_refresh_token: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    login_with_email_allowed: Mapped[bool] = mapped_column(Boolean, server_default=text('true'))
    duplicate_emails_allowed: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    allow_user_managed_access: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    sso_max_lifespan_remember_me: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    sso_idle_timeout_remember_me: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    access_code_lifespan: Mapped[Optional[int]] = mapped_column(Integer)
    user_action_lifespan: Mapped[Optional[int]] = mapped_column(Integer)
    access_token_lifespan: Mapped[Optional[int]] = mapped_column(Integer)
    account_theme: Mapped[Optional[str]] = mapped_column(String(255))
    admin_theme: Mapped[Optional[str]] = mapped_column(String(255))
    email_theme: Mapped[Optional[str]] = mapped_column(String(255))
    events_expiration: Mapped[Optional[int]] = mapped_column(BigInteger)
    login_theme: Mapped[Optional[str]] = mapped_column(String(255))
    name: Mapped[Optional[str]] = mapped_column(String(255))
    not_before: Mapped[Optional[int]] = mapped_column(Integer)
    password_policy: Mapped[Optional[str]] = mapped_column(String(2550))
    ssl_required: Mapped[Optional[str]] = mapped_column(String(255))
    sso_idle_timeout: Mapped[Optional[int]] = mapped_column(Integer)
    sso_max_lifespan: Mapped[Optional[int]] = mapped_column(Integer)
    master_admin_client: Mapped[Optional[str]] = mapped_column(String(36))
    login_lifespan: Mapped[Optional[int]] = mapped_column(Integer)
    default_locale: Mapped[Optional[str]] = mapped_column(String(255))
    otp_policy_counter: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    otp_policy_window: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('1'))
    otp_policy_period: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('30'))
    otp_policy_digits: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('6'))
    otp_policy_alg: Mapped[Optional[str]] = mapped_column(String(36), server_default=text("'HmacSHA1'::character varying"))
    otp_policy_type: Mapped[Optional[str]] = mapped_column(String(36), server_default=text("'totp'::character varying"))
    browser_flow: Mapped[Optional[str]] = mapped_column(String(36))
    registration_flow: Mapped[Optional[str]] = mapped_column(String(36))
    direct_grant_flow: Mapped[Optional[str]] = mapped_column(String(36))
    reset_credentials_flow: Mapped[Optional[str]] = mapped_column(String(36))
    client_auth_flow: Mapped[Optional[str]] = mapped_column(String(36))
    offline_session_idle_timeout: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    access_token_life_implicit: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    docker_auth_flow: Mapped[Optional[str]] = mapped_column(String(36))
    refresh_token_max_reuse: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    default_role: Mapped[Optional[str]] = mapped_column(String(255))

    authentication_flow: Mapped[List['AuthenticationFlow']] = relationship('AuthenticationFlow', back_populates='realm')
    authenticator_config: Mapped[List['AuthenticatorConfig']] = relationship('AuthenticatorConfig', back_populates='realm')
    client_initial_access: Mapped[List['ClientInitialAccess']] = relationship('ClientInitialAccess', back_populates='realm')
    component: Mapped[List['Component']] = relationship('Component', back_populates='realm')
    default_client_scope: Mapped[List['DefaultClientScope']] = relationship('DefaultClientScope', back_populates='realm')
    identity_provider: Mapped[List['IdentityProvider']] = relationship('IdentityProvider', back_populates='realm')
    identity_provider_mapper: Mapped[List['IdentityProviderMapper']] = relationship('IdentityProviderMapper', back_populates='realm')
    keycloak_role: Mapped[List['KeycloakRole']] = relationship('KeycloakRole', back_populates='realm_')
    realm_attribute: Mapped[List['RealmAttribute']] = relationship('RealmAttribute', back_populates='realm')
    realm_default_groups: Mapped[List['RealmDefaultGroups']] = relationship('RealmDefaultGroups', back_populates='realm')
    realm_enabled_event_types: Mapped[List['RealmEnabledEventTypes']] = relationship('RealmEnabledEventTypes', back_populates='realm')
    realm_events_listeners: Mapped[List['RealmEventsListeners']] = relationship('RealmEventsListeners', back_populates='realm')
    realm_required_credential: Mapped[List['RealmRequiredCredential']] = relationship('RealmRequiredCredential', back_populates='realm')
    realm_smtp_config: Mapped[List['RealmSmtpConfig']] = relationship('RealmSmtpConfig', back_populates='realm')
    realm_supported_locales: Mapped[List['RealmSupportedLocales']] = relationship('RealmSupportedLocales', back_populates='realm')
    required_action_provider: Mapped[List['RequiredActionProvider']] = relationship('RequiredActionProvider', back_populates='realm')
    user_federation_provider: Mapped[List['UserFederationProvider']] = relationship('UserFederationProvider', back_populates='realm')
    authentication_execution: Mapped[List['AuthenticationExecution']] = relationship('AuthenticationExecution', back_populates='realm')
    user_federation_mapper: Mapped[List['UserFederationMapper']] = relationship('UserFederationMapper', back_populates='realm')


class RealmLocalizations(Base):
    __tablename__ = 'realm_localizations'
    __table_args__ = (
        PrimaryKeyConstraint('realm_id', 'locale', name='realm_localizations_pkey'),
    )

    realm_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    locale: Mapped[str] = mapped_column(String(255), primary_key=True)
    texts: Mapped[str] = mapped_column(Text)


class RequiredActionConfig(Base):
    __tablename__ = 'required_action_config'
    __table_args__ = (
        PrimaryKeyConstraint('required_action_id', 'name', name='constraint_req_act_cfg_pk'),
    )

    required_action_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[Optional[str]] = mapped_column(Text)


class ResourceServer(Base):
    __tablename__ = 'resource_server'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_resource_server'),
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    allow_rs_remote_mgmt: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    policy_enforce_mode: Mapped[int] = mapped_column(SmallInteger)
    decision_strategy: Mapped[int] = mapped_column(SmallInteger, server_default=text('1'))

    resource_server_policy: Mapped[List['ResourceServerPolicy']] = relationship('ResourceServerPolicy', back_populates='resource_server')
    resource_server_resource: Mapped[List['ResourceServerResource']] = relationship('ResourceServerResource', back_populates='resource_server')
    resource_server_scope: Mapped[List['ResourceServerScope']] = relationship('ResourceServerScope', back_populates='resource_server')
    resource_server_perm_ticket: Mapped[List['ResourceServerPermTicket']] = relationship('ResourceServerPermTicket', back_populates='resource_server')


class RevokedToken(Base):
    __tablename__ = 'revoked_token'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='constraint_rt'),
        Index('idx_rev_token_on_expire', 'expire')
    )

    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    expire: Mapped[int] = mapped_column(BigInteger)


class SubscriptionInfluencer(Base):
    __tablename__ = 'subscription_influencer'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='subscription_influencer_pkey'),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    influencer_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    status: Mapped[str] = mapped_column(Enum('ACTIVE', 'INACTIVE', 'PENDING', name='subscriptioninfluencersstatus'))
    next_verification_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    subscription_status_log: Mapped[List['SubscriptionStatusLog']] = relationship('SubscriptionStatusLog', back_populates='subscription')
    subscription_verification: Mapped[List['SubscriptionVerification']] = relationship('SubscriptionVerification', back_populates='subscription')


class TokenConfiguration(Base):
    __tablename__ = 'token_configuration'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='token_configuration_pkey'),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_type: Mapped[str] = mapped_column(Enum('BRAND', 'INFLUENCER', 'CONSUMER', name='tokenusertype'))
    tokens_per_cycle: Mapped[int] = mapped_column(Integer)
    cycle_duration_days: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)


class TokenCycleRenewalGoal(Base):
    __tablename__ = 'token_cycle_renewal_goal'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='token_cycle_renewal_goal_pkey'),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_type: Mapped[str] = mapped_column(Enum('BRAND', 'INFLUENCER', 'CONSUMER', name='tokenusertype'))
    goal_type: Mapped[str] = mapped_column(Enum('SALES', 'CAMPAIGNS', 'CONTENT', name='goalsettingstype'))
    tokens_reward: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)


class TokenNotification(Base):
    __tablename__ = 'token_notification'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='token_notification_pkey'),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    user_type: Mapped[str] = mapped_column(Enum('BRAND', 'INFLUENCER', 'CONSUMER', name='tokenusertype'))
    token_notification_type: Mapped[str] = mapped_column(Enum('LOW_TOKENS', 'DEPLETED', 'CYCLE_RENEWED', 'PURCHASE_SUCCESS', name='tokennotificationtype'))
    message: Mapped[str] = mapped_column(Text)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    is_read: Mapped[Optional[bool]] = mapped_column(Boolean)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)


class TokenPlan(Base):
    __tablename__ = 'token_plan'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='token_plan_pkey'),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    token_amount: Mapped[int] = mapped_column(Integer)
    price: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    user_type: Mapped[str] = mapped_column(Enum('BRAND', 'INFLUENCER', 'CONSUMER', name='tokenusertype'))
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    description: Mapped[Optional[str]] = mapped_column(Text)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    token_purchase: Mapped[List['TokenPurchase']] = relationship('TokenPurchase', back_populates='token_plan')


class TokenUserCycle(Base):
    __tablename__ = 'token_user_cycle'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='token_user_cycle_pkey'),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    user_type: Mapped[str] = mapped_column(Enum('BRAND', 'INFLUENCER', 'CONSUMER', name='tokenusertype'))
    cycle_start_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    cycle_end_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    total_tokens: Mapped[int] = mapped_column(Integer)
    remaining_tokens: Mapped[int] = mapped_column(Integer)
    user_token_cycles_status: Mapped[str] = mapped_column(Enum('ACTIVE', 'EXPIRED', 'DEPLETED', name='usertokencyclesstatus'))
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    token_consumption_history: Mapped[List['TokenConsumptionHistory']] = relationship('TokenConsumptionHistory', back_populates='user_token_cycle')


class TrackingEvents(Base):
    __tablename__ = 'tracking_events'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='tracking_events_pkey'),
        Index('ix_tracking_events_id', 'id'),
        Index('ix_tracking_events_tracking_code', 'tracking_code')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    tracking_code: Mapped[str] = mapped_column(String)
    event_type: Mapped[str] = mapped_column(String)
    source_user_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    source_type: Mapped[str] = mapped_column(String)
    expires_at: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    platform: Mapped[Optional[str]] = mapped_column(String)
    enterprise_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    influencer_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    campaign_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    product_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    url_instagram_story: Mapped[Optional[str]] = mapped_column(String)
    url_instagram_post: Mapped[Optional[str]] = mapped_column(String)
    url_instagram_reels: Mapped[Optional[str]] = mapped_column(String)
    url_instagram_carrosel: Mapped[Optional[str]] = mapped_column(String)
    url_tiktok_feed_video: Mapped[Optional[str]] = mapped_column(String)
    url_tiktok_live: Mapped[Optional[str]] = mapped_column(String)
    url_tiktok_stories: Mapped[Optional[str]] = mapped_column(String)
    url_youtube: Mapped[Optional[str]] = mapped_column(String)
    metadata_at: Mapped[Optional[str]] = mapped_column(String)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    tracking_interactions: Mapped[List['TrackingInteractions']] = relationship('TrackingInteractions', back_populates='event')


class TrackingUrls(Base):
    __tablename__ = 'tracking_urls'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='tracking_urls_pkey'),
        Index('ak_urls_short_url', 'short_url'),
        Index('ak_urls_tracking_code', 'tracking_code'),
        Index('ak_urls_url', 'url'),
        Index('ix_tracking_urls_id', 'id')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    type: Mapped[str] = mapped_column(Enum('INFLUENCER', 'BRAND', 'CLIENT', name='urltype'))
    link_id: Mapped[str] = mapped_column(String)
    tracking_code: Mapped[str] = mapped_column(String)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    influencer_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    content_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    platform: Mapped[Optional[str]] = mapped_column(String)
    product_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    brand_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    campaign_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    channel: Mapped[Optional[str]] = mapped_column(String)
    client_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    program_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    source: Mapped[Optional[str]] = mapped_column(String)
    url: Mapped[Optional[str]] = mapped_column(String)
    short_url: Mapped[Optional[str]] = mapped_column(String)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)


class UserEntity(Base):
    __tablename__ = 'user_entity'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='constraint_fb'),
        UniqueConstraint('realm_id', 'email_constraint', name='uk_dykn684sl8up1crfei6eckhd7'),
        UniqueConstraint('realm_id', 'username', name='uk_ru8tt6t700s9v50bu18ws5ha6'),
        Index('idx_user_email', 'email'),
        Index('idx_user_service_account', 'realm_id', 'service_account_client_link')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    email_verified: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    enabled: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    not_before: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    email: Mapped[Optional[str]] = mapped_column(String(255))
    email_constraint: Mapped[Optional[str]] = mapped_column(String(255))
    federation_link: Mapped[Optional[str]] = mapped_column(String(255))
    first_name: Mapped[Optional[str]] = mapped_column(String(255))
    last_name: Mapped[Optional[str]] = mapped_column(String(255))
    realm_id: Mapped[Optional[str]] = mapped_column(String(255))
    username: Mapped[Optional[str]] = mapped_column(String(255))
    created_timestamp: Mapped[Optional[int]] = mapped_column(BigInteger)
    service_account_client_link: Mapped[Optional[str]] = mapped_column(String(255))

    ambassador: Mapped['Ambassador'] = relationship('Ambassador', uselist=False, back_populates='user')
    credential: Mapped[List['Credential']] = relationship('Credential', back_populates='user')
    federated_identity: Mapped[List['FederatedIdentity']] = relationship('FederatedIdentity', back_populates='user')
    user_attribute: Mapped[List['UserAttribute']] = relationship('UserAttribute', back_populates='user')
    user_brand: Mapped['UserBrand'] = relationship('UserBrand', uselist=False, back_populates='user')
    user_consent: Mapped[List['UserConsent']] = relationship('UserConsent', back_populates='user')
    user_customer: Mapped['UserCustomer'] = relationship('UserCustomer', uselist=False, back_populates='user')
    user_group_membership: Mapped[List['UserGroupMembership']] = relationship('UserGroupMembership', back_populates='user')
    user_influencer: Mapped['UserInfluencer'] = relationship('UserInfluencer', uselist=False, back_populates='user')
    user_permissions: Mapped['UserPermissions'] = relationship('UserPermissions', uselist=False, back_populates='user')
    user_required_action: Mapped[List['UserRequiredAction']] = relationship('UserRequiredAction', back_populates='user')
    user_role_mapping: Mapped[List['UserRoleMapping']] = relationship('UserRoleMapping', back_populates='user')


class UsernameLoginFailure(Base):
    __tablename__ = 'username_login_failure'
    __table_args__ = (
        PrimaryKeyConstraint('realm_id', 'username', name='CONSTRAINT_17-2'),
    )

    realm_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    username: Mapped[str] = mapped_column(String(255), primary_key=True)
    failed_login_not_before: Mapped[Optional[int]] = mapped_column(Integer)
    last_failure: Mapped[Optional[int]] = mapped_column(BigInteger)
    last_ip_failure: Mapped[Optional[str]] = mapped_column(String(255))
    num_failures: Mapped[Optional[int]] = mapped_column(Integer)


class Ambassador(Base):
    __tablename__ = 'ambassador'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['user_entity.id'], ondelete='CASCADE', name='ambassador_user_id_fkey'),
        PrimaryKeyConstraint('id', name='ambassador_pkey'),
        UniqueConstraint('user_id', name='ambassador_user_id_key')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[str] = mapped_column(String(36))
    user_status: Mapped[str] = mapped_column(Enum('PENDING', 'ACTIVE', 'SUSPENDED', 'BANNED', name='user_status_enum'))
    w9_submitted: Mapped[bool] = mapped_column(Boolean)
    account_tier: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    ambassador_code: Mapped[Optional[str]] = mapped_column(String(255))
    ambassador_wallet: Mapped[Optional[str]] = mapped_column(String(255))
    address_line_1: Mapped[Optional[str]] = mapped_column(String(255))
    address_line_2: Mapped[Optional[str]] = mapped_column(String(255))
    city: Mapped[Optional[str]] = mapped_column(String(255))
    state: Mapped[Optional[str]] = mapped_column(String(255))
    country: Mapped[Optional[str]] = mapped_column(String(255))
    zip_code: Mapped[Optional[str]] = mapped_column(String(255))
    w9_submission_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    user: Mapped['UserEntity'] = relationship('UserEntity', back_populates='ambassador')


class AuthenticationFlow(Base):
    __tablename__ = 'authentication_flow'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_auth_flow_realm'),
        PrimaryKeyConstraint('id', name='constraint_auth_flow_pk'),
        Index('idx_auth_flow_realm', 'realm_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    provider_id: Mapped[str] = mapped_column(String(36), server_default=text("'basic-flow'::character varying"))
    top_level: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    built_in: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    alias: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    realm_id: Mapped[Optional[str]] = mapped_column(String(36))

    realm: Mapped[Optional['Realm']] = relationship('Realm', back_populates='authentication_flow')
    authentication_execution: Mapped[List['AuthenticationExecution']] = relationship('AuthenticationExecution', back_populates='flow')


class AuthenticatorConfig(Base):
    __tablename__ = 'authenticator_config'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_auth_realm'),
        PrimaryKeyConstraint('id', name='constraint_auth_pk'),
        Index('idx_auth_config_realm', 'realm_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    alias: Mapped[Optional[str]] = mapped_column(String(255))
    realm_id: Mapped[Optional[str]] = mapped_column(String(36))

    realm: Mapped[Optional['Realm']] = relationship('Realm', back_populates='authenticator_config')


class CampaignActivityLog(Base):
    __tablename__ = 'campaign_activity_log'
    __table_args__ = (
        ForeignKeyConstraint(['campaign_id'], ['campaign.id'], name='campaign_activity_log_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_activity_log_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    activity_type: Mapped[str] = mapped_column(Enum('FAVORITE_ADDED', 'FAVORITE_REMOVED', 'CHAT_CREATED', 'COMMISSION_CREATED', 'COMMISSION_UPDATED', 'COMMISSION_DELETED', 'TEMPLATE_CREATED', 'TEMPLATE_UPDATED', 'TEMPLATE_DELETED', 'DELIVERABLE_CREATED', 'DELIVERABLE_UPDATED', 'DELIVERABLE_DELETED', 'DELIVERABLE_STATUS_UPDATED', 'CAMPAIGN_FAVORITE_ADDED', 'CAMPAIGN_FAVORITE_REMOVED', 'CAMPAIGN_INVITE_CREATED', 'CAMPAIGN_INVITE_UPDATED', 'CAMPAIGN_INVITE_DELETED', 'CAMPAIGN_INVITE_CANCELLED', 'CAMPAIGN_INVITE_ACCEPTED', 'CAMPAIGN_INVITE_DECLINED', 'CAMPAIGN_INVITE_COUNTER_PROPOSAL', 'CAMPAIGN_INVOICE_CREATED', 'CAMPAIGN_INVOICE_UPDATED', 'CAMPAIGN_INVOICE_DELETED', 'CAMPAIGN_MATCH_CREATED', 'CAMPAIGN_MATCH_UPDATED', 'CAMPAIGN_MATCH_DELETED', 'CAMPAIGN_MATERIAL_CREATED', 'CAMPAIGN_MATERIAL_UPDATED', 'CAMPAIGN_MATERIAL_DELETED', 'CAMPAIGN_METRICS_CREATED', 'CAMPAIGN_METRICS_UPDATED', 'CAMPAIGN_METRICS_DELETED', 'CAMPAIGN_NEGOTIATION_CREATED', 'CAMPAIGN_NEGOTIATION_ACCEPTED', 'BRAND_NEGOTIATION_CONFIRMED', 'INFLUENCER_NEGOTIATION_CONFIRMED', 'CAMPAIGN_PAYMENT_CREATED', 'CAMPAIGN_PAYMENT_UPDATED', 'CAMPAIGN_PAYMENT_PROCESSING', 'CAMPAIGN_REQUIREMENT_CREATED', 'CAMPAIGN_REQUIREMENT_UPDATED', 'CAMPAIGN_REQUIREMENT_DELETED', 'CAMPAIGN_REVIEW_CREATED', 'CAMPAIGN_REVIEW_UPDATED', 'CAMPAIGN_REVIEW_DELETED', 'CAMPAIGN_TARGETING_CREATED', 'CAMPAIGN_TARGETING_UPDATED', 'CAMPAIGN_TARGETING_DELETED', 'CAMPAIGN_CREATED', 'CAMPAIGN_UPDATED', 'CAMPAIGN_DELETED', 'CONTRACTED_CAMPAIGN_CREATED', 'FINALIZATION_REQUESTED', 'DISPUTE_REQUESTED', 'CAMPAIGN_FINALIZED', 'CONTRACTED_CAMPAIGN_UPDATED', name='activitytypeenum'))
    activity_data: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    brand_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    influencer_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    campaign_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    campaign: Mapped[Optional['Campaign']] = relationship('Campaign', back_populates='campaign_activity_log')


class CampaignChat(Base):
    __tablename__ = 'campaign_chat'
    __table_args__ = (
        ForeignKeyConstraint(['campaign_id'], ['campaign.id'], name='campaign_chat_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_chat_pkey'),
        Index('idx_campaign_chat_brand', 'brand_id'),
        Index('idx_campaign_chat_campaign_id', 'campaign_id'),
        Index('idx_campaign_chat_influencer', 'influencer_id'),
        Index('idx_campaign_chat_negotiation', 'negotiation_id'),
        Index('idx_campaign_chat_participants', 'brand_id', 'influencer_id', 'negotiation_id'),
        Index('idx_campaign_chat_status', 'status')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    chat_type: Mapped[str] = mapped_column(Enum('NEGOTIATION', 'DELIVERY', 'SUPPORT', name='chattypeenum'))
    status: Mapped[str] = mapped_column(Enum('ACTIVE', 'CLOSED', name='chatstatusenum'))
    brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    influencer_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    negotiation_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    closed_at: Mapped[Optional[int]] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    campaign: Mapped['Campaign'] = relationship('Campaign', back_populates='campaign_chat')
    chat_message: Mapped[List['ChatMessage']] = relationship('ChatMessage', back_populates='chat')


class CampaignDeliverableTemplate(Base):
    __tablename__ = 'campaign_deliverable_template'
    __table_args__ = (
        ForeignKeyConstraint(['campaign_id'], ['campaign.id'], name='campaign_deliverable_template_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_deliverable_template_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    content_type: Mapped[str] = mapped_column(Enum('PHOTO', 'VIDEO', 'STORY', 'REEL', 'LIVE', 'POST', name='contenttypeenum'))
    platform: Mapped[str] = mapped_column(Enum('INSTAGRAM', 'TIKTOK', 'YOUTUBE', 'FACEBOOK', 'OTHER', name='platformenum'))
    quantity: Mapped[int] = mapped_column(Integer)
    specifications: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    required_tags: Mapped[Optional[list]] = mapped_column(ARRAY(String()))
    guidelines: Mapped[Optional[str]] = mapped_column(String)
    submission_deadline_days: Mapped[Optional[int]] = mapped_column(Integer)
    review_deadline_days: Mapped[Optional[int]] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    campaign: Mapped['Campaign'] = relationship('Campaign', back_populates='campaign_deliverable_template')


class CampaignInvite(Base):
    __tablename__ = 'campaign_invite'
    __table_args__ = (
        ForeignKeyConstraint(['campaign_id'], ['campaign.id'], name='campaign_invite_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_invite_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    influencer_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    invite_type: Mapped[str] = mapped_column(Enum('BRAND_INVITE', 'INFLUENCER_APPLICATION', name='invitetypeenum'))
    status: Mapped[str] = mapped_column(Enum('PENDING', 'ACCEPTED', 'REJECTED', 'EXPIRED', 'CANCELLED', 'COUNTER_PROPOSAL', name='invitestatusenum'))
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    sender_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    proposed_value: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(12, 2))
    expires_at: Mapped[Optional[int]] = mapped_column(Integer)
    responded_at: Mapped[Optional[int]] = mapped_column(Integer)
    response_notes: Mapped[Optional[str]] = mapped_column(Text)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    campaign: Mapped['Campaign'] = relationship('Campaign', back_populates='campaign_invite')
    campaign_negotiation: Mapped[List['CampaignNegotiation']] = relationship('CampaignNegotiation', back_populates='campaign_invite')


class CampaignMatch(Base):
    __tablename__ = 'campaign_match'
    __table_args__ = (
        ForeignKeyConstraint(['campaign_id'], ['campaign.id'], name='campaign_match_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_match_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    influencer_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    match_score: Mapped[decimal.Decimal] = mapped_column(Numeric(5, 2))
    match_details: Mapped[dict] = mapped_column(JSON)
    status: Mapped[str] = mapped_column(Enum('PENDING', 'APPROVED', 'REJECTED', 'EXPIRED', name='matchstatusenum'))
    automated_match: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    requirements_match: Mapped[Optional[dict]] = mapped_column(JSON)
    audience_match: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(5, 2))
    category_match: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(5, 2))
    performance_score: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(5, 2))
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    campaign: Mapped['Campaign'] = relationship('Campaign', back_populates='campaign_match')


class CampaignMaterial(Base):
    __tablename__ = 'campaign_material'
    __table_args__ = (
        ForeignKeyConstraint(['campaign_id'], ['campaign.id'], name='campaign_material_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_material_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    material_type: Mapped[str] = mapped_column(Enum('PRODUCT_IMAGE', 'BRAND_GUIDELINES', 'TALKING_POINTS', 'VIDEO_ASSETS', 'PRESENTATION', 'LOGOS', name='materialtypeenum'))
    title: Mapped[str] = mapped_column(String(255))
    is_mandatory: Mapped[bool] = mapped_column(Boolean)
    version: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(Enum('ACTIVE', 'ARCHIVED', 'DELETED', name='materialstatusenum'))
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    description: Mapped[Optional[str]] = mapped_column(Text)
    file_url: Mapped[Optional[str]] = mapped_column(Text)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    campaign: Mapped['Campaign'] = relationship('Campaign', back_populates='campaign_material')


class CampaignRequirement(Base):
    __tablename__ = 'campaign_requirement'
    __table_args__ = (
        ForeignKeyConstraint(['campaign_id'], ['campaign.id'], name='campaign_requirement_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_requirement_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    requirement_type: Mapped[str] = mapped_column(Enum('FOLLOWERS_COUNT', 'ENGAGEMENT_RATE', 'AUDIENCE_DEMOGRAPHICS', 'CONTENT_CATEGORY', 'PLATFORM_PRESENCE', name='requirementtypeenum'))
    requirement_value: Mapped[dict] = mapped_column(JSON)
    is_mandatory: Mapped[bool] = mapped_column(Boolean)
    weight: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    campaign: Mapped['Campaign'] = relationship('Campaign', back_populates='campaign_requirement')


class CampaignTargeting(Base):
    __tablename__ = 'campaign_targeting'
    __table_args__ = (
        ForeignKeyConstraint(['campaign_id'], ['campaign.id'], name='campaign_targeting_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_targeting_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    targeting_type: Mapped[str] = mapped_column(Enum('DEMOGRAPHICS', 'INTERESTS', 'BEHAVIOR', 'LOCATION', 'PLATFORM', name='targetingtypeenum'))
    targeting_values: Mapped[dict] = mapped_column(JSON)
    priority: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    campaign: Mapped['Campaign'] = relationship('Campaign', back_populates='campaign_targeting')


class ClientAttributes(Base):
    __tablename__ = 'client_attributes'
    __table_args__ = (
        ForeignKeyConstraint(['client_id'], ['client.id'], name='fk3c47c64beacca966'),
        PrimaryKeyConstraint('client_id', 'name', name='constraint_3c'),
        Index('idx_client_att_by_name_value', 'name')
    )

    client_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[Optional[str]] = mapped_column(Text)

    client: Mapped['Client'] = relationship('Client', back_populates='client_attributes')


class ClientInitialAccess(Base):
    __tablename__ = 'client_initial_access'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_client_init_acc_realm'),
        PrimaryKeyConstraint('id', name='cnstr_client_init_acc_pk'),
        Index('idx_client_init_acc_realm', 'realm_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    realm_id: Mapped[str] = mapped_column(String(36))
    timestamp: Mapped[Optional[int]] = mapped_column(Integer)
    expiration: Mapped[Optional[int]] = mapped_column(Integer)
    count: Mapped[Optional[int]] = mapped_column(Integer)
    remaining_count: Mapped[Optional[int]] = mapped_column(Integer)

    realm: Mapped['Realm'] = relationship('Realm', back_populates='client_initial_access')


class ClientNodeRegistrations(Base):
    __tablename__ = 'client_node_registrations'
    __table_args__ = (
        ForeignKeyConstraint(['client_id'], ['client.id'], name='fk4129723ba992f594'),
        PrimaryKeyConstraint('client_id', 'name', name='constraint_84')
    )

    client_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[Optional[int]] = mapped_column(Integer)

    client: Mapped['Client'] = relationship('Client', back_populates='client_node_registrations')


class ClientScopeAttributes(Base):
    __tablename__ = 'client_scope_attributes'
    __table_args__ = (
        ForeignKeyConstraint(['scope_id'], ['client_scope.id'], name='fk_cl_scope_attr_scope'),
        PrimaryKeyConstraint('scope_id', 'name', name='pk_cl_tmpl_attr'),
        Index('idx_clscope_attrs', 'scope_id')
    )

    scope_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[Optional[str]] = mapped_column(String(2048))

    scope: Mapped['ClientScope'] = relationship('ClientScope', back_populates='client_scope_attributes')


class ClientScopeRoleMapping(Base):
    __tablename__ = 'client_scope_role_mapping'
    __table_args__ = (
        ForeignKeyConstraint(['scope_id'], ['client_scope.id'], name='fk_cl_scope_rm_scope'),
        PrimaryKeyConstraint('scope_id', 'role_id', name='pk_template_scope'),
        Index('idx_clscope_role', 'scope_id'),
        Index('idx_role_clscope', 'role_id')
    )

    scope_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    role_id: Mapped[str] = mapped_column(String(36), primary_key=True)

    scope: Mapped['ClientScope'] = relationship('ClientScope', back_populates='client_scope_role_mapping')


class Component(Base):
    __tablename__ = 'component'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_component_realm'),
        PrimaryKeyConstraint('id', name='constr_component_pk'),
        Index('idx_component_provider_type', 'provider_type'),
        Index('idx_component_realm', 'realm_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    parent_id: Mapped[Optional[str]] = mapped_column(String(36))
    provider_id: Mapped[Optional[str]] = mapped_column(String(36))
    provider_type: Mapped[Optional[str]] = mapped_column(String(255))
    realm_id: Mapped[Optional[str]] = mapped_column(String(36))
    sub_type: Mapped[Optional[str]] = mapped_column(String(255))

    realm: Mapped[Optional['Realm']] = relationship('Realm', back_populates='component')
    component_config: Mapped[List['ComponentConfig']] = relationship('ComponentConfig', back_populates='component')


class ContractedCampaign(Base):
    __tablename__ = 'contracted_campaign'
    __table_args__ = (
        ForeignKeyConstraint(['campaign_id'], ['campaign.id'], name='contracted_campaign_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='contracted_campaign_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    influencer_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    status: Mapped[str] = mapped_column(Enum('PENDING', 'IN_PROGRESS', 'CANCELLED', 'FINALIZATION_REQUESTED', 'DISPUTE_REQUESTED', 'COMPLETED', name='contractstatusenum'))
    campaign_finalized: Mapped[bool] = mapped_column(Boolean)
    campaign_in_dispute: Mapped[bool] = mapped_column(Boolean)
    due_date: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    brand_ambassador_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    influencer_ambassador_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    payment_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    contract_terms: Mapped[Optional[str]] = mapped_column(Text)
    review_status: Mapped[Optional[str]] = mapped_column(Text)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    campaign: Mapped['Campaign'] = relationship('Campaign', back_populates='contracted_campaign')
    campaign_commission: Mapped[List['CampaignCommission']] = relationship('CampaignCommission', back_populates='contracted_campaign')
    campaign_deliverable: Mapped[List['CampaignDeliverable']] = relationship('CampaignDeliverable', back_populates='contracted_campaign')
    campaign_invoice: Mapped[List['CampaignInvoice']] = relationship('CampaignInvoice', back_populates='contracted_campaign')
    campaign_payment: Mapped[List['CampaignPayment']] = relationship('CampaignPayment', back_populates='contracted_campaign')
    campaign_review: Mapped[List['CampaignReview']] = relationship('CampaignReview', back_populates='contracted_campaign')


class Credential(Base):
    __tablename__ = 'credential'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['user_entity.id'], name='fk_pfyr0glasqyl0dei3kl69r6v0'),
        PrimaryKeyConstraint('id', name='constraint_f'),
        Index('idx_user_credential', 'user_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    salt: Mapped[Optional[bytes]] = mapped_column(LargeBinary)
    type: Mapped[Optional[str]] = mapped_column(String(255))
    user_id: Mapped[Optional[str]] = mapped_column(String(36))
    created_date: Mapped[Optional[int]] = mapped_column(BigInteger)
    user_label: Mapped[Optional[str]] = mapped_column(String(255))
    secret_data: Mapped[Optional[str]] = mapped_column(Text)
    credential_data: Mapped[Optional[str]] = mapped_column(Text)
    priority: Mapped[Optional[int]] = mapped_column(Integer)

    user: Mapped[Optional['UserEntity']] = relationship('UserEntity', back_populates='credential')


class DefaultClientScope(Base):
    __tablename__ = 'default_client_scope'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_r_def_cli_scope_realm'),
        PrimaryKeyConstraint('realm_id', 'scope_id', name='r_def_cli_scope_bind'),
        Index('idx_defcls_realm', 'realm_id'),
        Index('idx_defcls_scope', 'scope_id')
    )

    realm_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    scope_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    default_scope: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))

    realm: Mapped['Realm'] = relationship('Realm', back_populates='default_client_scope')


class FavoriteProducts(Base):
    __tablename__ = 'favorite_products'
    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['products.product_id'], name='favorite_products_product_id_fkey'),
        PrimaryKeyConstraint('favorite_product_id', name='favorite_products_pkey')
    )

    favorite_product_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    product_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    product: Mapped['Products'] = relationship('Products', back_populates='favorite_products')


class FederatedIdentity(Base):
    __tablename__ = 'federated_identity'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['user_entity.id'], name='fk404288b92ef007a6'),
        PrimaryKeyConstraint('identity_provider', 'user_id', name='constraint_40'),
        Index('idx_fedidentity_feduser', 'federated_user_id'),
        Index('idx_fedidentity_user', 'user_id')
    )

    identity_provider: Mapped[str] = mapped_column(String(255), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    realm_id: Mapped[Optional[str]] = mapped_column(String(36))
    federated_user_id: Mapped[Optional[str]] = mapped_column(String(255))
    federated_username: Mapped[Optional[str]] = mapped_column(String(255))
    token: Mapped[Optional[str]] = mapped_column(Text)

    user: Mapped['UserEntity'] = relationship('UserEntity', back_populates='federated_identity')


class GroupAttribute(Base):
    __tablename__ = 'group_attribute'
    __table_args__ = (
        ForeignKeyConstraint(['group_id'], ['keycloak_group.id'], name='fk_group_attribute_group'),
        PrimaryKeyConstraint('id', name='constraint_group_attribute_pk'),
        Index('idx_group_att_by_name_value', 'name'),
        Index('idx_group_attr_group', 'group_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True, server_default=text("'sybase-needs-something-here'::character varying"))
    name: Mapped[str] = mapped_column(String(255))
    group_id: Mapped[str] = mapped_column(String(36))
    value: Mapped[Optional[str]] = mapped_column(String(255))

    group: Mapped['KeycloakGroup'] = relationship('KeycloakGroup', back_populates='group_attribute')


class GroupRoleMapping(Base):
    __tablename__ = 'group_role_mapping'
    __table_args__ = (
        ForeignKeyConstraint(['group_id'], ['keycloak_group.id'], name='fk_group_role_group'),
        PrimaryKeyConstraint('role_id', 'group_id', name='constraint_group_role'),
        Index('idx_group_role_mapp_group', 'group_id')
    )

    role_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    group_id: Mapped[str] = mapped_column(String(36), primary_key=True)

    group: Mapped['KeycloakGroup'] = relationship('KeycloakGroup', back_populates='group_role_mapping')


class IdentityProvider(Base):
    __tablename__ = 'identity_provider'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk2b4ebc52ae5c3b34'),
        PrimaryKeyConstraint('internal_id', name='constraint_2b'),
        UniqueConstraint('provider_alias', 'realm_id', name='uk_2daelwnibji49avxsrtuf6xj33'),
        Index('idx_ident_prov_realm', 'realm_id'),
        Index('idx_idp_for_login', 'realm_id', 'enabled', 'link_only', 'hide_on_login', 'organization_id'),
        Index('idx_idp_realm_org', 'realm_id', 'organization_id')
    )

    internal_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    enabled: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    store_token: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    authenticate_by_default: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    add_token_role: Mapped[bool] = mapped_column(Boolean, server_default=text('true'))
    trust_email: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    link_only: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    provider_alias: Mapped[Optional[str]] = mapped_column(String(255))
    provider_id: Mapped[Optional[str]] = mapped_column(String(255))
    realm_id: Mapped[Optional[str]] = mapped_column(String(36))
    first_broker_login_flow_id: Mapped[Optional[str]] = mapped_column(String(36))
    post_broker_login_flow_id: Mapped[Optional[str]] = mapped_column(String(36))
    provider_display_name: Mapped[Optional[str]] = mapped_column(String(255))
    organization_id: Mapped[Optional[str]] = mapped_column(String(255))
    hide_on_login: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('false'))

    realm: Mapped[Optional['Realm']] = relationship('Realm', back_populates='identity_provider')
    identity_provider_config: Mapped[List['IdentityProviderConfig']] = relationship('IdentityProviderConfig', back_populates='identity_provider')


class IdentityProviderMapper(Base):
    __tablename__ = 'identity_provider_mapper'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_idpm_realm'),
        PrimaryKeyConstraint('id', name='constraint_idpm'),
        Index('idx_id_prov_mapp_realm', 'realm_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    idp_alias: Mapped[str] = mapped_column(String(255))
    idp_mapper_name: Mapped[str] = mapped_column(String(255))
    realm_id: Mapped[str] = mapped_column(String(36))

    realm: Mapped['Realm'] = relationship('Realm', back_populates='identity_provider_mapper')
    idp_mapper_config: Mapped[List['IdpMapperConfig']] = relationship('IdpMapperConfig', back_populates='idp_mapper')


class KeycloakRole(Base):
    __tablename__ = 'keycloak_role'
    __table_args__ = (
        ForeignKeyConstraint(['realm'], ['realm.id'], name='fk_6vyqfe4cn4wlq8r6kt5vdsj5c'),
        PrimaryKeyConstraint('id', name='constraint_a'),
        UniqueConstraint('name', 'client_realm_constraint', name='UK_J3RWUVD56ONTGSUHOGM184WW2-2'),
        Index('idx_keycloak_role_client', 'client'),
        Index('idx_keycloak_role_realm', 'realm')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    client_role: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    client_realm_constraint: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    name: Mapped[Optional[str]] = mapped_column(String(255))
    realm_id: Mapped[Optional[str]] = mapped_column(String(255))
    client: Mapped[Optional[str]] = mapped_column(String(36))
    realm: Mapped[Optional[str]] = mapped_column(String(36))

    realm_: Mapped[Optional['Realm']] = relationship('Realm', back_populates='keycloak_role')
    keycloak_role: Mapped[List['KeycloakRole']] = relationship('KeycloakRole', secondary='composite_role', primaryjoin=lambda: KeycloakRole.id == t_composite_role.c.child_role, secondaryjoin=lambda: KeycloakRole.id == t_composite_role.c.composite, back_populates='keycloak_role_')
    keycloak_role_: Mapped[List['KeycloakRole']] = relationship('KeycloakRole', secondary='composite_role', primaryjoin=lambda: KeycloakRole.id == t_composite_role.c.composite, secondaryjoin=lambda: KeycloakRole.id == t_composite_role.c.child_role, back_populates='keycloak_role')
    role_attribute: Mapped[List['RoleAttribute']] = relationship('RoleAttribute', back_populates='role')


class Media(Base):
    __tablename__ = 'media'
    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['products.product_id'], name='media_product_id_fkey'),
        PrimaryKeyConstraint('media_id', name='media_pkey')
    )

    media_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    product_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    is_main: Mapped[bool] = mapped_column(Boolean)
    media: Mapped[str] = mapped_column(String)
    file_path: Mapped[str] = mapped_column(String)
    orientation_type: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    product: Mapped['Products'] = relationship('Products', back_populates='media')


class OfferInfluencer(Base):
    __tablename__ = 'offer_influencer'
    __table_args__ = (
        ForeignKeyConstraint(['offer_id'], ['offer.id'], name='offer_influencer_offer_id_fkey'),
        PrimaryKeyConstraint('id', 'offer_id', 'influencer_id', name='offer_influencer_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    offer_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    influencer_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    is_active: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    offer: Mapped['Offer'] = relationship('Offer', back_populates='offer_influencer')


class OrderBrands(Base):
    __tablename__ = 'order_brands'
    __table_args__ = (
        ForeignKeyConstraint(['order_id'], ['orders.order_id'], name='order_brands_order_id_fkey'),
        PrimaryKeyConstraint('order_brand_id', name='order_brands_pkey')
    )

    order_brand_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    order_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    address_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    status: Mapped[str] = mapped_column(String)
    order_number: Mapped[str] = mapped_column(String)
    order_brand_number: Mapped[str] = mapped_column(String)
    customer_name: Mapped[str] = mapped_column(String)
    customer_email: Mapped[str] = mapped_column(String)
    delivery_address: Mapped[str] = mapped_column(String)
    delivery_city: Mapped[str] = mapped_column(String)
    delivery_state: Mapped[str] = mapped_column(String)
    delivery_postal_code: Mapped[str] = mapped_column(String)
    payment_method: Mapped[str] = mapped_column(String)
    sub_total: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    shipping_cost: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    discount_amount: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    total_amount: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    customer_phone: Mapped[Optional[str]] = mapped_column(String)
    delivery_status: Mapped[Optional[str]] = mapped_column(String)
    payment_status: Mapped[Optional[str]] = mapped_column(String)
    card_last_digits: Mapped[Optional[str]] = mapped_column(String)
    installments: Mapped[Optional[int]] = mapped_column(Integer)
    estimated_delivery_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    delivered_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    notes: Mapped[Optional[str]] = mapped_column(String)
    tracking_code: Mapped[Optional[str]] = mapped_column(String)
    invoice: Mapped[Optional[str]] = mapped_column(String)
    invoice_link: Mapped[Optional[str]] = mapped_column(String)
    label_url: Mapped[Optional[str]] = mapped_column(String)
    label_id: Mapped[Optional[str]] = mapped_column(String)
    company_freight: Mapped[Optional[str]] = mapped_column(String)
    estimated_delivery: Mapped[Optional[dict]] = mapped_column(JSON)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    order: Mapped['Orders'] = relationship('Orders', back_populates='order_brands')


class OrderItems(Base):
    __tablename__ = 'order_items'
    __table_args__ = (
        ForeignKeyConstraint(['order_id'], ['orders.order_id'], name='order_items_order_id_fkey'),
        PrimaryKeyConstraint('order_item_id', name='order_items_pkey')
    )

    order_item_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    order_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    order_brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    influencer_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    ambassador_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    product_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    offer_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    status: Mapped[str] = mapped_column(String)
    order_number: Mapped[str] = mapped_column(String)
    order_brand_number: Mapped[str] = mapped_column(String)
    product_name: Mapped[str] = mapped_column(String)
    quantity: Mapped[int] = mapped_column(Integer)
    unit_price: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    item_discount: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    total_price: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    brand_name: Mapped[str] = mapped_column(String)
    sku: Mapped[str] = mapped_column(String)
    model: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    color: Mapped[Optional[str]] = mapped_column(String)
    size: Mapped[Optional[str]] = mapped_column(String)
    image: Mapped[Optional[str]] = mapped_column(String)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    order: Mapped['Orders'] = relationship('Orders', back_populates='order_items')


class ProtocolMapper(Base):
    __tablename__ = 'protocol_mapper'
    __table_args__ = (
        ForeignKeyConstraint(['client_id'], ['client.id'], name='fk_pcm_realm'),
        ForeignKeyConstraint(['client_scope_id'], ['client_scope.id'], name='fk_cli_scope_mapper'),
        PrimaryKeyConstraint('id', name='constraint_pcm'),
        Index('idx_clscope_protmap', 'client_scope_id'),
        Index('idx_protocol_mapper_client', 'client_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    protocol: Mapped[str] = mapped_column(String(255))
    protocol_mapper_name: Mapped[str] = mapped_column(String(255))
    client_id: Mapped[Optional[str]] = mapped_column(String(36))
    client_scope_id: Mapped[Optional[str]] = mapped_column(String(36))

    client: Mapped[Optional['Client']] = relationship('Client', back_populates='protocol_mapper')
    client_scope: Mapped[Optional['ClientScope']] = relationship('ClientScope', back_populates='protocol_mapper')
    protocol_mapper_config: Mapped[List['ProtocolMapperConfig']] = relationship('ProtocolMapperConfig', back_populates='protocol_mapper')


class RealmAttribute(Base):
    __tablename__ = 'realm_attribute'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_8shxd6l3e9atqukacxgpffptw'),
        PrimaryKeyConstraint('name', 'realm_id', name='constraint_9'),
        Index('idx_realm_attr_realm', 'realm_id')
    )

    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    realm_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    value: Mapped[Optional[str]] = mapped_column(Text)

    realm: Mapped['Realm'] = relationship('Realm', back_populates='realm_attribute')


class RealmDefaultGroups(Base):
    __tablename__ = 'realm_default_groups'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_def_groups_realm'),
        PrimaryKeyConstraint('realm_id', 'group_id', name='constr_realm_default_groups'),
        UniqueConstraint('group_id', name='con_group_id_def_groups'),
        Index('idx_realm_def_grp_realm', 'realm_id')
    )

    realm_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    group_id: Mapped[str] = mapped_column(String(36), primary_key=True)

    realm: Mapped['Realm'] = relationship('Realm', back_populates='realm_default_groups')


class RealmEnabledEventTypes(Base):
    __tablename__ = 'realm_enabled_event_types'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_h846o4h0w8epx5nwedrf5y69j'),
        PrimaryKeyConstraint('realm_id', 'value', name='constr_realm_enabl_event_types'),
        Index('idx_realm_evt_types_realm', 'realm_id')
    )

    realm_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    value: Mapped[str] = mapped_column(String(255), primary_key=True)

    realm: Mapped['Realm'] = relationship('Realm', back_populates='realm_enabled_event_types')


class RealmEventsListeners(Base):
    __tablename__ = 'realm_events_listeners'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_h846o4h0w8epx5nxev9f5y69j'),
        PrimaryKeyConstraint('realm_id', 'value', name='constr_realm_events_listeners'),
        Index('idx_realm_evt_list_realm', 'realm_id')
    )

    realm_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    value: Mapped[str] = mapped_column(String(255), primary_key=True)

    realm: Mapped['Realm'] = relationship('Realm', back_populates='realm_events_listeners')


class RealmRequiredCredential(Base):
    __tablename__ = 'realm_required_credential'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_5hg65lybevavkqfki3kponh9v'),
        PrimaryKeyConstraint('realm_id', 'type', name='constraint_92')
    )

    type: Mapped[str] = mapped_column(String(255), primary_key=True)
    input: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    secret: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    realm_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    form_label: Mapped[Optional[str]] = mapped_column(String(255))

    realm: Mapped['Realm'] = relationship('Realm', back_populates='realm_required_credential')


class RealmSmtpConfig(Base):
    __tablename__ = 'realm_smtp_config'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_70ej8xdxgxd0b9hh6180irr0o'),
        PrimaryKeyConstraint('realm_id', 'name', name='constraint_e')
    )

    realm_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[Optional[str]] = mapped_column(String(255))

    realm: Mapped['Realm'] = relationship('Realm', back_populates='realm_smtp_config')


class RealmSupportedLocales(Base):
    __tablename__ = 'realm_supported_locales'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_supported_locales_realm'),
        PrimaryKeyConstraint('realm_id', 'value', name='constr_realm_supported_locales'),
        Index('idx_realm_supp_local_realm', 'realm_id')
    )

    realm_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    value: Mapped[str] = mapped_column(String(255), primary_key=True)

    realm: Mapped['Realm'] = relationship('Realm', back_populates='realm_supported_locales')


class RedirectUris(Base):
    __tablename__ = 'redirect_uris'
    __table_args__ = (
        ForeignKeyConstraint(['client_id'], ['client.id'], name='fk_1burs8pb4ouj97h5wuppahv9f'),
        PrimaryKeyConstraint('client_id', 'value', name='constraint_redirect_uris'),
        Index('idx_redir_uri_client', 'client_id')
    )

    client_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    value: Mapped[str] = mapped_column(String(255), primary_key=True)

    client: Mapped['Client'] = relationship('Client', back_populates='redirect_uris')


class RequiredActionProvider(Base):
    __tablename__ = 'required_action_provider'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_req_act_realm'),
        PrimaryKeyConstraint('id', name='constraint_req_act_prv_pk'),
        Index('idx_req_act_prov_realm', 'realm_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    enabled: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    default_action: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    alias: Mapped[Optional[str]] = mapped_column(String(255))
    name: Mapped[Optional[str]] = mapped_column(String(255))
    realm_id: Mapped[Optional[str]] = mapped_column(String(36))
    provider_id: Mapped[Optional[str]] = mapped_column(String(255))
    priority: Mapped[Optional[int]] = mapped_column(Integer)

    realm: Mapped[Optional['Realm']] = relationship('Realm', back_populates='required_action_provider')


class ResourceServerPolicy(Base):
    __tablename__ = 'resource_server_policy'
    __table_args__ = (
        ForeignKeyConstraint(['resource_server_id'], ['resource_server.id'], name='fk_frsrpo213xcx4wnkog82ssrfy'),
        PrimaryKeyConstraint('id', name='constraint_farsrp'),
        UniqueConstraint('name', 'resource_server_id', name='uk_frsrpt700s9v50bu18ws5ha6'),
        Index('idx_res_serv_pol_res_serv', 'resource_server_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    type: Mapped[str] = mapped_column(String(255))
    resource_server_id: Mapped[str] = mapped_column(String(36))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    decision_strategy: Mapped[Optional[int]] = mapped_column(SmallInteger)
    logic: Mapped[Optional[int]] = mapped_column(SmallInteger)
    owner: Mapped[Optional[str]] = mapped_column(String(255))

    resource_server: Mapped['ResourceServer'] = relationship('ResourceServer', back_populates='resource_server_policy')
    policy: Mapped[List['ResourceServerPolicy']] = relationship('ResourceServerPolicy', secondary='associated_policy', primaryjoin=lambda: ResourceServerPolicy.id == t_associated_policy.c.associated_policy_id, secondaryjoin=lambda: ResourceServerPolicy.id == t_associated_policy.c.policy_id, back_populates='associated_policy')
    associated_policy: Mapped[List['ResourceServerPolicy']] = relationship('ResourceServerPolicy', secondary='associated_policy', primaryjoin=lambda: ResourceServerPolicy.id == t_associated_policy.c.policy_id, secondaryjoin=lambda: ResourceServerPolicy.id == t_associated_policy.c.associated_policy_id, back_populates='policy')
    resource: Mapped[List['ResourceServerResource']] = relationship('ResourceServerResource', secondary='resource_policy', back_populates='policy')
    scope: Mapped[List['ResourceServerScope']] = relationship('ResourceServerScope', secondary='scope_policy', back_populates='policy')
    policy_config: Mapped[List['PolicyConfig']] = relationship('PolicyConfig', back_populates='policy')
    resource_server_perm_ticket: Mapped[List['ResourceServerPermTicket']] = relationship('ResourceServerPermTicket', back_populates='policy')


class ResourceServerResource(Base):
    __tablename__ = 'resource_server_resource'
    __table_args__ = (
        ForeignKeyConstraint(['resource_server_id'], ['resource_server.id'], name='fk_frsrho213xcx4wnkog82ssrfy'),
        PrimaryKeyConstraint('id', name='constraint_farsr'),
        UniqueConstraint('name', 'owner', 'resource_server_id', name='uk_frsr6t700s9v50bu18ws5ha6'),
        Index('idx_res_srv_res_res_srv', 'resource_server_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    owner: Mapped[str] = mapped_column(String(255))
    resource_server_id: Mapped[str] = mapped_column(String(36))
    owner_managed_access: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    type: Mapped[Optional[str]] = mapped_column(String(255))
    icon_uri: Mapped[Optional[str]] = mapped_column(String(255))
    display_name: Mapped[Optional[str]] = mapped_column(String(255))

    policy: Mapped[List['ResourceServerPolicy']] = relationship('ResourceServerPolicy', secondary='resource_policy', back_populates='resource')
    resource_server: Mapped['ResourceServer'] = relationship('ResourceServer', back_populates='resource_server_resource')
    scope: Mapped[List['ResourceServerScope']] = relationship('ResourceServerScope', secondary='resource_scope', back_populates='resource')
    resource_attribute: Mapped[List['ResourceAttribute']] = relationship('ResourceAttribute', back_populates='resource')
    resource_server_perm_ticket: Mapped[List['ResourceServerPermTicket']] = relationship('ResourceServerPermTicket', back_populates='resource')
    resource_uris: Mapped[List['ResourceUris']] = relationship('ResourceUris', back_populates='resource')


class ResourceServerScope(Base):
    __tablename__ = 'resource_server_scope'
    __table_args__ = (
        ForeignKeyConstraint(['resource_server_id'], ['resource_server.id'], name='fk_frsrso213xcx4wnkog82ssrfy'),
        PrimaryKeyConstraint('id', name='constraint_farsrs'),
        UniqueConstraint('name', 'resource_server_id', name='uk_frsrst700s9v50bu18ws5ha6'),
        Index('idx_res_srv_scope_res_srv', 'resource_server_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    resource_server_id: Mapped[str] = mapped_column(String(36))
    icon_uri: Mapped[Optional[str]] = mapped_column(String(255))
    display_name: Mapped[Optional[str]] = mapped_column(String(255))

    policy: Mapped[List['ResourceServerPolicy']] = relationship('ResourceServerPolicy', secondary='scope_policy', back_populates='scope')
    resource: Mapped[List['ResourceServerResource']] = relationship('ResourceServerResource', secondary='resource_scope', back_populates='scope')
    resource_server: Mapped['ResourceServer'] = relationship('ResourceServer', back_populates='resource_server_scope')
    resource_server_perm_ticket: Mapped[List['ResourceServerPermTicket']] = relationship('ResourceServerPermTicket', back_populates='scope')


class ScopeMapping(Base):
    __tablename__ = 'scope_mapping'
    __table_args__ = (
        ForeignKeyConstraint(['client_id'], ['client.id'], name='fk_ouse064plmlr732lxjcn1q5f1'),
        PrimaryKeyConstraint('client_id', 'role_id', name='constraint_81'),
        Index('idx_scope_mapping_role', 'role_id')
    )

    client_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    role_id: Mapped[str] = mapped_column(String(36), primary_key=True)

    client: Mapped['Client'] = relationship('Client', back_populates='scope_mapping')


class SubscriptionStatusLog(Base):
    __tablename__ = 'subscription_status_log'
    __table_args__ = (
        ForeignKeyConstraint(['subscription_id'], ['subscription_influencer.id'], name='subscription_status_log_subscription_id_fkey'),
        PrimaryKeyConstraint('id', name='subscription_status_log_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    subscription_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    new_status: Mapped[str] = mapped_column(String(50))
    reason: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    old_status: Mapped[Optional[str]] = mapped_column(String(50))
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    subscription: Mapped['SubscriptionInfluencer'] = relationship('SubscriptionInfluencer', back_populates='subscription_status_log')


class SubscriptionVerification(Base):
    __tablename__ = 'subscription_verification'
    __table_args__ = (
        ForeignKeyConstraint(['subscription_id'], ['subscription_influencer.id'], name='subscription_verification_subscription_id_fkey'),
        PrimaryKeyConstraint('id', name='subscription_verification_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    subscription_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    influencer_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    verification_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    goals_achieved: Mapped[dict] = mapped_column(JSONB)
    next_verification_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    sales_value: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)
    campaigns_count: Mapped[Optional[int]] = mapped_column(Integer)
    content_count: Mapped[Optional[int]] = mapped_column(Integer)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    subscription: Mapped['SubscriptionInfluencer'] = relationship('SubscriptionInfluencer', back_populates='subscription_verification')


class TokenConsumptionHistory(Base):
    __tablename__ = 'token_consumption_history'
    __table_args__ = (
        ForeignKeyConstraint(['user_token_cycle_id'], ['token_user_cycle.id'], name='token_consumption_history_user_token_cycle_id_fkey'),
        PrimaryKeyConstraint('id', name='token_consumption_history_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    user_type: Mapped[str] = mapped_column(Enum('BRAND', 'INFLUENCER', 'CONSUMER', name='tokenusertype'))
    user_token_cycle_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    tokens_used: Mapped[int] = mapped_column(Integer)
    feature_used: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    user_token_cycle: Mapped['TokenUserCycle'] = relationship('TokenUserCycle', back_populates='token_consumption_history')


class TokenPurchase(Base):
    __tablename__ = 'token_purchase'
    __table_args__ = (
        ForeignKeyConstraint(['token_plan_id'], ['token_plan.id'], name='token_purchase_token_plan_id_fkey'),
        PrimaryKeyConstraint('id', name='token_purchase_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    user_type: Mapped[str] = mapped_column(Enum('BRAND', 'INFLUENCER', 'CONSUMER', name='tokenusertype'))
    token_plan_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    amount_paid: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    tokens_acquired: Mapped[int] = mapped_column(Integer)
    payment_status: Mapped[str] = mapped_column(Enum('PENDING', 'COMPLETED', 'FAILED', name='paymentstatus'))
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    token_plan: Mapped['TokenPlan'] = relationship('TokenPlan', back_populates='token_purchase')


class TrackingInteractions(Base):
    __tablename__ = 'tracking_interactions'
    __table_args__ = (
        ForeignKeyConstraint(['event_id'], ['tracking_events.id'], name='tracking_interactions_event_id_fkey'),
        PrimaryKeyConstraint('id', 'event_id', name='tracking_interactions_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    event_id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    occurred_at: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    visitor_id: Mapped[Optional[str]] = mapped_column(String)
    interaction_type: Mapped[Optional[str]] = mapped_column(String)
    utm_data: Mapped[Optional[dict]] = mapped_column(JSONB)
    device_info: Mapped[Optional[dict]] = mapped_column(JSONB)
    referrer_url: Mapped[Optional[str]] = mapped_column(String)
    ip_address: Mapped[Optional[str]] = mapped_column(String)
    conversion_value: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(15, 2))
    metadata_at: Mapped[Optional[str]] = mapped_column(String)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    event: Mapped['TrackingEvents'] = relationship('TrackingEvents', back_populates='tracking_interactions')


class UserAttribute(Base):
    __tablename__ = 'user_attribute'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['user_entity.id'], name='fk_5hrm2vlf9ql5fu043kqepovbr'),
        PrimaryKeyConstraint('id', name='constraint_user_attribute_pk'),
        Index('idx_user_attribute', 'user_id'),
        Index('idx_user_attribute_name', 'name', 'value'),
        Index('user_attr_long_values', 'long_value_hash', 'name'),
        Index('user_attr_long_values_lower_case', 'long_value_hash_lower_case', 'name')
    )

    name: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[str] = mapped_column(String(36))
    id: Mapped[str] = mapped_column(String(36), primary_key=True, server_default=text("'sybase-needs-something-here'::character varying"))
    value: Mapped[Optional[str]] = mapped_column(String(255))
    long_value_hash: Mapped[Optional[bytes]] = mapped_column(LargeBinary)
    long_value_hash_lower_case: Mapped[Optional[bytes]] = mapped_column(LargeBinary)
    long_value: Mapped[Optional[str]] = mapped_column(Text)

    user: Mapped['UserEntity'] = relationship('UserEntity', back_populates='user_attribute')


class UserBrand(Base):
    __tablename__ = 'user_brand'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['user_entity.id'], ondelete='CASCADE', name='user_brand_user_id_fkey'),
        PrimaryKeyConstraint('id', name='user_brand_pkey'),
        UniqueConstraint('user_id', name='user_brand_user_id_key')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[str] = mapped_column(String(36))
    business_name: Mapped[str] = mapped_column(String)
    ein_verified: Mapped[bool] = mapped_column(Boolean)
    kyb_verified: Mapped[bool] = mapped_column(Boolean)
    aml_verified: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    dba_name: Mapped[Optional[str]] = mapped_column(String)
    business_type: Mapped[Optional[str]] = mapped_column(String)
    ein: Mapped[Optional[str]] = mapped_column(String(10))
    tax_classification: Mapped[Optional[str]] = mapped_column(String(50))
    support_email: Mapped[Optional[str]] = mapped_column(String)
    company_description: Mapped[Optional[str]] = mapped_column(Text)
    mission_statement: Mapped[Optional[str]] = mapped_column(Text)
    logo_url: Mapped[Optional[str]] = mapped_column(String)
    banner_url: Mapped[Optional[str]] = mapped_column(String)
    website_url: Mapped[Optional[str]] = mapped_column(String)
    business_license: Mapped[Optional[str]] = mapped_column(String(50))
    state_registration: Mapped[Optional[str]] = mapped_column(String(50))
    compliance_notes: Mapped[Optional[dict]] = mapped_column(JSONB)
    last_compliance_check: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    state_restrictions: Mapped[Optional[str]] = mapped_column(String(2))
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    user: Mapped['UserEntity'] = relationship('UserEntity', back_populates='user_brand')


class UserConsent(Base):
    __tablename__ = 'user_consent'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['user_entity.id'], name='fk_grntcsnt_user'),
        PrimaryKeyConstraint('id', name='constraint_grntcsnt_pm'),
        UniqueConstraint('client_id', 'user_id', name='uk_local_consent'),
        UniqueConstraint('client_storage_provider', 'external_client_id', 'user_id', name='uk_external_consent'),
        Index('idx_user_consent', 'user_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(36))
    client_id: Mapped[Optional[str]] = mapped_column(String(255))
    created_date: Mapped[Optional[int]] = mapped_column(BigInteger)
    last_updated_date: Mapped[Optional[int]] = mapped_column(BigInteger)
    client_storage_provider: Mapped[Optional[str]] = mapped_column(String(36))
    external_client_id: Mapped[Optional[str]] = mapped_column(String(255))

    user: Mapped['UserEntity'] = relationship('UserEntity', back_populates='user_consent')
    user_consent_client_scope: Mapped[List['UserConsentClientScope']] = relationship('UserConsentClientScope', back_populates='user_consent')


class UserCustomer(Base):
    __tablename__ = 'user_customer'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['user_entity.id'], ondelete='CASCADE', name='user_customer_user_id_fkey'),
        PrimaryKeyConstraint('id', name='user_customer_pkey'),
        UniqueConstraint('referral_code', name='user_customer_referral_code_key'),
        UniqueConstraint('user_id', name='user_customer_user_id_key')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[str] = mapped_column(String(36))
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    currency_preference: Mapped[str] = mapped_column(String)
    loyalty_tier: Mapped[str] = mapped_column(String)
    loyalty_points: Mapped[int] = mapped_column(Integer)
    marketing_email_opt_in: Mapped[bool] = mapped_column(Boolean)
    sms_opt_in: Mapped[bool] = mapped_column(Boolean)
    push_notification_opt_in: Mapped[bool] = mapped_column(Boolean)
    two_factor_enabled: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    date_of_birth: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    gender: Mapped[Optional[str]] = mapped_column(Enum('MALE', 'FEMALE', 'NON_BINARY', name='gender_enum'))
    profile_image: Mapped[Optional[str]] = mapped_column(String)
    alternate_email: Mapped[Optional[str]] = mapped_column(String)
    preferred_contact_method: Mapped[Optional[str]] = mapped_column(String)
    billing_address_id: Mapped[Optional[str]] = mapped_column(String(36))
    default_payment_method: Mapped[Optional[str]] = mapped_column(String)
    payment_methods: Mapped[Optional[list]] = mapped_column(ARRAY(JSONB(astext_type=Text())))
    clothing_sizes: Mapped[Optional[dict]] = mapped_column(JSONB)
    color_preferences: Mapped[Optional[dict]] = mapped_column(JSONB)
    customer_preferences: Mapped[Optional[dict]] = mapped_column(JSONB)
    style_preferences: Mapped[Optional[dict]] = mapped_column(JSONB)
    brand_preferences: Mapped[Optional[dict]] = mapped_column(JSONB)
    loyalty_join_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    referral_code: Mapped[Optional[str]] = mapped_column(String(50))
    referred_by: Mapped[Optional[str]] = mapped_column(String(50))
    newsletter_preferences: Mapped[Optional[dict]] = mapped_column(JSONB)
    last_login_ip: Mapped[Optional[str]] = mapped_column(String(50))
    password_last_changed: Mapped[Optional[datetime.date]] = mapped_column(Date)
    security_questions: Mapped[Optional[dict]] = mapped_column(JSONB)
    last_purchase_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    last_cart_activity: Mapped[Optional[datetime.date]] = mapped_column(Date)
    last_wishlist_update: Mapped[Optional[datetime.date]] = mapped_column(Date)
    browse_history: Mapped[Optional[dict]] = mapped_column(JSONB)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    user: Mapped['UserEntity'] = relationship('UserEntity', back_populates='user_customer')


class UserFederationProvider(Base):
    __tablename__ = 'user_federation_provider'
    __table_args__ = (
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_1fj32f6ptolw2qy60cd8n01e8'),
        PrimaryKeyConstraint('id', name='constraint_5c'),
        Index('idx_usr_fed_prv_realm', 'realm_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    changed_sync_period: Mapped[Optional[int]] = mapped_column(Integer)
    display_name: Mapped[Optional[str]] = mapped_column(String(255))
    full_sync_period: Mapped[Optional[int]] = mapped_column(Integer)
    last_sync: Mapped[Optional[int]] = mapped_column(Integer)
    priority: Mapped[Optional[int]] = mapped_column(Integer)
    provider_name: Mapped[Optional[str]] = mapped_column(String(255))
    realm_id: Mapped[Optional[str]] = mapped_column(String(36))

    realm: Mapped[Optional['Realm']] = relationship('Realm', back_populates='user_federation_provider')
    user_federation_config: Mapped[List['UserFederationConfig']] = relationship('UserFederationConfig', back_populates='user_federation_provider')
    user_federation_mapper: Mapped[List['UserFederationMapper']] = relationship('UserFederationMapper', back_populates='federation_provider')


class UserGroupMembership(Base):
    __tablename__ = 'user_group_membership'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['user_entity.id'], name='fk_user_group_user'),
        PrimaryKeyConstraint('group_id', 'user_id', name='constraint_user_group'),
        Index('idx_user_group_mapping', 'user_id')
    )

    group_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    membership_type: Mapped[str] = mapped_column(String(255))

    user: Mapped['UserEntity'] = relationship('UserEntity', back_populates='user_group_membership')


class UserInfluencer(Base):
    __tablename__ = 'user_influencer'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['user_entity.id'], ondelete='CASCADE', name='user_influencer_user_id_fkey'),
        PrimaryKeyConstraint('id', name='user_influencer_pkey'),
        UniqueConstraint('user_id', name='user_influencer_user_id_key')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[str] = mapped_column(String(36))
    tax_id_type: Mapped[str] = mapped_column(String)
    content_guidelines_accepted: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    ftc_disclosure_accepted: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    coppa_compliant: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    independent_contractor_agreement: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    non_disclosure_agreement: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    professional_name: Mapped[Optional[str]] = mapped_column(String)
    ssn_last_four: Mapped[Optional[str]] = mapped_column(String(4))
    social_media_profiles: Mapped[Optional[dict]] = mapped_column(JSONB)
    content_categories: Mapped[Optional[list]] = mapped_column(ARRAY(String()))
    primary_platform: Mapped[Optional[str]] = mapped_column(String)
    audience_demographics: Mapped[Optional[dict]] = mapped_column(JSONB)
    brand_safety_score: Mapped[Optional[float]] = mapped_column(Double(53))
    authenticity_score: Mapped[Optional[float]] = mapped_column(Double(53))
    engagement_metrics: Mapped[Optional[dict]] = mapped_column(JSONB)
    reach_metrics: Mapped[Optional[dict]] = mapped_column(JSONB)
    portfolio_url: Mapped[Optional[str]] = mapped_column(String)
    media_kit_url: Mapped[Optional[str]] = mapped_column(String)
    past_collaborations: Mapped[Optional[dict]] = mapped_column(JSONB)
    payment_preferences: Mapped[Optional[dict]] = mapped_column(JSONB)
    content_languages: Mapped[Optional[list]] = mapped_column(ARRAY(String()))
    expertise_level: Mapped[Optional[str]] = mapped_column(String(20))
    niche_categories: Mapped[Optional[dict]] = mapped_column(JSONB)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    user: Mapped['UserEntity'] = relationship('UserEntity', back_populates='user_influencer')


class UserPermissions(Base):
    __tablename__ = 'user_permissions'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['user_entity.id'], ondelete='CASCADE', name='user_permissions_user_id_fkey'),
        PrimaryKeyConstraint('id', name='user_permissions_pkey'),
        UniqueConstraint('user_id', name='user_permissions_user_id_key')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    user_id: Mapped[str] = mapped_column(String(36))
    is_campaign_approved: Mapped[bool] = mapped_column(Boolean)
    is_marketplace_approved: Mapped[bool] = mapped_column(Boolean)
    is_nationwide_approved: Mapped[bool] = mapped_column(Boolean)
    is_featured: Mapped[bool] = mapped_column(Boolean)
    account_tier: Mapped[str] = mapped_column(String(20))
    is_banned: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    user_type: Mapped[Optional[str]] = mapped_column(Enum('BRAND', 'INFLUENCER', 'CUSTOMER', name='user_type_enum'))
    ban_reason: Mapped[Optional[str]] = mapped_column(Text)
    ban_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    stripe_account_id: Mapped[Optional[str]] = mapped_column(String(255))
    stripe_access_token: Mapped[Optional[str]] = mapped_column(Text)
    stripe_refresh_token: Mapped[Optional[str]] = mapped_column(Text)
    stripe_scope: Mapped[Optional[str]] = mapped_column(String(255))
    stripe_livemode: Mapped[Optional[bool]] = mapped_column(Boolean)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    user: Mapped['UserEntity'] = relationship('UserEntity', back_populates='user_permissions')


class UserRequiredAction(Base):
    __tablename__ = 'user_required_action'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['user_entity.id'], name='fk_6qj3w1jw9cvafhe19bwsiuvmd'),
        PrimaryKeyConstraint('required_action', 'user_id', name='constraint_required_action'),
        Index('idx_user_reqactions', 'user_id')
    )

    user_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    required_action: Mapped[str] = mapped_column(String(255), primary_key=True, server_default=text("' '::character varying"))

    user: Mapped['UserEntity'] = relationship('UserEntity', back_populates='user_required_action')


class UserRoleMapping(Base):
    __tablename__ = 'user_role_mapping'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['user_entity.id'], name='fk_c4fqv34p1mbylloxang7b1q3l'),
        PrimaryKeyConstraint('role_id', 'user_id', name='constraint_c'),
        Index('idx_user_role_mapping', 'user_id')
    )

    role_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(36), primary_key=True)

    user: Mapped['UserEntity'] = relationship('UserEntity', back_populates='user_role_mapping')


class WebOrigins(Base):
    __tablename__ = 'web_origins'
    __table_args__ = (
        ForeignKeyConstraint(['client_id'], ['client.id'], name='fk_lojpho213xcx4wnkog82ssrfy'),
        PrimaryKeyConstraint('client_id', 'value', name='constraint_web_origins'),
        Index('idx_web_orig_client', 'client_id')
    )

    client_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    value: Mapped[str] = mapped_column(String(255), primary_key=True)

    client: Mapped['Client'] = relationship('Client', back_populates='web_origins')


t_associated_policy = Table(
    'associated_policy', Base.metadata,
    Column('policy_id', String(36), primary_key=True, nullable=False),
    Column('associated_policy_id', String(36), primary_key=True, nullable=False),
    ForeignKeyConstraint(['associated_policy_id'], ['resource_server_policy.id'], name='fk_frsr5s213xcx4wnkog82ssrfy'),
    ForeignKeyConstraint(['policy_id'], ['resource_server_policy.id'], name='fk_frsrpas14xcx4wnkog82ssrfy'),
    PrimaryKeyConstraint('policy_id', 'associated_policy_id', name='constraint_farsrpap'),
    Index('idx_assoc_pol_assoc_pol_id', 'associated_policy_id')
)


class AuthenticationExecution(Base):
    __tablename__ = 'authentication_execution'
    __table_args__ = (
        ForeignKeyConstraint(['flow_id'], ['authentication_flow.id'], name='fk_auth_exec_flow'),
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_auth_exec_realm'),
        PrimaryKeyConstraint('id', name='constraint_auth_exec_pk'),
        Index('idx_auth_exec_flow', 'flow_id'),
        Index('idx_auth_exec_realm_flow', 'realm_id', 'flow_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    authenticator_flow: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    alias: Mapped[Optional[str]] = mapped_column(String(255))
    authenticator: Mapped[Optional[str]] = mapped_column(String(36))
    realm_id: Mapped[Optional[str]] = mapped_column(String(36))
    flow_id: Mapped[Optional[str]] = mapped_column(String(36))
    requirement: Mapped[Optional[int]] = mapped_column(Integer)
    priority: Mapped[Optional[int]] = mapped_column(Integer)
    auth_flow_id: Mapped[Optional[str]] = mapped_column(String(36))
    auth_config: Mapped[Optional[str]] = mapped_column(String(36))

    flow: Mapped[Optional['AuthenticationFlow']] = relationship('AuthenticationFlow', back_populates='authentication_execution')
    realm: Mapped[Optional['Realm']] = relationship('Realm', back_populates='authentication_execution')


class CampaignCommission(Base):
    __tablename__ = 'campaign_commission'
    __table_args__ = (
        ForeignKeyConstraint(['contracted_campaign_id'], ['contracted_campaign.id'], name='campaign_commission_contracted_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_commission_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    contracted_campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    commission_type: Mapped[str] = mapped_column(Enum('PLATFORM', 'AMBASSADOR_BRAND', 'AMBASSADOR_INFLUENCER', name='commissiontypeenum'))
    percentage: Mapped[decimal.Decimal] = mapped_column(Numeric(5, 2))
    base_value: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    commission_value: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    currency: Mapped[str] = mapped_column(String(3))
    status: Mapped[str] = mapped_column(Enum('CALCULATED', 'PENDING', 'PROCESSING', 'PAID', 'FAILED', 'CANCELLED', name='commissionstatusenum'))
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    payment_date: Mapped[Optional[int]] = mapped_column(Integer)
    payment_reference: Mapped[Optional[str]] = mapped_column(String(255))
    payment_details: Mapped[Optional[dict]] = mapped_column(JSON)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    contracted_campaign: Mapped['ContractedCampaign'] = relationship('ContractedCampaign', back_populates='campaign_commission')


class CampaignDeliverable(Base):
    __tablename__ = 'campaign_deliverable'
    __table_args__ = (
        ForeignKeyConstraint(['contracted_campaign_id'], ['contracted_campaign.id'], name='campaign_deliverable_contracted_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_deliverable_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    contracted_campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    deliverable_type: Mapped[str] = mapped_column(Enum('POST', 'STORY', 'REEL', 'VIDEO', 'LIVE', 'OTHER', name='deliverabletypeenum'))
    platform: Mapped[str] = mapped_column(Enum('INSTAGRAM', 'TIKTOK', 'YOUTUBE', 'FACEBOOK', 'OTHER', name='platformenum'))
    status: Mapped[str] = mapped_column(Enum('PENDING', 'SUBMITTED', 'IN_REVIEW', 'APPROVED', 'REJECTED', 'PUBLISHED', name='deliverablestatusenum'))
    revision_count: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    content_approve_url: Mapped[Optional[str]] = mapped_column(Text)
    content_publication_url: Mapped[Optional[str]] = mapped_column(Text)
    preview_url: Mapped[Optional[str]] = mapped_column(Text)
    submission_date: Mapped[Optional[int]] = mapped_column(Integer)
    approval_date: Mapped[Optional[int]] = mapped_column(Integer)
    publication_date: Mapped[Optional[int]] = mapped_column(Integer)
    reviewer_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    review_notes: Mapped[Optional[str]] = mapped_column(Text)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    contracted_campaign: Mapped['ContractedCampaign'] = relationship('ContractedCampaign', back_populates='campaign_deliverable')


class CampaignInvoice(Base):
    __tablename__ = 'campaign_invoice'
    __table_args__ = (
        ForeignKeyConstraint(['contracted_campaign_id'], ['contracted_campaign.id'], name='campaign_invoice_contracted_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_invoice_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    contracted_campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    invoice_type: Mapped[str] = mapped_column(Enum('INFLUENCER_INVOICE', 'PLATFORM_INVOICE', 'SERVICE_INVOICE', 'COMMISSION_INVOICE', name='invoicetypeenum'))
    invoice_date: Mapped[int] = mapped_column(Integer)
    due_date: Mapped[int] = mapped_column(Integer)
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(12, 2))
    billing_details: Mapped[dict] = mapped_column(JSON)
    invoice_items: Mapped[dict] = mapped_column(JSON)
    status: Mapped[str] = mapped_column(Enum('DRAFT', 'PENDING', 'PAID', 'CANCELLED', 'OVERDUE', name='invoicestatusenum'))
    created_by: Mapped[uuid.UUID] = mapped_column(Uuid)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    invoice_number: Mapped[Optional[str]] = mapped_column(Text)
    tax_amount: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(12, 2))
    invoice_url: Mapped[Optional[str]] = mapped_column(Text)
    payment_receipt_url: Mapped[Optional[str]] = mapped_column(Text)
    notes: Mapped[Optional[str]] = mapped_column(Text)
    internal_notes: Mapped[Optional[str]] = mapped_column(Text)
    approved_by: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    approved_at: Mapped[Optional[int]] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    contracted_campaign: Mapped['ContractedCampaign'] = relationship('ContractedCampaign', back_populates='campaign_invoice')


class CampaignNegotiation(Base):
    __tablename__ = 'campaign_negotiation'
    __table_args__ = (
        ForeignKeyConstraint(['campaign_invite_id'], ['campaign_invite.id'], name='campaign_negotiation_campaign_invite_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_negotiation_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    campaign_invite_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    influencer_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    negotiation_type: Mapped[str] = mapped_column(Enum('VALUE_PROPOSAL', 'DELIVERABLE_CHANGE', 'TIMELINE_CHANGE', name='negotiationtypeenum'))
    brand_confirmation: Mapped[bool] = mapped_column(Boolean)
    influencer_confirmation: Mapped[bool] = mapped_column(Boolean)
    status: Mapped[str] = mapped_column(Enum('PENDING', 'ACCEPTED', 'REJECTED', 'CANCELLED', name='negotiationstatusenum'))
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    previous_value: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(12, 2))
    proposed_value: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(12, 2))
    changes_proposed: Mapped[Optional[dict]] = mapped_column(JSON)
    response: Mapped[Optional[str]] = mapped_column(Text)
    responded_at: Mapped[Optional[int]] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    campaign_invite: Mapped['CampaignInvite'] = relationship('CampaignInvite', back_populates='campaign_negotiation')


class CampaignPayment(Base):
    __tablename__ = 'campaign_payment'
    __table_args__ = (
        ForeignKeyConstraint(['contracted_campaign_id'], ['contracted_campaign.id'], name='campaign_payment_contracted_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_payment_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    contracted_campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    status: Mapped[str] = mapped_column(Enum('PENDING', 'PROCESSING', 'COMPLETED', 'FAILED', 'REFUNDED', name='paymentstatusenum'))
    commission_paid: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    gateway_payment_id: Mapped[Optional[str]] = mapped_column(String(255))
    gateway_response: Mapped[Optional[dict]] = mapped_column(JSON)
    payment_date: Mapped[Optional[int]] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    contracted_campaign: Mapped['ContractedCampaign'] = relationship('ContractedCampaign', back_populates='campaign_payment')


class CampaignReview(Base):
    __tablename__ = 'campaign_review'
    __table_args__ = (
        ForeignKeyConstraint(['contracted_campaign_id'], ['contracted_campaign.id'], name='campaign_review_contracted_campaign_id_fkey'),
        PrimaryKeyConstraint('id', name='campaign_review_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    contracted_campaign_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    brand_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    influencer_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    reviewer_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    reviewer_role: Mapped[str] = mapped_column(Enum('BRAND', 'INFLUENCER', name='reviewerroleenum'))
    communication_rating: Mapped[int] = mapped_column(Integer)
    content_quality_rating: Mapped[int] = mapped_column(Integer)
    deadline_compliance_rating: Mapped[int] = mapped_column(Integer)
    is_public: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    general_feedback: Mapped[Optional[str]] = mapped_column(Text)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    contracted_campaign: Mapped['ContractedCampaign'] = relationship('ContractedCampaign', back_populates='campaign_review')


class ChatMessage(Base):
    __tablename__ = 'chat_message'
    __table_args__ = (
        ForeignKeyConstraint(['chat_id'], ['campaign_chat.id'], name='chat_message_chat_id_fkey'),
        PrimaryKeyConstraint('id', name='chat_message_pkey'),
        Index('idx_chat_message_chat_id', 'chat_id'),
        Index('idx_chat_message_created_at', 'created_at'),
        Index('idx_chat_message_sender_id', 'sender_id')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    chat_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    sender_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    sender_type: Mapped[str] = mapped_column(Enum('BRAND', 'INFLUENCER', name='sendertypeenum'))
    message_type: Mapped[str] = mapped_column(Enum('TEXT', 'IMAGE', 'DOCUMENT', 'PROPOSAL', name='messagetypeenum'))
    content: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Enum('SENT', 'READ', name='messagestatusenum'))
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    read_at: Mapped[Optional[int]] = mapped_column(Integer)
    deleted_at: Mapped[Optional[int]] = mapped_column(Integer)

    chat: Mapped['CampaignChat'] = relationship('CampaignChat', back_populates='chat_message')


class ComponentConfig(Base):
    __tablename__ = 'component_config'
    __table_args__ = (
        ForeignKeyConstraint(['component_id'], ['component.id'], name='fk_component_config'),
        PrimaryKeyConstraint('id', name='constr_component_config_pk'),
        Index('idx_compo_config_compo', 'component_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    component_id: Mapped[str] = mapped_column(String(36))
    name: Mapped[str] = mapped_column(String(255))
    value: Mapped[Optional[str]] = mapped_column(Text)

    component: Mapped['Component'] = relationship('Component', back_populates='component_config')


t_composite_role = Table(
    'composite_role', Base.metadata,
    Column('composite', String(36), primary_key=True, nullable=False),
    Column('child_role', String(36), primary_key=True, nullable=False),
    ForeignKeyConstraint(['child_role'], ['keycloak_role.id'], name='fk_gr7thllb9lu8q4vqa4524jjy8'),
    ForeignKeyConstraint(['composite'], ['keycloak_role.id'], name='fk_a63wvekftu8jo1pnj81e7mce2'),
    PrimaryKeyConstraint('composite', 'child_role', name='constraint_composite_role'),
    Index('idx_composite', 'composite'),
    Index('idx_composite_child', 'child_role')
)


class IdentityProviderConfig(Base):
    __tablename__ = 'identity_provider_config'
    __table_args__ = (
        ForeignKeyConstraint(['identity_provider_id'], ['identity_provider.internal_id'], name='fkdc4897cf864c4e43'),
        PrimaryKeyConstraint('identity_provider_id', 'name', name='constraint_d')
    )

    identity_provider_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[Optional[str]] = mapped_column(Text)

    identity_provider: Mapped['IdentityProvider'] = relationship('IdentityProvider', back_populates='identity_provider_config')


class IdpMapperConfig(Base):
    __tablename__ = 'idp_mapper_config'
    __table_args__ = (
        ForeignKeyConstraint(['idp_mapper_id'], ['identity_provider_mapper.id'], name='fk_idpmconfig'),
        PrimaryKeyConstraint('idp_mapper_id', 'name', name='constraint_idpmconfig')
    )

    idp_mapper_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[Optional[str]] = mapped_column(Text)

    idp_mapper: Mapped['IdentityProviderMapper'] = relationship('IdentityProviderMapper', back_populates='idp_mapper_config')


class PolicyConfig(Base):
    __tablename__ = 'policy_config'
    __table_args__ = (
        ForeignKeyConstraint(['policy_id'], ['resource_server_policy.id'], name='fkdc34197cf864c4e43'),
        PrimaryKeyConstraint('policy_id', 'name', name='constraint_dpc')
    )

    policy_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[Optional[str]] = mapped_column(Text)

    policy: Mapped['ResourceServerPolicy'] = relationship('ResourceServerPolicy', back_populates='policy_config')


class ProtocolMapperConfig(Base):
    __tablename__ = 'protocol_mapper_config'
    __table_args__ = (
        ForeignKeyConstraint(['protocol_mapper_id'], ['protocol_mapper.id'], name='fk_pmconfig'),
        PrimaryKeyConstraint('protocol_mapper_id', 'name', name='constraint_pmconfig')
    )

    protocol_mapper_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[Optional[str]] = mapped_column(Text)

    protocol_mapper: Mapped['ProtocolMapper'] = relationship('ProtocolMapper', back_populates='protocol_mapper_config')


class ResourceAttribute(Base):
    __tablename__ = 'resource_attribute'
    __table_args__ = (
        ForeignKeyConstraint(['resource_id'], ['resource_server_resource.id'], name='fk_5hrm2vlf9ql5fu022kqepovbr'),
        PrimaryKeyConstraint('id', name='res_attr_pk')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True, server_default=text("'sybase-needs-something-here'::character varying"))
    name: Mapped[str] = mapped_column(String(255))
    resource_id: Mapped[str] = mapped_column(String(36))
    value: Mapped[Optional[str]] = mapped_column(String(255))

    resource: Mapped['ResourceServerResource'] = relationship('ResourceServerResource', back_populates='resource_attribute')


t_resource_policy = Table(
    'resource_policy', Base.metadata,
    Column('resource_id', String(36), primary_key=True, nullable=False),
    Column('policy_id', String(36), primary_key=True, nullable=False),
    ForeignKeyConstraint(['policy_id'], ['resource_server_policy.id'], name='fk_frsrpp213xcx4wnkog82ssrfy'),
    ForeignKeyConstraint(['resource_id'], ['resource_server_resource.id'], name='fk_frsrpos53xcx4wnkog82ssrfy'),
    PrimaryKeyConstraint('resource_id', 'policy_id', name='constraint_farsrpp'),
    Index('idx_res_policy_policy', 'policy_id')
)


t_resource_scope = Table(
    'resource_scope', Base.metadata,
    Column('resource_id', String(36), primary_key=True, nullable=False),
    Column('scope_id', String(36), primary_key=True, nullable=False),
    ForeignKeyConstraint(['resource_id'], ['resource_server_resource.id'], name='fk_frsrpos13xcx4wnkog82ssrfy'),
    ForeignKeyConstraint(['scope_id'], ['resource_server_scope.id'], name='fk_frsrps213xcx4wnkog82ssrfy'),
    PrimaryKeyConstraint('resource_id', 'scope_id', name='constraint_farsrsp'),
    Index('idx_res_scope_scope', 'scope_id')
)


class ResourceServerPermTicket(Base):
    __tablename__ = 'resource_server_perm_ticket'
    __table_args__ = (
        ForeignKeyConstraint(['policy_id'], ['resource_server_policy.id'], name='fk_frsrpo2128cx4wnkog82ssrfy'),
        ForeignKeyConstraint(['resource_id'], ['resource_server_resource.id'], name='fk_frsrho213xcx4wnkog83sspmt'),
        ForeignKeyConstraint(['resource_server_id'], ['resource_server.id'], name='fk_frsrho213xcx4wnkog82sspmt'),
        ForeignKeyConstraint(['scope_id'], ['resource_server_scope.id'], name='fk_frsrho213xcx4wnkog84sspmt'),
        PrimaryKeyConstraint('id', name='constraint_fapmt'),
        UniqueConstraint('owner', 'requester', 'resource_server_id', 'resource_id', 'scope_id', name='uk_frsr6t700s9v50bu18ws5pmt'),
        Index('idx_perm_ticket_owner', 'owner'),
        Index('idx_perm_ticket_requester', 'requester')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    owner: Mapped[str] = mapped_column(String(255))
    requester: Mapped[str] = mapped_column(String(255))
    created_timestamp: Mapped[int] = mapped_column(BigInteger)
    resource_id: Mapped[str] = mapped_column(String(36))
    resource_server_id: Mapped[str] = mapped_column(String(36))
    granted_timestamp: Mapped[Optional[int]] = mapped_column(BigInteger)
    scope_id: Mapped[Optional[str]] = mapped_column(String(36))
    policy_id: Mapped[Optional[str]] = mapped_column(String(36))

    policy: Mapped[Optional['ResourceServerPolicy']] = relationship('ResourceServerPolicy', back_populates='resource_server_perm_ticket')
    resource: Mapped['ResourceServerResource'] = relationship('ResourceServerResource', back_populates='resource_server_perm_ticket')
    resource_server: Mapped['ResourceServer'] = relationship('ResourceServer', back_populates='resource_server_perm_ticket')
    scope: Mapped[Optional['ResourceServerScope']] = relationship('ResourceServerScope', back_populates='resource_server_perm_ticket')


class ResourceUris(Base):
    __tablename__ = 'resource_uris'
    __table_args__ = (
        ForeignKeyConstraint(['resource_id'], ['resource_server_resource.id'], name='fk_resource_server_uris'),
        PrimaryKeyConstraint('resource_id', 'value', name='constraint_resour_uris_pk')
    )

    resource_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    value: Mapped[str] = mapped_column(String(255), primary_key=True)

    resource: Mapped['ResourceServerResource'] = relationship('ResourceServerResource', back_populates='resource_uris')


class RoleAttribute(Base):
    __tablename__ = 'role_attribute'
    __table_args__ = (
        ForeignKeyConstraint(['role_id'], ['keycloak_role.id'], name='fk_role_attribute_id'),
        PrimaryKeyConstraint('id', name='constraint_role_attribute_pk'),
        Index('idx_role_attribute', 'role_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    role_id: Mapped[str] = mapped_column(String(36))
    name: Mapped[str] = mapped_column(String(255))
    value: Mapped[Optional[str]] = mapped_column(String(255))

    role: Mapped['KeycloakRole'] = relationship('KeycloakRole', back_populates='role_attribute')


t_scope_policy = Table(
    'scope_policy', Base.metadata,
    Column('scope_id', String(36), primary_key=True, nullable=False),
    Column('policy_id', String(36), primary_key=True, nullable=False),
    ForeignKeyConstraint(['policy_id'], ['resource_server_policy.id'], name='fk_frsrasp13xcx4wnkog82ssrfy'),
    ForeignKeyConstraint(['scope_id'], ['resource_server_scope.id'], name='fk_frsrpass3xcx4wnkog82ssrfy'),
    PrimaryKeyConstraint('scope_id', 'policy_id', name='constraint_farsrsps'),
    Index('idx_scope_policy_policy', 'policy_id')
)


class UserConsentClientScope(Base):
    __tablename__ = 'user_consent_client_scope'
    __table_args__ = (
        ForeignKeyConstraint(['user_consent_id'], ['user_consent.id'], name='fk_grntcsnt_clsc_usc'),
        PrimaryKeyConstraint('user_consent_id', 'scope_id', name='constraint_grntcsnt_clsc_pm'),
        Index('idx_usconsent_clscope', 'user_consent_id'),
        Index('idx_usconsent_scope_id', 'scope_id')
    )

    user_consent_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    scope_id: Mapped[str] = mapped_column(String(36), primary_key=True)

    user_consent: Mapped['UserConsent'] = relationship('UserConsent', back_populates='user_consent_client_scope')


class UserFederationConfig(Base):
    __tablename__ = 'user_federation_config'
    __table_args__ = (
        ForeignKeyConstraint(['user_federation_provider_id'], ['user_federation_provider.id'], name='fk_t13hpu1j94r2ebpekr39x5eu5'),
        PrimaryKeyConstraint('user_federation_provider_id', 'name', name='constraint_f9')
    )

    user_federation_provider_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[Optional[str]] = mapped_column(String(255))

    user_federation_provider: Mapped['UserFederationProvider'] = relationship('UserFederationProvider', back_populates='user_federation_config')


class UserFederationMapper(Base):
    __tablename__ = 'user_federation_mapper'
    __table_args__ = (
        ForeignKeyConstraint(['federation_provider_id'], ['user_federation_provider.id'], name='fk_fedmapperpm_fedprv'),
        ForeignKeyConstraint(['realm_id'], ['realm.id'], name='fk_fedmapperpm_realm'),
        PrimaryKeyConstraint('id', name='constraint_fedmapperpm'),
        Index('idx_usr_fed_map_fed_prv', 'federation_provider_id'),
        Index('idx_usr_fed_map_realm', 'realm_id')
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    federation_provider_id: Mapped[str] = mapped_column(String(36))
    federation_mapper_type: Mapped[str] = mapped_column(String(255))
    realm_id: Mapped[str] = mapped_column(String(36))

    federation_provider: Mapped['UserFederationProvider'] = relationship('UserFederationProvider', back_populates='user_federation_mapper')
    realm: Mapped['Realm'] = relationship('Realm', back_populates='user_federation_mapper')
    user_federation_mapper_config: Mapped[List['UserFederationMapperConfig']] = relationship('UserFederationMapperConfig', back_populates='user_federation_mapper')


class UserFederationMapperConfig(Base):
    __tablename__ = 'user_federation_mapper_config'
    __table_args__ = (
        ForeignKeyConstraint(['user_federation_mapper_id'], ['user_federation_mapper.id'], name='fk_fedmapper_cfg'),
        PrimaryKeyConstraint('user_federation_mapper_id', 'name', name='constraint_fedmapper_cfg_pm')
    )

    user_federation_mapper_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[Optional[str]] = mapped_column(String(255))

    user_federation_mapper: Mapped['UserFederationMapper'] = relationship('UserFederationMapper', back_populates='user_federation_mapper_config')
