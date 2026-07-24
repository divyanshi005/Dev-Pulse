                  GitHub REST API
                         │
          Page 1   Page 2   Page 3
             │        │        │
             └────────┴────────┘
                      │
                      ▼
              GitHub Extractor
                      │
                      ▼
          Raw JSON (30 repositories)
                      │
                      ▼
             GitHub Transformer
                      │
                      ▼
             Repository Dataclass
                      │
                      ▼
              PostgreSQL Loader
                      │
                      ▼
        staging.github_repositories