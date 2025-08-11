# 📈 Daily Statistics

```diff
 .github/scripts/README.md                          |   141 +
 .github/scripts/analyze-git-activity.sh            |    59 +
 .github/scripts/calculate-week-info.sh             |    44 +
 .github/scripts/create-docusaurus-structure.sh     |   111 +
 .github/scripts/generate-markdown-reports.sh       |   191 +
 .github/scripts/generate_daily_report.py           |   251 +
 .github/scripts/sync-to-hub-gh.sh                  |   182 +
 .github/scripts/sync-to-hub.sh                     |   184 +
 .github/workflows/daily-ai-report.yml              |    39 +
 .github/workflows/gh_actions_deploy.yml            |   110 +
 .github/workflows/sync-to-report-gh.yml            |    53 +
 .gitignore                                         |     2 +
 README.md                                          |   298 +-
 .../2025-08-02/daily-report-hub_sample1/README.md  |    16 -
 .../daily-report-hub_sample1/daily_code_diff.md    |    13 -
 .../daily-report-hub_sample1/daily_code_diff.txt   |   151 -
 .../daily-report-hub_sample1/daily_commits.md      |    66 -
 .../daily-report-hub_sample1/daily_commits.txt     |    10 -
 .../daily_cumulative_diff.md                       |    10 -
 .../daily_cumulative_diff.txt                      |     8 -
 .../daily-report-hub_sample1/daily_diff_stats.md   |    11 -
 .../daily-report-hub_sample1/daily_diff_stats.txt  |     9 -
 .../daily-report-hub_sample1/daily_summary.md      |   104 -
 .../daily-report-hub_sample1/daily_summary.txt     |    18 -
 .../daily-report-hub_sample1/latest_code_diff.md   |    17 -
 .../daily-report-hub_sample1/latest_code_diff.txt  |   145 -
 .../daily-report-hub_sample1/latest_diff.md        |     3 -
 .../daily-report-hub_sample1/latest_diff.txt       |     1 -
 .../daily-report-hub_sample1/metadata.json         |    20 -
 docs/blog/2019-05-28-first-blog-post.md            |    12 +
 docs/blog/2019-05-29-long-blog-post.md             |    44 +
 docs/blog/2021-08-01-mdx-blog-post.mdx             |    24 +
 .../docusaurus-plushie-banner.jpeg                 |   Bin 0 -> 96122 bytes
 docs/blog/2021-08-26-welcome/index.md              |    29 +
 docs/blog/authors.yml                              |    25 +
 docs/blog/tags.yml                                 |    19 +
 docs/docs/activities/2025/_category_.json          |     8 +
 .../2025-08-11/_category_.json                     |     8 +
 .../2025-08-11/daily-report-hub/README.md          |   297 +
 .../2025-08-11/daily-report-hub/_category_.json    |     8 +
 .../2025-08-11/daily-report-hub/daily_code_diff.md | 69584 +++++++++++++++++++
 .../2025-08-11/daily-report-hub/daily_commits.md   |  8246 +++
 .../daily-report-hub/daily_cumulative_diff.md      |    98 +
 .../daily-report-hub/daily_diff_stats.md           |   101 +
 .../2025-08-11/daily-report-hub/daily_summary.md   |   550 +
 .../daily-report-hub/latest_code_diff.md           | 39984 +++++++++++
 .../2025-08-11/daily-report-hub/latest_diff.md     |    18 +
 .../2025-08-11/daily-report-hub/metadata.json      |    27 +
 .../2025-08-11/daily-report-hub_sample1/README.md  |    90 +
 .../daily-report-hub_sample1/_category_.json       |     8 +
 .../daily-report-hub_sample1/ai_daily_report.md    |    68 +
 .../daily-report-hub_sample1/daily_code_diff.md    |  1744 +
 .../daily-report-hub_sample1/daily_commits.md      |  3626 +
 .../daily_cumulative_diff.md                       |    18 +
 .../daily-report-hub_sample1/daily_diff_stats.md   |    21 +
 .../daily-report-hub_sample1/daily_summary.md      |   274 +
 .../daily-report-hub_sample1/latest_code_diff.md   |    69 +
 .../daily-report-hub_sample1/latest_diff.md        |     8 +
 .../daily-report-hub_sample1/metadata.json         |    27 +
 .../_category_.json                                |     8 +
 docs/docs/activities/_category_.json               |     8 +
 docs/docs/ai-features.md                           |    92 +
 docs/docs/faq.md                                   |   157 +
 docs/docs/getting-started.md                       |   229 +
 docs/docs/intro.md                                 |   106 +
 docs/docs/scripts-guide.md                         |   262 +
 docs/docusaurus.config.ts                          |   179 +
 docs/package-lock.json                             | 18807 +++++
 docs/package.json                                  |    49 +
 docs/sidebars.ts                                   |    33 +
 docs/src/components/HomepageFeatures/index.tsx     |    72 +
 .../components/HomepageFeatures/styles.module.css  |    11 +
 docs/src/css/custom.css                            |   125 +
 docs/src/pages/index.module.css                    |    23 +
 docs/src/pages/index.tsx                           |    50 +
 docs/src/pages/markdown-page.md                    |     7 +
 docs/static/.nojekyll                              |     0
 docs/static/img/Pteranodon-social-card.jpg         |   Bin 0 -> 419715 bytes
 docs/static/img/Pteranodon-social-card.png         |   Bin 0 -> 2452231 bytes
 docs/static/img/Pteranodon.png                     |   Bin 0 -> 1944776 bytes
 docs/static/img/docusaurus-social-card.jpg         |   Bin 0 -> 55746 bytes
 docs/static/img/docusaurus.png                     |   Bin 0 -> 5142 bytes
 docs/static/img/favicon-Pteranodon.ico             |   Bin 0 -> 30979 bytes
 docs/static/img/favicon.ico                        |   Bin 0 -> 3626 bytes
 docs/static/img/logo.svg                           |     1 +
 docs/static/img/undraw_docusaurus_mountain.svg     |   171 +
 docs/static/img/undraw_docusaurus_react.svg        |   170 +
 docs/static/img/undraw_docusaurus_tree.svg         |    40 +
 docs/tsconfig.json                                 |     8 +
 example/test_gemini_google_sdk.py                  |    21 +
 example/test_gemini_litellm.py                     |    57 +
 projects/daily-report-hub_sample1/README.md        |    11 -
 projects/daily-report-hub_sample1/commit.txt       |     1 -
 projects/daily-report-hub_sample1/diff.txt         |     4 -
 projects/daily-report-hub_sample1/metadata.json    |     7 -
 projects/daily-report-hub_sample1/update_time.txt  |     1 -
 96 files changed, 147385 insertions(+), 627 deletions(-)
```
