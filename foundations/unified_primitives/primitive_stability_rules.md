# PRIMITIVE STABILITY RULES

## Purpose

This document defines the rules for maintaining stable primitive definitions across TIG, SIR, and SGI.

---

## Rule 1 — No Redefinition Outside SIR

Primitive definitions may only be changed inside SIR.

TIG and SGI may specialize primitives,
but must not redefine them.

---

## Rule 2 — No Semantic Drift

A primitive must retain the same meaning across:

- physical usage
- mathematical abstraction
- technical implementation

---

## Rule 3 — Explicit Status

Each primitive must be classified as:

- formal
- semi-formal
- heuristic
- speculative

---

## Rule 4 — Dependency Control

A primitive must not depend on higher-level implementation structures.

---

## Rule 5 — Version Synchronization

Any primitive change must update:

- global_glossary.md
- cross_repo_mapping.md
- CANONICAL_REFERENCE_HIERARCHY.md

---

## Current Status

Primitive stabilization layer.
