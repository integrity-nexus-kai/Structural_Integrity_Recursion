# Definitions

## Time

\( t \)

Time parameter of system evolution.

Time may be discrete or continuous.

---

## System State

\( x(t) \)

State of the system at time \(t\).

The internal structure of the state space is not specified.

---

## Consistency Structure

\( \mathcal{C} \)

Constraint structure defining admissible and non-admissible system configurations.

The consistency structure may contain:

- invariant components,
- adaptive components,
- or recursively updated constraints.

---

## Integrity

\( I(t) \in \mathbb{R}_{\ge 0} \)

Integrity measure of the system at time \(t\).

Higher values correspond to greater compatibility between:

- current system state,
- and consistency structure.

No specific metric is imposed.

---

## Integrity Deviation

\( D(t) \in \mathbb{R}_{\ge 0} \)

Magnitude of inconsistency between:

- current system state,
- and consistency structure.

\(D(t)=0\) corresponds to full compatibility.

---

## Observed Deviation

\( \hat{D}(t) \)

Internally detected or processed deviation.

In general:

\[
\hat{D}(t) \le D(t)
\]

The system may not fully observe its own inconsistencies.

---

## Update Operator

\( U(t) \)

Operator describing system adaptation.

The update process modifies the current state according to detected inconsistencies.

General form:

\[
x(t+1)
=
U\big(x(t), \hat{D}(t), \mathcal{C}(t)\big)
\]

---

## Integrity Change

\[
\Delta I(t)
=
I(t+1)-I(t)
\]

Interpretation:

- \( \Delta I(t) > 0 \): integrity improvement
- \( \Delta I(t) < 0 \): integrity degradation
- \( \Delta I(t) = 0 \): neutral update

---

## Recursive Integrity Components

Three minimal recursive components are introduced.

### Detection Rate

\( R_e(t) \)

Ability to detect inconsistencies.

---

### Reaction Rate

\( R_r(t) \)

Temporal responsiveness of corrective updates.

---

### Correction Effectiveness

\( R_c(t) \)

Expected effectiveness of updates on integrity change.

---

## Structural Integrity Recursion

The Structural Integrity Recursion function is defined abstractly as:

\[
\mathrm{SIR}(t)
=
F\big(
R_e(t),
R_r(t),
R_c(t)
\big)
\]

where \(F\) is a monotonic aggregation function.

No explicit functional form is imposed.
