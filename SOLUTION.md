# My Solution - Bitcoin Scripting Assignment

## Overview
This assignment covers Bitcoin Script analysis and implements a Hashed Time-Lock Contract (HTLC) for atomic swaps.

## Files
- `assignment-a.md` — Task A: P2PKH script breakdown, data flow, and security analysis
- `assignment-b.py` — Task B: HTLC implementation in Python
- `output.txt` — Program output from running assignment-b.py

## How to Run
```bash
python3 assignment-b.py
```

## Assignment A Summary
Analysed the P2PKH script `OP_DUP OP_HASH160 <PubKeyHash> OP_EQUALVERIFY OP_CHECKSIG` covering:
- Purpose of each opcode
- Step by step data flow through the stack
- What happens when signature verification fails
- Security benefits of hash verification

## Assignment B Summary
Implemented a Hashed Time-Lock Contract (HTLC) with:
- Alice can claim funds using secret preimage within 21 minutes
- Bob gets a refund after 21 minutes using OP_CHECKSEQUENCEVERIFY
- 3 scenarios tested: Alice claims, Bob refunds, wrong secret rejected