# dustjacket

A Claude Code skill that restyles, generates, and drift-checks READMEs in their repo type's house
style and a chosen voice — without fabricating anything. See [PRODUCT.md](PRODUCT.md) for product
context, [docs/design.md](docs/design.md) for the skill design, and [docs/research.md](docs/research.md)
for the extracted rules.

## Review workflow

### Context documents

- **PRODUCT.md** — product context, personas, principles, feature map. Read before any product decision.
- **DESIGN.md** — design system, colors, typography, component patterns. Read before any UI work.

### Quality gates

| Gate | When | Command |
|------|------|---------|
| Should we build? | Before any engineering | `/gate-should-we-build [idea]` |
| Design review | After design doc, before implementation | `/gate-design-review` |
| Audit | After implementation, before acceptance | `/audit` |
| Acceptance | After audit passes, before merge | `/gate-acceptance` |

### Periodic reviews

| Review | Cadence | Command |
|--------|---------|---------|
| Codebase health | Weekly or pre-milestone | `/review-codebase-health` |
| Frontend health | Monthly or post-UI-sprint | `/review-frontend-health` |
| Architecture | Quarterly or pre-major-feature | `/review-architecture` |
| Product health | Monthly | `/review-product-health` |
| README drift | After a release or feature batch | `/review-readme` |
| All reviews | As needed | `/deep-review` |

### After each review

1. Fix any **critical** findings before the next feature
2. File **important** findings as tasks to address this cycle
3. Track **minor** findings — they compound if ignored
4. Update context docs if the review surfaced changes:
   - `/review-product-health` updates PRODUCT.md
   - `/review-frontend-health` updates DESIGN.md
   - `/review-architecture` updates CLAUDE.md
   - `/review-readme` proposes a README.md diff
