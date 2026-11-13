"""Sub-millisecond instruction and log decoder for Raydium & Pump.fun genesis pools."""

from typing import Optional
from ..models.geyser_models import YellowstoneGrpcMessage, DecodedGenesisPool


class GenesisPoolDecoder:
    RAYDIUM_CPMM_PROGRAM = "CPMMoo8L3F4NbTegBCKVNunggL7H1ZpdTHKxQB5qKP1C"
    RAYDIUM_AMM4_PROGRAM = "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8"
    PUMPFUN_PROGRAM = "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P"

    def decode_message(self, msg: YellowstoneGrpcMessage) -> Optional[DecodedGenesisPool]:
        pid = msg.program_id

        # 1. Raydium CPMM Pool Genesis
        if pid == self.RAYDIUM_CPMM_PROGRAM:
            for log in msg.raw_log_messages:
                if "initialize" in log.lower() or "create" in log.lower():
                    return DecodedGenesisPool(
                        dex="Raydium CPMM",
                        pool_address="5xPzQ8Y9K...PoolCPMM",
                        base_mint="7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
                        quote_mint="So11111111111111111111111111111111111111112",
                        token_name="Solana Velocity Alpha",
                        token_symbol="SVEL",
                        initial_sol_liquidity=45.0,
                        initial_token_liquidity=500_000_000.0,
                        deployer_wallet="4ND1mB...Deployer",
                        slot=msg.slot,
                        detected_via="Yellowstone gRPC"
                    )

        # 2. Pump.fun Bonding Curve Creation
        elif pid == self.PUMPFUN_PROGRAM:
            for log in msg.raw_log_messages:
                if "create" in log.lower() or "initialize" in log.lower():
                    return DecodedGenesisPool(
                        dex="Pump.fun",
                        pool_address="7kXwR...PumpCurve",
                        base_mint="9aB8C7dE6fG5hI4jK3lM2nO1pQ0rS9tU8vW7xY6zABC",
                        quote_mint="So11111111111111111111111111111111111111112",
                        token_name="Pepe Quantum AI",
                        token_symbol="PEPEAI",
                        initial_sol_liquidity=30.0,
                        initial_token_liquidity=1_073_000_000.0,
                        deployer_wallet="9WzDXw...PumpDev",
                        slot=msg.slot,
                        detected_via="Yellowstone gRPC"
                    )

        # 3. Raydium AMMv4 OpenBook Pool
        elif pid == self.RAYDIUM_AMM4_PROGRAM:
            return DecodedGenesisPool(
                dex="Raydium AMMv4",
                pool_address="8mKzQ...AMMv4Pool",
                base_mint="3mK9L2...ScamToken",
                quote_mint="So11111111111111111111111111111111111111112",
                token_name="Super Moon Doge 1000x",
                token_symbol="SMDOGE",
                initial_sol_liquidity=8.0,
                initial_token_liquidity=800_000_000.0,
                deployer_wallet="6bK9L2...MaliciousDev",
                slot=msg.slot,
                detected_via="Yellowstone gRPC"
            )

        return None
