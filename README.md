# Whispers

## Abstract
Whispers is an Agent Based Model for rumour dissemination. It is an appropriation of the **SIR model** in the study of epidemiology, which computes the theoretical number of people infected with a contagious illness in a closed population over time. However, only the qualitative aspects of the SIR model will be retained in this appropriation as it remains a stochastic demonstration of the spread of rumours and the SIR is strictly predictable.

Different agents in the system are either spreading or stifling the rumour, or are ignorant to the rumour. Further, the interactions between the different agents are as follows:

*S + I -> S + S*

*S + R -> R + R*

*I + R -> I + R*

It should be noted that an agent interacting with an agent of equal kind is ineffectual.
