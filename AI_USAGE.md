# AI Usage Disclosure

Use this format for each significant AI-assisted contribution.

## Disclosure Entry

- **Date:**
- **AI tool:**
- **What I asked:**
- **What the agent produced:**
- **What I changed, rejected, or corrected:**

## Entry 1

- **Date:** 2026-09-13
- **AI tool:** GitHub Copilot
- **What I asked:** Create the initial Python project structure and development-tool configuration for CSC 582 Assignment #1 without implementing classes or circuit logic.
- **What the agent produced:** The requested directory scaffold, Python package initializers, pytest, Black, and pdoc configuration, dependency list, ignore rules, README, AI disclosure template, and empty-directory placeholders.
- **What I changed, rejected, or corrected:** I will copy the unmodified `munger.py` from the professor's distribution repository; it was not recreated or modified by the agent.

## Entry 2

- **Date:** 2026-09-13
- **AI tool:** GitHub Copilot
- **What I asked:** Create and test only the `AbstractDevice` base class using Python's `ABC` and `abstractmethod`, without implementing gates, adders, or circuit logic.
- **What the agent produced:** `source/FourBitAdder/intern/AbstractDevice.py` with one abstract `update(self) -> None` method, plus a pytest test proving direct instantiation raises `TypeError`.
- **What I changed, rejected, or corrected:** No changes, rejections, or corrections were made.

## Entry 3

- **Date:** 2026-09-13
- **AI tool:** OpenAI Codex
- **What I asked:** Inspect the official assignment sources and current project without implementing anything, then complete only the approved AbstractDevice documentation and test stage.
- **What the agent produced:** An inspection report covering the PDF, walkthrough, architecture, starter pseudocode, local files, Git history, and official munger checksum. After approval, clarified the setter/update guarantee in AbstractDevice docstrings and added tests for an incomplete subclass and a concrete update override. The tests use local test-only subclasses, not new circuit APIs. Ran Black on source and tests and ran the complete pytest suite.
- **What I changed, rejected, or corrected:** I approved the limited AbstractDevice stage. No further user changes, rejections, or corrections have been reported. Codex noted that the abstract method requires an implementation but does not automatically enforce calls from future input setters; those will need verification when implemented.

## Entry 4

- **Date:** 2026-09-13
- **AI tool:** OpenAI Codex
- **What I asked:** Investigate the test-file import error, then identified the Pylance warning that FourBitAdder.intern.AbstractDevice could not be resolved.
- **What the agent produced:** Confirmed the existing pytest suite passes and added .vscode/settings.json with python.analysis.extraPaths pointing to ./source, following Microsoft's documentation. This configures editor import resolution separately from pytest's pythonpath setting. Ran Black and the complete pytest suite; the editor warning itself could not be observed from the terminal.
- **What I changed, rejected, or corrected:** I supplied the exact Pylance warning. No further user changes, rejections, or corrections have been reported.

## Entry 5

- **Date:** 2026-09-15
- **AI tool:** OpenAI Codex
- **What I asked:** Continue the assignment with another small implementation stage.
- **What the agent produced:** Inspected the current files and history and reread the relevant official starter pseudocode. Translated AbstractGate with the starter's pin and method names, inherited abstract update contract, and zero-initialized construction. Added contract tests using a recording subclass, plus an incremental Mermaid class diagram. The recording subclass is test-only and implements no Boolean logic. Ran Black on source and tests and the complete pytest suite.
- **What I changed, rejected, or corrected:** No user changes, rejections, or corrections have been reported for this stage. The agent limited this stage to AbstractGate; primitives, generated documentation, and composite circuits remain unfinished.

## README wording revision

- **Date:** 2026-09-18
- **AI tool:** OpenAI Codex
- **What I asked:** Remove assistant-style narration and make the README read as standard project documentation.
- **What the agent produced:** Rewrote README.md with direct setup, usage, architecture, testing, documentation, and submission instructions. Retained the implementation details, assignment layout deviations, and reference to the AI disclosure log.
- **What I changed, rejected, or corrected:** I requested a change in writing style. No subsequent user edits or review have been reported.
