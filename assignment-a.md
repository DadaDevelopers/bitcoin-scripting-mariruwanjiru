# Assignment A - Bitcoin Script Analysis

## Script: P2PKH (Pay to Public Key Hash)
OP_DUP OP_HASH160 <PubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
## Task 1: Opcode Breakdown

| Opcode | Purpose |
|--------|---------|
| OP_DUP | Duplicates the top stack item (the public key) |
| OP_HASH160 | Hashes the top stack item with SHA256 then RIPEMD160 |
| <PubKeyHash> | The expected hash of the recipient's public key |
| OP_EQUALVERIFY | Verifies the two hashes match, fails if they don't |
| OP_CHECKSIG | Verifies the signature against the public key |

## Task 2: Data Flow
Unlocking Script Input:
<Signature> <PublicKey>
Step 1 - OP_DUP:
Stack: <Signature> <PublicKey> <PublicKey>
Step 2 - OP_HASH160:
Stack: <Signature> <PublicKey> <Hash160(PublicKey)>
Step 3 - Push <PubKeyHash>:
Stack: <Signature> <PublicKey> <Hash160(PublicKey)> <PubKeyHash>
Step 4 - OP_EQUALVERIFY:
Checks: Hash160(PublicKey) == PubKeyHash
Stack: <Signature> <PublicKey>
Step 5 - OP_CHECKSIG:
Checks: Signature is valid for PublicKey
Stack: TRUE (if valid)

## Task 3: What Happens if Signature Verification Fails

If signature verification fails at OP_CHECKSIG:
- The script returns FALSE
- The transaction is considered INVALID
- The transaction is rejected by the network
- The funds remain unspent and locked in the UTXO
- No coins are moved under any circumstance

## Task 4: Security Benefits of Hash Verification

1. **Privacy**: The public key is not revealed until spending time. Only the hash is visible on the blockchain before spending, protecting the owner's identity.

2. **Quantum resistance**: Since only the hash is exposed (not the public key), it provides an extra layer of protection against potential future quantum computing attacks.

3. **Integrity**: OP_EQUALVERIFY ensures the spender must prove they own the exact public key that hashes to the address. No other key can produce the same hash (collision resistance).

4. **Double verification**: The script requires BOTH hash match AND valid signature, meaning an attacker would need to both find a hash collision AND forge a signature — computationally infeasible.