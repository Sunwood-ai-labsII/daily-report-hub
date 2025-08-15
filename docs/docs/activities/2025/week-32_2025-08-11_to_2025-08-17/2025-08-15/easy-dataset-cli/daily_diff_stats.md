# 📈 Daily Statistics

```diff
 .SourceSageignore                                  |  55 +++
 .env.example                                       |   2 +
 .github/workflows/sync-to-report-gh.yml            |  52 +++
 .gitignore                                         | 211 ++++++++++++
 LICENSE                                            |  21 ++
 README.md                                          | 338 +++++++++++++++++++
 easy_dataset_cli/__init__.py                       |   1 +
 easy_dataset_cli/alpaca_converter.py               | 238 +++++++++++++
 easy_dataset_cli/core.py                           |  53 +++
 easy_dataset_cli/file_utils.py                     |  59 ++++
 easy_dataset_cli/ga_parser.py                      | 182 ++++++++++
 easy_dataset_cli/main.py                           | 369 +++++++++++++++++++++
 easy_dataset_cli/prompts.py                        |  30 ++
 .../prompts/ga_definition_generation.md            |  47 +++
 easy_dataset_cli/prompts/qa_generation.md          |  46 +++
 .../prompts/qa_generation_with_fulltext.md         |  52 +++
 easy_dataset_cli/qa_generator.py                   | 209 ++++++++++++
 easy_dataset_cli/text_splitter.py                  |  17 +
 easy_dataset_cli/utils.py                          |  42 +++
 easy_dataset_cli/xml_utils.py                      | 154 +++++++++
 example/input/documents/Touhou_Chireiden.md        | 203 ++++++++++++
 example/input/documents/sample_document.txt        |  14 +
 example/input/documents/sample_ga_definition.md    |  21 ++
 example/input/documents/test_short.md              |  16 +
 pyproject.toml                                     |  23 ++
 25 files changed, 2455 insertions(+)
```
