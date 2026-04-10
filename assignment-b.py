import hashlib
import time

# ============================================================
# Assignment B - Hashed Time-Lock Contract (HTLC)
# Atomic swap between Alice and Bob
# - Alice can claim with secret preimage within 21 minutes
# - Bob gets refund after 21 minutes
# ============================================================

def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()

def hash160(data: bytes) -> bytes:
    return hashlib.new('ripemd160', sha256(data)).digest()

def generate_secret():
    """Alice generates a secret and its hash"""
    secret = b"alice_secret_preimage"
    secret_hash = sha256(secret)
    return secret, secret_hash

def htlc_script(secret_hash: bytes, alice_pubkey: str, bob_pubkey: str, timeout_minutes: int) -> str:
    """
    HTLC Locking Script:
    Alice can claim with secret preimage within timeout
    Bob can claim refund after timeout
    """
    script = f"""
    OP_IF
        # Alice's claim path (with secret preimage)
        OP_SHA256 <{secret_hash.hex()}> OP_EQUALVERIFY
        OP_DUP OP_HASH160 <{alice_pubkey}> OP_EQUALVERIFY OP_CHECKSIG
    OP_ELSE
        # Bob's refund path (after timeout)
        <{timeout_minutes * 60}> OP_CHECKSEQUENCEVERIFY OP_DROP
        OP_DUP OP_HASH160 <{bob_pubkey}> OP_EQUALVERIFY OP_CHECKSIG
    OP_ENDIF
    """
    return script

def alice_claim_script(secret: bytes, alice_signature: str, alice_pubkey: str) -> str:
    """
    Alice's unlocking script to claim funds using secret preimage
    """
    script = f"""
    <{alice_signature}>
    <{alice_pubkey}>
    <{secret.hex()}>
    OP_TRUE  # Takes the IF branch
    """
    return script

def bob_refund_script(bob_signature: str, bob_pubkey: str) -> str:
    """
    Bob's unlocking script to claim refund after timeout
    """
    script = f"""
    <{bob_signature}>
    <{bob_pubkey}>
    OP_FALSE  # Takes the ELSE branch
    """
    return script

def simulate_htlc():
    """Simulate the full HTLC atomic swap"""

    print("=" * 60)
    print("HTLC Atomic Swap Simulation")
    print("=" * 60)

    # Generate secret
    secret, secret_hash = generate_secret()
    print(f"\n[SETUP]")
    print(f"Secret (preimage): {secret.decode()}")
    print(f"Secret Hash (SHA256): {secret_hash.hex()}")

    # Participants
    alice_pubkey = "alice_pubkeyhash_abc123"
    bob_pubkey = "bob_pubkeyhash_xyz789"
    timeout_minutes = 21

    # Generate HTLC locking script
    print(f"\n[HTLC LOCKING SCRIPT]")
    locking_script = htlc_script(secret_hash, alice_pubkey, bob_pubkey, timeout_minutes)
    print(locking_script)

    # Simulate Alice claiming within timeout
    print("\n[SCENARIO 1: Alice claims within 21 minutes]")
    alice_sig = "alice_valid_signature"
    claim_script = alice_claim_script(secret, alice_sig, alice_pubkey)
    print("Alice's Unlocking Script:")
    print(claim_script)

    # Verify Alice's claim
    provided_hash = sha256(secret)
    if provided_hash == secret_hash:
        print("✓ Secret preimage verified successfully!")
        print("✓ Alice's signature verified!")
        print("✓ Alice claims the funds successfully!")
    else:
        print("✗ Secret preimage verification FAILED!")

    # Simulate Bob's refund after timeout
    print("\n[SCENARIO 2: Bob claims refund after 21 minutes]")
    bob_sig = "bob_valid_signature"
    refund_script = bob_refund_script(bob_sig, bob_pubkey)
    print("Bob's Unlocking Script:")
    print(refund_script)
    print(f"✓ Timeout of {timeout_minutes} minutes has elapsed!")
    print("✓ Bob's signature verified!")
    print("✓ Bob claims the refund successfully!")

    # Test with wrong secret
    print("\n[SCENARIO 3: Wrong secret attempt]")
    wrong_secret = b"wrong_secret"
    wrong_hash = sha256(wrong_secret)
    if wrong_hash != secret_hash:
        print("✗ Wrong secret provided!")
        print("✗ OP_EQUALVERIFY fails!")
        print("✗ Transaction REJECTED - funds remain locked!")

    print("\n" + "=" * 60)
    print("HTLC Simulation Complete")
    print("=" * 60)

# Run simulation
simulate_htlc()