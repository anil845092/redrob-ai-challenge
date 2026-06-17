# Redrob AI Challenge – Intelligent Candidate Discovery

## Overview

This project was developed as part of the Redrob AI Challenge: Intelligent Candidate Discovery.

The objective of the challenge is to identify and rank the top 100 candidates for a Senior AI Engineer position from a dataset containing 100,000 candidate profiles.

## Problem Statement

Recruiters often receive thousands of applications for highly specialized AI roles. Manually reviewing profiles is time-consuming and inefficient.

The goal of this solution is to automate candidate discovery by scoring and ranking candidates based on their relevance to the target job description.

## Dataset

The dataset contains:

* 100,000 candidate profiles
* Professional experience information
* Skills and certifications
* Education history
* Behavioral and recruiter engagement signals
* Open-to-work indicators
* GitHub activity metrics

## Approach

### 1. Data Processing

Candidate records were loaded from the provided JSONL dataset and parsed into a structured format for analysis.

### 2. Feature Extraction

The following features were considered:

#### Technical Skills

* Python
* NLP
* Fine-tuning LLMs
* Embeddings
* LangChain
* Pinecone
* Milvus
* FAISS
* Weaviate
* Qdrant
* Hugging Face Transformers
* TensorFlow
* PyTorch
* Machine Learning
* Deep Learning
* Information Retrieval

#### Experience

* Years of professional experience
* Preference for candidates with 5–9 years of experience

#### Behavioral Signals

* Open-to-work status
* Recruiter response rate
* GitHub activity score
* Profile engagement metrics

### 3. Candidate Scoring

A weighted scoring model was implemented.

The final score is calculated using:

* Technical skill relevance
* Experience alignment
* Behavioral indicators
* Recruiter engagement signals

Candidates with stronger alignment to the Senior AI Engineer role receive higher scores.

### 4. Ranking

All candidates were scored and sorted in descending order.

The top 100 candidates were selected and exported into the required submission format.

## Output Format

The generated output file contains:

* candidate_id
* rank
* score
* reasoning

Example:

candidate_id,rank,score,reasoning

CAND_0002025,1,266,Strong match for Senior AI Engineer role based on skills, experience, and signals.

## Technologies Used

* Python
* Pandas
* JSON
* Google Colab

## Repository Structure

* candidate_ranker.py
* submission.csv
* README.md

## Future Improvements

* Semantic matching using embeddings
* Resume-to-JD similarity scoring
* Experience relevance weighting
* Career history analysis
* Advanced ranking models

## Author

Anil Yadav
