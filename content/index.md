# EDMeta: Editorial Metadata Shortform Specification

## Summary

EDMeta is a compact, machine- and human-readable string format for denoting authorship origin, editorial checks, and licensing on written or media content. It aims to improve transparency, support ethical content sourcing, and enable automated processing or filtering in both human-facing and federated systems.

## Goals

- **Transparency**: Show clearly how a piece of content was created, verified, and licensed.
- **Compactness**: Fit easily in signatures, footers, posts, and metadata headers.
- **Interoperability**: Be parseable into structured formats (e.g., JSON-LD, ActivityStreams).
- **Extensibility**: Allow for future categories or domain-specific extensions.

---

## Syntax

```text
ED:<origin>:<checks>:<license>
```

All segments use shortcodes for compact representation.

### Origin

Describes the creation process:

| Code    | Meaning                               |
|---------|----------------------------------------|
| `H`     | Human-authored                         |
| `AI0`   | Pure AI-generated                      |
| `AI1`   | AI-generated, lightly edited           |
| `AI2`   | Human-led, AI-assisted                 |
| `AI3`   | AI-generated, heavily curated          |
| `+H-ED` | Human-edited (can be appended to AI)   |

Examples:

- `H` → human-authored
- `AI2` → human-led, AI-assisted
- `AI0+H-ED` → AI-generated, then human-edited

### Checks

Editorial and quality checks applied, expressed as 2-letter codes:

| Code | Meaning             |
|------|---------------------|
| `Sp` | Spell-checked       |
| `Gr` | Grammar-checked     |
| `St` | Style-checked       |
| `Ft` | Fact-checked        |
| `Ct` | Sources cited       |
| `Md` | Moderated           |
| `Pr` | Peer-reviewed       |
| `Bs` | Bias-reviewed       |
| `Au` | Author identity verified |

Concatenate without separators:

- `SpGrStFt` = spell, grammar, style, fact checks

### License

Use established short forms:

| Code       | License Description                         |
|------------|---------------------------------------------|
| `CC-BY`    | Creative Commons Attribution                 |
| `CC-NC`    | CC Attribution NonCommercial                 |
| `CC-NC-SA` | CC Attribution NonCommercial ShareAlike     |
| `ARR`      | All Rights Reserved                         |
| `PD`       | Public Domain                               |

---

## Examples

```text
ED:H:SpStFt:CC-BY
```

> Human-authored, spell/style/fact-checked, Creative Commons Attribution

```text
ED:AI0+H-ED:GrCtMd:CC-NC-SA
```

> AI-generated, human-edited, grammar/citation/moderation checked, Creative Commons NonCommercial ShareAlike

---

## Expanded Use

- **JSON-LD Mapping**

  For structured data, map to JSON-LD:

  ```json
  {
    "@context": "https://schema.org",
    "@type": "CreativeWork",
    "authoringOrigin": "human-authored",
    "editorialChecks": ["spell-checked", "style-checked", "fact-checked"],
    "license": "CC Attribution"
  }

  ```json
  {
    "@context": "https://schema.org",
    "@type": "CreativeWork",
    "authoringOrigin": "ai-generated+human-edited",
    "editorialChecks": ["grammar-checked", "sources cited", "moderated"],
    "license": "CC Attribution NonCommercial ShareAlike"
  }
  ```

- **Fediverse Integration**
  Display in footers of posts as:

  ```text
  ED:AI2:SpGr:CC-BY
  ```

  Parsed by clients into readable tooltip or metadata badge.

---

## Roadmap

- [x] Python reference parser and generator
- [x] JavaScript WebComponent for rendering badges
- [x] `edmeta.dev` microsite
- [ ] Registry of community/industry extensions
- [ ] ActivityStreams/AS2 vocabulary alignment
- [ ] microsite validator and live badge generator

---

## Community

EDMeta is a community-driven initiative. We welcome contributions, feedback, and discussions on GitHub.
Join us in shaping the future of editorial metadata!

- [GitHub Discussions](https://github.com/EditorialMetadata/EDMeta/discussions)
- [GitHub Issues](https://github.com/EditorialMetadata/EDMeta/issues)
- [GitHub Repository](https://github.com/EditorialMetadata/EDMeta)

## Contributing

We welcome contributions to EDMeta! Whether you're a developer, designer, or just passionate about editorial metadata, your input is valuable. Please check our [contributing guidelines](https://github.com/EditorialMetadata/EDMeta/blob/main/CONTRIBUTING.md) for more information on how to get involved.

## Acknowledgments

EDMeta is inspired by the need for transparency in content creation and editorial processes. We acknowledge the contributions of the open-source community and the importance of collaboration in shaping this specification.

## Future Directions

- **Domain-Specific Extensions**: Encourage the community to propose and develop domain-specific codes for various industries (e.g., journalism, academia, etc.).
- **Integration with Existing Standards**: Explore alignment with existing metadata standards and frameworks to enhance interoperability.
- **Tooling and Libraries**: Develop libraries and tools in various programming languages to facilitate the adoption of EDMeta in different environments.
- **Community Engagement**: Foster a vibrant community around EDMeta, encouraging discussions, feedback, and contributions to the specification.
- **Educational Resources**: Create documentation, tutorials, and examples to help users understand and implement EDMeta effectively.

## Contact

For inquiries, feedback, or collaboration opportunities, please reach out to us via our [GitHub Discussions](https://github.com/EditorialMetadata/EDMeta/discussions) or [GitHub Issues](https://github.com/EditorialMetadata/EDMeta/issues).

## Licensing & Governance

EDMeta is designed for open adoption. Proposals for new codes should be submitted via GitHub discussions or governance body (TBD).

> _“Clarity is the new trust.”_
