score_question = """Evaluate each question's difficulty (1–10) cumulatively based on the criteria below:

**Group 1: Knowledge Specificity (1–3 points)**  
- 1 point if the question requires advanced or specialized domain knowledge beyond general practitioner-level expertise.
- +1 additional point if deep, niche, or highly specialized expertise is required.
- +1 additional point if answering correctly requires familiarity with obscure, rarely documented, or highly specialized concepts.

*Proceed to Group 2 scoring if the question scores **2 or more points** in Group 1.*

**Group 2: Reasoning Complexity (4–7 points)** *(Award if Group 1 score ≥ 2)*  
- +1 point if solving clearly demands multi-step logical reasoning or inference beyond straightforward deduction.
- +1 additional point if the question requires extracting implicit information, hidden assumptions, or subtle nuances critical to the solution.
- +1 additional point if the question demands synthesizing knowledge or concepts across multiple distinct domains or disciplines.
- +1 additional point if the correct reasoning path or solution is notably non-obvious, counterintuitive, or violates common intuitions.

*Proceed to Group 3 scoring if the question scores at least **1 point** in both previous groups.*

**Group 3: Analytical Creativity (8–10 points)** *(Award if ≥ 1 point each from Groups 1 & 2)*  
- +1 point if the solution requires employing novel, unconventional, or rarely used analytical methods.
- +1 additional point if it substantially challenges creativity in constructing novel reasoning paths or synthesizing entirely new approaches.
- +1 additional point if analogous examples or precedents of this question type are virtually nonexistent or exceedingly rare, making typical problem-solving patterns ineffective.

**Maximum total cumulative score:** 10 points

---

Firstly briefly review the provided question, explain your scoring, then return your final score. Your response must be in the following format:

[Analysis]  
{review of the question, scoring logic goes here}

[Score]  
{N(integer below 10)}

Here is the question you have to score:

[Instruction]"""


refine_question = """I want to refine the question so that it meets the score 10. Your job is to rewrite the question. 
First brainstorm the weakness of the question and possible ways to enhance it.
Then return the refined question. Your output should be in the following format. 

[Brainstorm]  
{brainstorm of weakeness and possible enhancements.}

[Refined Question]
{refined question comes here}

---"""
