# 📈 Daily Statistics

```diff
 .SourceSageignore                                  |  55 ++
 .env.example                                       |   2 +
 .github/workflows/sync-to-report-gh.yml            |  52 ++
 .gitignore                                         | 211 +++++++
 LICENSE                                            |  21 +
 README.md                                          | 358 +++++++++++
 easy_dataset_cli/__init__.py                       |   1 +
 easy_dataset_cli/alpaca_converter.py               | 237 +++++++
 easy_dataset_cli/core.py                           |  57 ++
 easy_dataset_cli/file_utils.py                     |  59 ++
 easy_dataset_cli/ga_parser.py                      | 182 ++++++
 easy_dataset_cli/main.py                           | 428 +++++++++++++
 easy_dataset_cli/prompts.py                        |  35 ++
 .../prompts/ga_definition_generation.md            |  47 ++
 easy_dataset_cli/prompts/qa_generation.md          |  46 ++
 .../prompts/qa_generation_with_fulltext.md         |  52 ++
 .../prompts/qa_generation_with_thinking.md         |  53 ++
 easy_dataset_cli/qa_generator.py                   | 681 +++++++++++++++++++++
 easy_dataset_cli/text_splitter.py                  |  17 +
 easy_dataset_cli/utils.py                          |  42 ++
 easy_dataset_cli/xml_utils.py                      | 401 ++++++++++++
 example/input/documents/Touhou_Chireiden.md        | 203 ++++++
 example/input/documents/sample_document.txt        |  14 +
 example/input/documents/sample_ga_definition.md    |  21 +
 example/input/documents/test_short.md              |  16 +
 example/scripts/orin.bat                           |   5 +
 example/scripts/simple.bat                         |   1 +
 fix_xml_generation.py                              |  34 +
 pyproject.toml                                     |  23 +
 tests/test_aggregate_logs.py                       | 145 +++++
 tests/test_answer_extraction.py                    |  56 ++
 tests/test_fixed_parsing.py                        |  68 ++
 tests/test_simple_xml.py                           |  68 ++
 tests/test_subelement.py                           |  59 ++
 tests/test_think_tag_preservation.py               |  57 ++
 tests/test_xml_parsing.py                          | 121 ++++
 36 files changed, 3928 insertions(+)
```
