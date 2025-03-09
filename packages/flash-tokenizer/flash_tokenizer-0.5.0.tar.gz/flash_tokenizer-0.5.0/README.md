
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/FlashTokenizer_main_dark.png">
    <img alt="FlashTokenizer" src="./assets/FlashTokenizer_main_light.png" width=55%>
  </picture>
</p>
<h1 align="center">
Tokenizer Library for LLM Serving
</h1>


### EFFICIENT AND OPTIMIZED TOKENIZER ENGINE FOR LLM INFERENCE SERVING

FlashTokenizer는 LLM 추론시 사용하는 BertTokenizer와 같은  고성능 tokenizer 구현체 입니다. FlashAttention, FlashInfer와 같이 최고의 속도와 정확도를 보여주며 transformers의 BertTokenizerFast보다 4~5배 빠릅니다.

FlashTokenizer는 아래와 같은 핵심 기능이 포함됩니다.
 * C++17로 구현되었으며 LLVM으로 빌드할 시 가장 빠릅니다.
 * pybind11을 통해 Python에서도 동일하게 빠른 속도를 보여줍니다.
 * Blingfire는 정확도가 낮아 실제로 사용하기에 어려웠지만 FlashBertTokenizer는 높은 정확도와 빠른 속도까지 모두 가지고 있습니다.


<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/TokenizerPerformanceGraph_dark.png">
    <img alt="FlashTokenizer" src="./assets/TokenizerPerformanceGraph_light.png" width=100%>
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/TokenizerPerformanceBar_dark.jpg">
    <img alt="FlashTokenizer" src="./assets/TokenizerPerformanceBar_light.jpg" width=100%>
  </picture>
</p>


| Tokenizer             | Elapsed Time (s) |   titles |   Accuracy |
|-----------------------|----------------|----------|------------|
| BertTokenizer(Huggingface)     |       255.651  |  404,464 |   100 (Baseline)   |
| **FlashBertTokenizer**    |        19.1325 |  404,464 |    99.3248 |
| BertTokenizerFast(HuggingFace) |        75.8732 |  404,464 |    99.8615 |
| BertTokenizerFast(PaddleNLP) |        71.5387 |  404,464 |    99.8615 |
| FastBertTokenizer(Tensorflow-text) |        82.2638 |  404,464 |    99.8507 |
| Blingfire             |        12.7293 |  404,464 |    96.8979 |





FlashInfer는 대규모 언어 모델용 라이브러리이자 커널 생성기로, FlashAttention, SparseAttention, PageAttention, 샘플링 등과 같은 LLM GPU 커널의 고성능 구현을 제공합니다. 플래시인퍼는 LLM 제공 및 추론에 중점을 두고 있으며 다양한 시나리오에서 최첨단 성능을 제공합니다.

FlashInfer is a library and kernel generator for Large Language Models that provides high-performance implementation of LLM GPU kernels such as FlashAttention, SparseAttention, PageAttention, Sampling, and more. FlashInfer focuses on LLM serving and inference, and delivers state-of-the-art performance across diverse scenarios.

<p align="center">
| <a href="https://flashinfer.ai"><b>Blog</b></a> | <a href="https://docs.flashinfer.ai"><b>Documentation</b></a> | <a href="https://join.slack.com/t/flashinfer/shared_invite/zt-2r93kj2aq-wZnC2n_Z2~mf73N5qnVGGA"><b>Slack</b></a>|  <a href="https://github.com/orgs/flashinfer-ai/discussions"><b>Discussion Forum</b></a> |
</p>

[![Release](https://github.com/flashinfer-ai/flashinfer/actions/workflows/release_wheel.yml/badge.svg)](https://github.com/flashinfer-ai/flashinfer/actions/workflows/release_wheel.yml)
[![Documentation](https://github.com/flashinfer-ai/flashinfer/actions/workflows/build-doc.yml/badge.svg)](https://github.com/flashinfer-ai/flashinfer/actions/workflows/build-doc.yml)


Flash BERT tokenizer implementation with C++ backend.

## Installation



```
brew install llvm libomp

```





```bash
pip install -U flash-tokenizer
```

```bash
git clone https://github.com/springkim/flash-tokenizer.git
cd flash-tokenizer
pip install .
```

## Usage

```python
from flash_tokenizer import FlashBertTokenizer
tokenizer = FlashBertTokenizer("path/to/vocab.txt", do_lower_case=True)
# Tokenize text
ids = tokenizer("Hello, world!")
print(ids)
```
