# Prompts: The AI Team

One prompt per role. Each step's chat follows its prompt: attach the file and
say "Please follow this prompt," or paste everything below its line.
`START-HERE.md` explains the order, and what to attach to each.

| Step | Role | Prompt | Where to run it |
|---|---|---|---|
| 1. Tracking (first, and throughout) | Scrum Master | [`c01-tracking-prompt.md`](c01-tracking-prompt.md) | A chat in your Claude Project, kept open all project |
| 2. Feasibility | Product Manager | [`c02-feasibility-prompt.md`](c02-feasibility-prompt.md) | A chat in your Claude Project |
| 3. Requirements | Product Manager | [`c03-requirements-prompt.md`](c03-requirements-prompt.md) | A chat in your Claude Project |
| 4. Design | Software Architect | [`c04-design-prompt.md`](c04-design-prompt.md) | A chat in your Claude Project |
| 5. User Experience | UI/UX Designer | [`c05-user-experience-prompt.md`](c05-user-experience-prompt.md) | A chat in your Claude Project |
| 6. Initial Infrastructure | DevOps Engineer | [`c06-initial-infrastructure-prompt.md`](c06-initial-infrastructure-prompt.md) | Claude Code, in the project folder |
| 7. Test Creation | SDET | [`c07-test-creation-prompt.md`](c07-test-creation-prompt.md) | Claude Code |
| 8. Implementation | Software Engineer | [`c08-01-implementation-prompt.md`](c08-01-implementation-prompt.md) | Claude Code |
| 8. Code reviews (rounds 1 and 2) | Independent Code Reviewer | [`c08-02-code-review-prompt.md`](c08-02-code-review-prompt.md) | Round 1: another company's AI, such as Codex, read-only. Round 2: a **new** Claude Code session |
| 8. Polishing | Polishing Partner, with you | [`c08-04-polishing-prompt.md`](c08-04-polishing-prompt.md) | Claude Code |
| 8. Hands-on review (round 3) | Hands-On Review Helper, for a person | [`c08-03-hands-on-review-prompt.md`](c08-03-hands-on-review-prompt.md) | A chat in your Claude Project |
| 9. Release | Release Manager | [`c09-release-prompt.md`](c09-release-prompt.md) | A chat, then Claude Code for the move |
| 10. Maintenance | SRE / Maintenance Engineer | [`c10-maintenance-prompt.md`](c10-maintenance-prompt.md) | Claude Code |

These are copies of the prompts in the workflow repo's
[`prompts/`](https://github.com/b0ts/ai_assisted_sdlc_workflow/tree/main/prompts)
folder. You may edit your copies to fit your project (for example, to add
your organization's name); keep the c-numbers, so the chats and documents
still match.
