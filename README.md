[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/S_3oprdD)
# assignment-4
Bitcoin Scripting

# Bitcoin Scripting Assignment

## Assignment A

### Given Script:
```
OP_DUP OP_HASH160 <PubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

### Tasks:

1. Break down each opcode's purpose
2. Create a diagram showing data flow
3. Identify what happens if signature verification fails
4. Explain the security benefits of hash verification

---

## Assignment B

### Implement a Hashed Time-Lock Contract for atomic swap between Alice and Bob:

- Alice can claim with secret preimage within 21 minutes
- Bob gets refund after 21 minutes

### Tasks:

1. Complete the HTLC script
2. Create claiming transaction script
3. Create refund transaction script
4. Test with sample hash and timeout
