# paperagent

paperagent 是一个集成了从 arXiv 下载论文以及利用本地大模型 (Ollama) 对论文进行评价的 Python 包。该包提供了一个单一接口 `run_agent`，可以传入搜索关键词、下载论文数量、保存路径（默认为 "papers"）和大模型问题（若未指定，默认生成中文摘要并从新意度、有效性、问题大小三个维度进行综合评估），最终将大模型返回的答案（经过 `<think>...</think>` 内容过滤）写入一个包含当前日期的 Markdown 文件中。

---

## Features / 功能

- **Download Research Papers from arXiv / 下载 arXiv 论文**  
  根据用户提供的关键词搜索并下载指定数量的论文 PDF 文件。

- **Language Model Evaluation / 大模型问答**  
  对每篇下载的论文，从 PDF 中提取第一页内容，并利用本地大模型生成中文摘要及论文质量评分。  
  返回内容中会过滤掉 `<think>...</think>` 标签内的内容。

- **Output / 输出**  
  所有论文的标题及大模型的回答将写入到一个 Markdown 文件中，文件名为 `论文质量评估YYYYMMDD.md`，其中 `YYYYMMDD` 表示当前日期。

---

## Input Parameters and Output Details / 输入参数和输出详情

### Input Parameters (输入参数)
- **paper_keyword** (字符串):  
  用于在 arXiv 上搜索论文的关键词。  
  *Example / 示例:* `"object detection"`

- **total_count** (整数):  
  指定需要下载的论文总数量。  
  *Example / 示例:* `5`

- **save_path** (字符串, 默认 "papers"):  
  指定保存下载 PDF 的文件夹路径。若未传入，将默认使用 "papers"。  
  *Example / 示例:* `"downloads"`

- **question** (字符串, 可选):  
  提供给大模型的提问内容；若未指定，则使用默认问题：  
  > "帮我生成这篇文章的中文摘要，并从新意度、有效性、问题大小三个维度综合评估这篇文章的价值，满分十分，生成完中文摘要后，打出你认为的评分。"  
  *Example / 示例:* `"请生成这篇文章的中文摘要，并评估其价值。"`

- **model_name** (字符串, 默认 "deepseek-r1:1.5b"):  
  本地大模型的名称，用于 Ollama 的模型调用。

### Output (输出)
- **PDF 下载**:  
  根据指定关键词和数量，从 arXiv 下载论文 PDF 文件到指定的 `save_path` 文件夹中。

- **大模型回答**:  
  对每篇论文，提取 PDF 的第一页内容作为上下文，并与提问一起传给大模型。大模型返回的答案中会过滤掉 `<think>...</think>` 部分。

- **评估文件**:  
  所有论文的标题和大模型回答会写入一个 Markdown 文件，文件名格式为 `论文质量评估YYYYMMDD.md`（如 `论文质量评估20250307.md`），用于记录每篇论文的中文摘要和综合评分。

---

## Installation / 安装

使用 pip 安装：
```bash
pip install paperagent
```