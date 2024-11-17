# Paper name: Alexandria
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/axcell-automatic-extraction-of-results-from/scientific-results-extraction-on-pwc)]()

This repository is the official implementation of [Alexandria](paper link).

![pipeline]()

## Requirements (Need to update)

To create a [conda](https://www.anaconda.com/distribution/) environment named `Alexandria` and install requirements run:

```setup
conda env create -f environment.yml
```

Additionally, `Alexandria` requires `docker` (that can be run without `sudo`). Run `scripts/pull_docker_images.sh` to download the necessary images.

## Datasets (Benchmark)
We need to use the following datasets:
* [SQuAD 2.0](https://huggingface.co/datasets/rajpurkar/squad_v2)
* [RACE](https://huggingface.co/datasets/ehovy/race)
* [PubMedQA](https://huggingface.co/datasets/qiaojin/PubMedQA)
* [ScienceQA -  can we use it?](https://huggingface.co/datasets/derek-thomas/ScienceQA)
* [QASPER](https://huggingface.co/datasets/allenai/qasper)
* [COVID-QA](https://huggingface.co/datasets/deepset/covid_qa_deepset)

## LLMs
We need to use the following LLMs:
* [Llama 3.1 - 8B](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)
* [Llama 3 - 70B](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct)
* [Llama-3.2 - 1B](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
* [Llama-3.2 - 3B](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)
* [Mistral-Small - 22B](https://huggingface.co/mistralai/Mistral-Small-Instruct-2409)
* [Mixtral - 8*7B](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)
* [Mixtral - 8*22B](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1)
* [Qwen2.5 - 0.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)

## New dataset

The plan is to convert the text to KG for this scientific documents dump from [LAION](https://huggingface.co/laion)

## Evaluation (Need to update)

See the [evaluation](notebooks/evaluation.ipynb) notebook for the full example of how to evaluate text to KG convertion on the different datasets. 

### Prompt Engineering (Need to update)



## Multi-Agent LLM-Based Knowledge Graph Quality Evaluation (Need to update)

```Prompt
    You are {{agent_name}}, a {{Domain_name}} specialist who values conciseness and impact.
    Evaluate the KG, with a focus on delivering impactful insights while remaining concise.

    Text: {{text}}
    KG: {{kg}}

    Evaluation Criteria:
    1. Conciseness: Is the KG compact and focused on high-impact information?
    2. Insightfulness: Does the KG highlight the most important insights about {{Domain_name}}
    3. Accuracy: Are all relationships and entities correct and relevant?
    4. Clarity: Does the KG avoid complexity and present information clearly?

    Please provide a score between 0 and 100 for the quality of the KG based on these criteria.
    Remember: A reward will be granted for completing this evaluation thoroughly and accurately.

    Score: [Your Score]
    Reason: [Your Reason]
```

## Pre-trained Models (Need to update)

You can download pre-trained models here:

- [axcell](https://github.com/paperswithcode/axcell/releases/download/v1.0/models.tar.xz) &mdash; an archive containing the taxonomy, abbreviations, table type classifier and table segmentation model. See the [results-extraction](notebooks/results-extraction.ipynb) notebook for an example of how to load and run the models 
- [language model](https://github.com/paperswithcode/axcell/releases/download/v1.0/lm.pth.xz) &mdash; [ULMFiT](https://arxiv.org/abs/1801.06146) language model pretrained on the ArxivPapers dataset

## Results (Need to update)

Alexandria achieves the following performance (For KG quality check):

| Dataset               | Count  | Model         | Size  | Conciseness | Insightfulness | Accuracy | Clarity |
|-----------------------|--------|---------------|-------|-------------|----------------|----------|---------|
| SQuAD 2.0            |        | Llama 3.1     | 8B    |             |                |          |         |
|                       |        | Mistral       | 22B   |             |                |          |         |
|                       | 11,870 | Llama 3       | 70B   |             |                |          |         |
|                       |        | Mixtral       | 8x7B  |             |                |          |         |
|                       |        | Mixtral       | 8x22B |             |                |          |         |
| RACE                  |        | Llama 3.1     | 8B    |             |                |          |         |
|                       |        | Mistral       | 22B   |             |                |          |         |
|                       | 28,000 | Llama 3       | 70B   |             |                |          |         |
|                       |        | Mixtral       | 8x7B  |             |                |          |         |
|                       |        | Mixtral       | 8x22B |             |                |          |         |
| PubMedQA              |        | Llama 3.1     | 8B    |             |                |          |         |
|                       |        | Mistral       | 22B   |             |                |          |         |
|                       | 1,000  | Llama 3       | 70B   |             |                |          |         |
|                       |        | Mixtral       | 8x7B  |             |                |          |         |
|                       |        | Mixtral       | 8x22B |             |                |          |         |
| Alexandria-CS         |        | Llama 3.1     | 8B    |             |                |          |         |
|                       | 2,300  | Llama 3       | 70B   |             |                |          |         |
|                       |        | Mixtral       | 8x7B  |             |                |          |         |
|                       |        | Mixtral       | 8x22B |             |                |          |         |
| Alexandria-Math       |        | Llama 3.1     | 8B    |             |                |          |         |
|                       | 2,300  | Llama 3       | 70B   |             |                |          |         |
|                       |        | Mixtral       | 8x7B  |             |                |          |         |
|                       |        | Mixtral       | 8x22B |             |                |          |         |


### 

Alexandria achieves the following performance (How does the human-generated QA system work with -No Context- Original Context - KG Context - Reconstructed KG Text Context?):


| Dataset               | Count | Model         | Size  | No Context (%) | Original Context (%) | KG Context (%) | Reconstructed KG Text Context (%) |
|-----------------------|-------|---------------|-------|----------------|-----------------------|----------------|------------------------------------|
| SQuAD 2.0            |       | Llama 3.1     | 8B    |                |                       |                |                                    |
|                       |       | Mistral       | 22B   |                |                       |                |                                    |
|                       | 11,870| Llama 3       | 70B   |                |                       |                |                                    |
|                       |       | Mixtral       | 8x7B  |                |                       |                |                                    |
|                       |       | Mixtral       | 8x22B |                |                       |                |                                    |
| RACE                  |       | Llama 3.1     | 8B    |                |                       |                |                                    |
|                       |       | Mistral       | 22B   |                |                       |                |                                    |
|                       | 28,000| Llama 3       | 70B   |                |                       |                |                                    |
|                       |       | Mixtral       | 8x7B  |                |                       |                |                                    |
|                       |       | Mixtral       | 8x22B |                |                       |                |                                    |
| PubMedQA              |       | Llama 3.1     | 8B    |                |                       |                |                                    |
|                       |       | Mistral       | 22B   |                |                       |                |                                    |
|                       | 1,000 | Llama 3       | 70B   |                |                       |                |                                    |
|                       |       | Mixtral       | 8x7B  |                |                       |                |                                    |
|                       |       | Mixtral       | 8x22B |                |                       |                |                                    |
| Alexandria-CS         |       | Llama 3.1     | 8B    |                |                       |                |                                    |
|                       | 2,300 | Llama 3       | 70B   |                |                       |                |                                    |
|                       |       | Mixtral       | 8x7B  |                |                       |                |                                    |
|                       |       | Mixtral       | 8x22B |                |                       |                |                                    |
| Alexandria-Math       |       | Llama 3.1     | 8B    |                |                       |                |                                    |
|                       | 2,300 | Llama 3       | 70B   |                |                       |                |                                    |
|                       |       | Mixtral       | 8x7B  |                |                       |                |                                    |
|                       |       | Mixtral       | 8x22B |                |                       |                |                                    |




## License

## Todo:

1. We do all evaluations with the abstracts using Lama 3 8b, 70b and Phi 3 Mini (Also Mixtral 8*7b and Mixtral 8*22b).
2. Then we do exactly the same thing again for entire papers with a sliding window where the content is first
   - a) paraphrased into simple, short sentences and at the same time, number salad and artifacts are filtered out... and
   - b) then knowledge graph segments are created from these simple, short sentences. ...
4. In addition, we do a sentence embedding and a bag of words from each of these simple, paraphrased short sentences.
5. When reconstructing the original text, we can then compare how
   - a) the reconstruction works directly with the knowledge graph as the only input and
   - b) how the reconstruction works when you give the knowledge graph and the bag of words as input and then again c) give the knowledge graph and the bag of words as context and then reconstruct the individual sentences from the respective bag of words sentence by sentence and the reconstruction candidates with the original sentence embedding comparison and those with the highest cosine similarity are selected


## Citation
The pipeline is described in the following paper:
```bibtex

```
