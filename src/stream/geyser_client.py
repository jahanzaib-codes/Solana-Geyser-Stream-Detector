"""Yellowstone gRPC Geyser client emulator streaming raw Solana transactions."""

import time
from typing import List, Tuple
from ..models.geyser_models import YellowstoneGrpcMessage, DecodedGenesisPool, SecurityAuditReport
from ..decoder.genesis_pool_decoder import GenesisPoolDecoder
from ..security.honeypot_pre_auditor import HoneypotPreAuditor


class YellowstoneStreamEmulator:
    def __init__(self):
        self.decoder = GenesisPoolDecoder()
        self.auditor = HoneypotPreAuditor()

    def stream_and_audit(self) -> List[Tuple[YellowstoneGrpcMessage, DecodedGenesisPool, SecurityAuditReport]]:
        now = int(time.time())
        messages = [
            YellowstoneGrpcMessage(
                slot=289410291,
                signature="5KqP7W...RaydiumCPMMGenesis",
                block_time=now - 2,
                program_id="CPMMoo8L3F4NbTegBCKVNunggL7H1ZpdTHKxQB5qKP1C",
                raw_log_messages=["Program CPMMoo8... invoke [1]", "Program log: initialize_pool", "Program success"],
                latency_ms=4.2
            ),
            YellowstoneGrpcMessage(
                slot=289410294,
                signature="3xL9K2...PumpFunGenesis",
                block_time=now - 1,
                program_id="6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P",
                raw_log_messages=["Program 6EF8r... invoke [1]", "Program log: create", "Program success"],
                latency_ms=3.8
            ),
            YellowstoneGrpcMessage(
                slot=289410298,
                signature="4mP8R1...ScamAMM4Genesis",
                block_time=now,
                program_id="675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8",
                raw_log_messages=["Program 675kP... invoke [1]", "Program log: initialize2", "Program success"],
                latency_ms=5.1
            )
        ]

        results = []
        for msg in messages:
            pool = self.decoder.decode_message(msg)
            if pool:
                audit = self.auditor.audit_pool(pool)
                results.append((msg, pool, audit))

        return results
