"""Data models for Yellowstone gRPC streaming, genesis pair decoding, and audit reports."""

from pydantic import BaseModel, Field
from typing import List, Optional


class YellowstoneGrpcMessage(BaseModel):
    slot: int
    signature: str
    block_time: int
    program_id: str
    raw_log_messages: List[str]
    latency_ms: float


class DecodedGenesisPool(BaseModel):
    dex: str  # "Raydium CPMM" | "Pump.fun" | "Raydium AMMv4"
    pool_address: str
    base_mint: str
    quote_mint: str  # WSOL
    token_name: str
    token_symbol: str
    initial_sol_liquidity: float
    initial_token_liquidity: float
    deployer_wallet: str
    slot: int
    detected_via: str = "Yellowstone gRPC"


class SecurityAuditReport(BaseModel):
    pool: DecodedGenesisPool
    is_safe: bool
    risk_score: int = Field(ge=0, le=100)
    verdict: str  # "SAFE" | "HIGH_RISK" | "HONEYPOT"
    mint_authority_revoked: bool
    freeze_authority_revoked: bool
    lp_burned_pct: float
    dev_holding_pct: float
    jito_bundle_recommended: bool
    recommended_tip_sol: float
    audit_flags: List[str] = Field(default_factory=list)
